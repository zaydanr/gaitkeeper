# **GaitKeeper**
**MedTech 2025 Hackathon Project**  
GaitKeeper: Real-Time Gait Analysis for Rehabilitation  
*A MedTech 2025 Hackathon Project*  

 <img width="838" alt="Screenshot 2025-02-23 at 11 34 25 AM" src="https://github.com/user-attachments/assets/1f34bb80-b559-4648-b79c-c1796257165a" />

<img width="453" alt="Screenshot 2025-02-23 at 11 35 07 AM" src="https://github.com/user-attachments/assets/2972e449-af08-4cbf-9b85-f0da78e7acfe" />
<img width="233" alt="Screenshot 2025-02-23 at 11 41 14 AM" src="https://github.com/user-attachments/assets/decfa0dc-835a-4530-8243-bd6886dad2a3" />

<img width="830" alt="Screenshot 2025-02-23 at 11 39 59 AM" src="https://github.com/user-attachments/assets/b4d305d3-af39-4142-beb5-dd3a9f8e8a08" />

---

## 🏆 **Pitch**  
Rehabilitation patients struggle to track their gait accurately.  
Therapists face **burnout** from repetitive gait assessments.  
Lack of **real-time feedback** slows recovery.  

### **🔹 Solution**  
GaitKeeper is an innovative, **low-cost wearable** that provides **real-time gait analysis** using **IMU sensors and AI-based processing (GaitMap API)**.  
It integrates seamlessly with **telehealth platforms** for remote rehabilitation.  

---

## 🚨 **The Problem: Why GaitKeeper?**  

### **Challenges in Gait Rehabilitation**  
✅ Patients lack access to **affordable gait tracking tools** for at-home therapy.  
✅ Therapists manually track gait, leading to **burnout** and inconsistencies.  
✅ No **real-time feedback** on progress, causing slower recovery.  

### **User Needs**  
👩‍🦽 **Patients:** Need a simple, wearable **gait monitoring** solution.  
👨‍⚕️ **Therapists:** Need an **automated** tracking tool to **reduce workload**.  
🏥 **Healthcare systems:** Need a **scalable, low-cost** rehabilitation tool.  

---

## 🔬 **Our Solution: GaitKeeper**  

GaitKeeper is a **wearable device** that uses **IMU sensors and force sensors** to track gait **in real-time**.  
It integrates with the **GaitMap API** to detect abnormalities, track rehabilitation progress, and predict fall risks.  

✅ **Key Features:**  
- **Stride analysis, step symmetry, gait speed, cadence tracking**  
- **Real-time gait visualization**  
- **Remote monitoring for therapists & clinicians**  
- **Affordable & lightweight wearable**  

📷 **Prototype Image:** *(Include an image here of the device being worn.)*  
🎥 **Video Demo:** *(Include a link to the video.)*  

---

## 🛠 **How It Works**  

1️⃣ **User Starts Data Capture:**  
   - Press a button or trigger data collection via **JSON API**.  

2️⃣ **Data Transmission:**  
   - The system sends data **via MQTT** from two **IMU sensors**.  

3️⃣ **Data Processing:**  
   - **Raw sensor data → CSV file → GaitMap API analysis.**  
   - Extracts **gait speed, stride length, cadence, stability metrics, and anomalies.**  

4️⃣ **Real-Time Visualization & Alerts:**  
   - Patients and therapists receive **instant feedback** on progress.  
   - AI models predict **fall risks & mobility impairments.**  

---

## 🏗 **Hardware Components**  

| Component      | Function  |
|---------------|-----------|
| **ESP32**     | Microcontroller for data processing & communication |
| **IMU Sensors** | Captures motion data (acceleration, angular velocity, orientation) |
| **SD Card Module** | Stores raw gait data locally |
| **Regulator** | Ensures stable power delivery |
| **Button**    | Manually starts/stops data collection |
| **LED Indicator** | Provides real-time system status |
| **Battery-Powered** | Enables portable use |
| **Velcro Strap** | Attaches the sensor to the shoe for accurate data capture |

---

## 📊 **Software Stack & API Usage**  

- **Flask** → Web interface for real-time gait analysis.  
- **Matplotlib** → Plots gait parameters dynamically.  
- **GaitMap API** → Processes IMU data to extract **stride length, cadence, stability, etc.**  
- **MQTT Protocol** → Streams data from sensors to the cloud.  

---

## 🧑‍💻 **Installation & Setup**  

```bash
git clone https://github.com/your-username/GaitKeeper.git
cd GaitKeeper

```bash
pip install -r requirements.txt

```bash
python app.py
