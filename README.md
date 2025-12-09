# Drowsiness Detection System 🚨

This project is a **real-time drowsiness detection system** that uses computer vision techniques to monitor eye activity and trigger an alarm when drowsiness is detected.  

It utilizes **OpenCV**, **dlib**, and **facial landmark detection** to track the **Eye Aspect Ratio (EAR)** and determine whether the user is awake or drowsy.

---

## 📌 Features
- Real-time face and eye detection using **dlib**’s 68-point facial landmark predictor.  
- Calculates **Eye Aspect Ratio (EAR)** to detect eye closure.  
- Detects if eyes remain closed for more than **2 seconds** (adjustable).  
- Plays a loud **alarm beep** (`winsound`) if drowsiness is detected.  
- Displays the status (`Awake` or `Drowsy`) on the video feed.  

---

## 🛠️ Requirements
Install the required libraries before running the script:

```bash
pip install opencv-python dlib numpy scipy

```
---

## ⚙️ Key Parameters

Threshold EAR: 0.25 → below this, eyes are considered closed.

Required Frames: depends on your webcam FPS (~2 seconds).

Alarm Sound: Plays a 1000Hz beep for 2 seconds on Windows.

---


## 🚀 Future Improvements

🔊 Cross-platform alarm (Linux/Mac support).

🚨 Add yawn detection (Mouth Aspect Ratio).

📝 Log drowsiness events with timestamps.

📱 Build a mobile app version.

🌐 Integrate with IoT (car safety system).

---
