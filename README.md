# 🖐️ Virtual Touchpad Pro

> Control your computer using hand gestures powered by **Python**, **OpenCV**, and **MediaPipe**.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![Status](https://img.shields.io/badge/Status-Under%20Development-yellow)

---

# 📖 Overview

Virtual Touchpad Pro is an AI-powered virtual touchpad that allows users to control the mouse cursor using only hand gestures through a webcam.

The project is designed with a clean, modular architecture that makes it easy to maintain, extend, and experiment with new gestures.

The long-term goal is to create a professional desktop application suitable for:

- Portfolio Projects
- College Final Year Projects
- Hackathons
- Resume Showcase
- AI & Computer Vision Learning

---

# ✨ Features

## ✅ Currently Available

- Webcam input
- Hand detection
- Hand landmark tracking
- Finger state detection
- Cursor movement
- Gesture recognition engine
- Modular project architecture
- Logging system
- Tracking visualization

---

## 🚧 In Development

- Left Click
- Right Click
- Double Click
- Drag & Drop
- Scroll
- Cursor Smoothing
- Gesture Calibration
- FPS Counter
- Overlay UI

---

## 📌 Planned Features

- Zoom Gesture
- Screenshot Gesture
- Volume Control
- Brightness Control
- Multi-Hand Support
- Custom Gesture Configuration
- Settings Window
- Multiple Camera Support
- Windows Executable
- Auto Updater

---

# 📂 Project Structure

```text
VirtualTouchpadPro/
│
├── app.py
│
├── assets/
│
├── config/
│   ├── constants.py
│   └── settings.py
│
├── core/
│   ├── __init__.py
│   ├── bounding_box.py
│   ├── camera.py
│   ├── enums.py
│   ├── finger_state.py
│   ├── gesture_engine.py
│   ├── hand.py
│   ├── hand_detector.py
│   ├── landmark.py
│   ├── mouse_controller.py
│   ├── smoothing.py
│   └── tracker.py
│
├── gestures/
│   ├── __init__.py
│   ├── base.py
│   ├── move.py
│   └── left_click.py
│
├── tests/
│
├── utils/
│
├── README.md
├── WORKING.md
└── requirements.txt
```

---

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/M-sahoo2007/VirtualTouchpadPro.git
```

```bash
cd VirtualTouchpadPro
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run

```bash
python app.py
```

---

# 🖐️ Current Gestures

| Gesture | Action | Status |
|----------|--------|--------|
| ☝ Index Finger | Move Cursor | ✅ |
| 🤏 Thumb + Index | Left Click | 🚧 |
| 🤏 Thumb + Middle | Right Click | 🚧 |
| ✋ Open Palm | Drag | 🚧 |
| ✌ Three Fingers | Scroll | 🚧 |

---

# 🏗️ Architecture

```text
Camera
      │
      ▼
Hand Detector
      │
      ▼
Gesture Engine
      │
      ▼
Gesture Detectors
      │
      ▼
Mouse Controller
      │
      ▼
Operating System Cursor
```

---

# 🧠 Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

---

# 🚀 Development Roadmap

## Phase 1

- [x] Camera
- [x] Hand Detection
- [x] Finger Detection
- [x] Mouse Movement

---

## Phase 2

- [ ] Gesture Engine
- [ ] Left Click
- [ ] Right Click
- [ ] Drag
- [ ] Scroll

---

## Phase 3

- [ ] Cursor Smoothing
- [ ] Motion Prediction
- [ ] Gesture Calibration

---

## Phase 4

- [ ] Overlay UI
- [ ] FPS Counter
- [ ] Tracking Confidence

---

## Phase 5

- [ ] Volume Control
- [ ] Brightness Control
- [ ] Screenshot
- [ ] Presentation Mode

---

## Phase 6

- [ ] Settings Panel
- [ ] Multiple Cameras
- [ ] Themes
- [ ] User Profiles

---

## Phase 7

- [ ] Performance Optimization
- [ ] Async Camera
- [ ] Memory Optimization

---

## Phase 8

- [ ] Windows Installer
- [ ] Executable
- [ ] Documentation
- [ ] Release v1.0

---

# 📸 Screenshots

Coming Soon...

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.

2. Create a feature branch.

```bash
git checkout -b feature/my-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature/my-feature
```

5. Open a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Maheswar Sahoo**

Computer Science Engineering Student

Interested in

- Artificial Intelligence
- Computer Vision
- Python
- Cybersecurity
- Open Source

---

# ⭐ Support

If you find this project useful,

⭐ Star the repository

🍴 Fork it

🐞 Report issues

💡 Suggest new features

---

**Virtual Touchpad Pro** is an educational open-source project built to explore modern computer vision techniques for touchless human-computer interaction.