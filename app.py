import matplotlib
matplotlib.use("Agg")
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify, flash, send_file
from flask_assets import Environment
import time
import matplotlib.pyplot as plt
import io

# Import assets and forms
from assets import bundles
from forms import InputForm

# Import GaitMap processing functions
from gaitmap.example_data import get_healthy_example_imu_data_not_rotated
from gaitmap.preprocessing import sensor_alignment
from gaitmap.stride_segmentation import BarthDtw
from gaitmap.event_detection import RamppEventDetection
from gaitmap.trajectory_reconstruction import StrideLevelTrajectory
from gaitmap.parameters import TemporalParameterCalculation, SpatialParameterCalculation

app = Flask(__name__)
app.config['SECRET_KEY'] = '7b7e30111ddc1f8a5b1d80934d336798'

# Register assets (CSS/JS bundling)
assets = Environment(app)
assets.register(bundles)

def process_gait_data():
    sampling_rate_hz = 204.8
    dataset = get_healthy_example_imu_data_not_rotated()

    # Preprocessing: Align data to gravity
    dataset_aligned = sensor_alignment.align_dataset_to_gravity(dataset, sampling_rate_hz)

    # Convert IMU data to the correct coordinate system (foot-based frame)
    from gaitmap.utils.coordinate_conversion import convert_to_fbf
    bf_data = convert_to_fbf(dataset_aligned, left_like="left_", right_like="right_")

    # Rename columns to match expected format for segmentation
    bf_data = bf_data.rename(columns={
        'acc_x': 'acc_pa', 'acc_y': 'acc_ml', 'acc_z': 'acc_si',
        'gyr_x': 'gyr_pa', 'gyr_y': 'gyr_ml', 'gyr_z': 'gyr_si'
    })

    # Stride Segmentation
    dtw = BarthDtw()
    segmented_data = dtw.segment(data=bf_data, sampling_rate_hz=sampling_rate_hz)

    # Event Detection
    ed = RamppEventDetection()
    ed.detect(data=bf_data, stride_list=segmented_data.stride_list_, sampling_rate_hz=sampling_rate_hz)

    # Convert columns back to expected format before trajectory estimation
    bf_data_for_trajectory = bf_data.rename(columns={
        'acc_pa': 'acc_x', 'acc_ml': 'acc_y', 'acc_si': 'acc_z',
        'gyr_pa': 'gyr_x', 'gyr_ml': 'gyr_y', 'gyr_si': 'gyr_z'
    }).reset_index(drop=True)

    # Trajectory Reconstruction
    trajectory = StrideLevelTrajectory()
    trajectory.estimate(data=bf_data_for_trajectory, stride_event_list=ed.min_vel_event_list_, sampling_rate_hz=sampling_rate_hz)

    # Temporal Parameter Calculation
    temporal_params = TemporalParameterCalculation()
    temporal_params.calculate(stride_event_list=ed.min_vel_event_list_, sampling_rate_hz=sampling_rate_hz)

    # Spatial Parameter Calculation
    spatial_params = SpatialParameterCalculation()
    spatial_params.calculate(
        stride_event_list=ed.min_vel_event_list_, 
        positions=trajectory.position_, 
        orientations=trajectory.orientation_, 
        sampling_rate_hz=sampling_rate_hz
    )

    # Prepare results (for plotting, we won't return JSON here)
    results = {
        "num_strides": {k: len(v) for k, v in ed.min_vel_event_list_.items()},
        "temporal_params": temporal_params.parameters_pretty_,
        "spatial_params": spatial_params.parameters_pretty_
    }
    return results

# Route to Return Plot as an Image
@app.route('/plot_analysis', methods=["GET"])
def plot_analysis():
    results = process_gait_data()
    temporal = results.get("temporal_params", {})

    # Try to extract stride_time from the temporal parameters.
    # Adjust the sensor key ("left_sensor") and parameter key ("stride_time") as needed.
    stride_times = []
    if isinstance(temporal, dict) and "left_sensor" in temporal:
        sensor_data = temporal["left_sensor"]
        if isinstance(sensor_data, dict) and "stride_time" in sensor_data:
            stride_times = sensor_data["stride_time"]

    # Fallback: If stride_times is empty, use a dummy list
    # if not stride_times:
    #     stride_times = [1.0, 1.2, 1.1, 1.3, 1.2, 1.4, 1.1]

    # # Create a plot using Matplotlib
    # plt.figure(figsize=(10, 6))
    # plt.plot(stride_times, marker='o', linestyle='-', color='blue')
    # plt.title("Stride Time Across Strides")
    # plt.xlabel("Stride Index")
    # plt.ylabel("Stride Time (s)")
    # plt.grid(True)

    # Read imu_data.csv
    imu_data = pd.read_csv('imu_data.csv')

    # Plot the data
    plt.figure(figsize=(10, 6))
    # first row is time, second row is acc_x, third row is acc_y, fourth row is acc_z
    plt.plot(imu_data.iloc[:, 0], imu_data.iloc[:, 1], label='acc_x')
    plt.plot(imu_data.iloc[:, 0], imu_data.iloc[:, 2], label='acc_y')
    plt.plot(imu_data.iloc[:, 0], imu_data.iloc[:, 3], label='acc_z')
    plt.title("IMU Data")
    plt.xlabel("Time (ms)")
    plt.ylabel("Acceleration (m/s^2)")
    plt.legend()
    plt.grid(True)

    # Save plot to a BytesIO buffer
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches="tight")
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

# Main Route (Homepage)
@app.route('/')
def index():
    return render_template('index.html', data=None)

# Form Route
@app.route('/form', methods=['GET', 'POST'])
def form():
    inputForm = InputForm()
    data = None
    if inputForm.inputString.data:
        time.sleep(2)
        data = inputForm.inputString.data
    return render_template('form.html', data=data, inputForm=inputForm)

# Route to Run Gait Analysis (returns JSON results)
@app.route("/run_analysis", methods=["GET"])
def run_analysis():
    results = process_gait_data()
    # Instead of returning JSON, we might simply print or log the results
    # For now, we'll return a simple text response indicating completion.
    return "Gait analysis complete. Check the logs for details."

# Dummy Routes for Start/Stop Test
@app.route('/start_test', methods=['POST'])
def start_test():
    return "Test started!", 200

@app.route('/stop_test', methods=['POST'])
def stop_test():
    return "Test stopped!", 200

if __name__ == '__main__':
    app.run(debug=True)
