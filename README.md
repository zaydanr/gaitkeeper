# GaitKeeper
MedTech 2025 Hackathon Project
GaitKeeper: Real-Time Gait Analysis for Rehabilitation
A MedTech 2025 Hackathon Project


(Insert an image of the prototype here.)

🏆 Pitch
Rehabilitation patients struggle to track their gait accurately.
Therapists face burnout from repetitive gait assessments.
Lack of real-time feedback slows recovery.

🔹 Solution: GaitKeeper is an innovative, low-cost wearable that provides real-time gait analysis using IMU sensors and AI-based processing (GaitMap API). It integrates seamlessly with telehealth platforms for remote rehabilitation.

🚨 The Problem: Why GaitKeeper?
Challenges in Gait Rehabilitation
✅ Patients lack access to affordable gait tracking tools for at-home therapy.
✅ Therapists manually track gait, leading to burnout and inconsistencies.
✅ No real-time feedback on progress, causing slower recovery.

User Needs
👩‍🦽 Patients: Need a simple, wearable gait monitoring solution.
👨‍⚕️ Therapists: Need an automated tracking tool to reduce workload.
🏥 Healthcare systems: Need a scalable, low-cost rehabilitation tool.

🔬 Our Solution: GaitKeeper
GaitKeeper is a wearable device that uses IMU sensors and force sensors to track gait in real-time.
It integrates with the GaitMap API to detect abnormalities, track rehabilitation progress, and predict fall risks.

✅ Key Features:

Stride analysis, step symmetry, gait speed, cadence tracking
Real-time gait visualization
Remote monitoring for therapists & clinicians
Affordable & lightweight wearable
📷 Prototype Image: (Include an image here of the device being worn.)
🎥 Video Demo: (Include a link to the video.)

🛠 How It Works
User Starts Data Capture: Press a button or trigger data collection via JSON API.
Data Transmission: The system sends data via MQTT from two IMU sensors.
Data Processing:
Raw sensor data → CSV file → GaitMap API analysis.
Extracts gait speed, stride length, cadence, stability metrics, and anomalies.
Real-Time Visualization & Alerts:
Patients and therapists receive instant feedback on progress.
AI models predict fall risks & mobility impairments.
🏗 Hardware Components
Component	Function
ESP32	Microcontroller for data processing & communication
IMU Sensors	Captures motion data (acceleration, angular velocity, orientation)
SD Card Module	Stores raw gait data locally
Regulator	Ensures stable power delivery
Button	Manually starts/stops data collection
LED Indicator	Provides real-time system status
Battery-Powered	Enables portable use
Velcro Strap	Attaches the sensor to the shoe for accurate data capture
📊 Software Stack & API Usage
Flask → Web interface for real-time gait analysis.
Matplotlib → Plots gait parameters dynamically.
GaitMap API → Processes IMU data to extract stride length, cadence, stability, etc.
MQTT Protocol → Streams data from sensors to the cloud.
🧑‍💻 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/GaitKeeper.git
cd GaitKeeper
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Flask App
bash
Copy
Edit
python app.py
Open http://127.0.0.1:5000/ in your browser.
Click Run Gait Analysis to generate real-time gait plots.
📈 Example Output: Gait Analysis Plot
Here’s a sample stride time analysis plot generated from GaitKeeper:


(Replace with actual plot image.)

🔹 Insights from the Data:

Higher stride time variability → Indicates possible mobility impairments.
Sudden drop in stride length → Could signal instability or muscle fatigue.
Irregular cadence → Can indicate neurological disorders or injury recovery delays.
🚀 Future Enhancements
🔜 Live feedback via mobile app for rehabilitation exercises.
🔜 Machine Learning models for fall risk prediction.
🔜 Integration with smart home assistants for voice-guided therapy.

🤝 Contributors
👩‍💻 Your Name – Software & Gait Analysis
👨‍🔬 Teammate Name – Hardware & Wearables
👨‍⚕️ [Teammate Name] – Medical Research & User Testing

📬 Have feedback? Contact us at your-email@example.com

🌟 Support & Contributions
We welcome contributions!

Submit issues, feature requests, or pull requests to help improve GaitKeeper.
Star ⭐ this repo if you find it useful!
📜 License
This project is open-source under the MIT License.

🎥 Watch Our Demo
(Insert a YouTube or Google Drive link to your demo video.)

🔥 GaitKeeper: The Future of AI-Powered Gait Analysis! 🚶‍♂️💡
Next Steps for You
✅ Add actual images & video links where placeholders (path/to/...) are used.
✅ Update the GitHub repository with a docs/ folder containing example CSVs or data files.
✅ Test setup instructions on a fresh system to confirm installation steps work smoothly.
Would you like a GitHub Wiki or PDF documentation version of this? 🚀
