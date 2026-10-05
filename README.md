# AI-Based Solar-Powered Farm Surveillance 🌾

**Farm Guardian** is an intelligent, real-time animal detection system built to protect agricultural fields from animal intrusion. Using a pretrained **YOLOv8** model and **OpenCV**, this system utilizes live webcam feeds to identify various animals that commonly damage crops and alerts farmers instantly.

## 🚀 Features

- **Real-Time Detection:** Processes live video feeds to detect animals instantly.
- **YOLOv8 Integration:** Leverages the state-of-the-art YOLOv8 object detection model for high accuracy and speed.
- **Specific Animal Targeting:** Pre-configured to recognize common farm intruders from the COCO dataset (e.g., birds, cats, dogs, horses, sheep, cows, elephants, bears, zebras, giraffes).
- **Lightweight & Efficient:** Designed to run efficiently on edge devices, paving the way for solar-powered deployment.

## 🛠️ Technologies Used

- **Python 3**
- **Ultralytics YOLOv8** (Object Detection)
- **OpenCV** (Computer Vision & Video Processing)
- **PyFiglet** (CLI Aesthetics)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DevanshKhandar/AI-Based-Solar-Powered-Farm-Surveillance.git
   cd AI-Based-Solar-Powered-Farm-Surveillance
   ```

2. **Install required dependencies:**
   ```bash
   pip install ultralytics opencv-python pyfiglet
   ```

3. **Run the detector:**
   ```bash
   python animal_detect.py
   ```

## 🎮 Usage

When you run the script, it will access your primary webcam and open a live feed window. 
- Bounding boxes and confidence scores will appear around any detected animals in real-time.
- Press the **`q`** key while focused on the video window to safely quit the program.

## 🔮 Future Scope

- Integration with solar-powered IoT hardware (e.g., Raspberry Pi or Jetson Nano) for off-grid farm deployment.
- Automated sound alerts (sirens, ultrasonic repellents) triggered upon detection.
- SMS/Email notifications sent directly to the farmer's smartphone.

---
*Developed by [Devansh Khandar](https://github.com/DevanshKhandar).*
