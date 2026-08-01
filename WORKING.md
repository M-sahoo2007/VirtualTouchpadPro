# Virtual Touchpad Pro - Working Guide

## Current Status

**Version:** 0.1.0 (Development)

This document explains the gestures currently implemented in the application and how to use them.

---

# Requirements

* Python 3.11+
* Webcam
* Good lighting
* One hand visible to the camera

---

# Starting the Application

Activate the virtual environment.

```bash
.venv\Scripts\activate
```

Run the application.

```bash
python app.py
```

A webcam window titled **Virtual Touchpad Pro** should appear.

---

# Current Features

| Feature            | Status         |
| ------------------ | -------------- |
| Camera             | ✅ Working      |
| Hand Detection     | ✅ Working      |
| Landmark Detection | ✅ Working      |
| Finger Detection   | ✅ Working      |
| Cursor Movement    | ✅ Working      |
| Left Click         | 🚧 Improving   |
| Right Click        | 🚧 Improving   |
| Drag               | 🚧 Basic       |
| Scroll             | 🚧 Basic       |
| Double Click       | ❌ Not Finished |
| Volume Control     | ❌ Planned      |
| Brightness Control | ❌ Planned      |

---

# Gesture Controls

## 1. Move Cursor

**Gesture**

* Raise only your index finger.

**Action**

Moves the mouse cursor.

---

## 2. Left Click

**Gesture**

Touch your thumb and index finger together (pinch).

**Action**

Performs a left mouse click.

**Current Status**

Under calibration. The pinch distance threshold is still being tuned.

---

## 3. Right Click

**Gesture**

Touch your thumb and middle finger together.

**Action**

Performs a right mouse click.

---

## 4. Drag

**Gesture**

Open all five fingers.

**Action**

Starts drag mode.

Release the gesture to stop dragging.

---

## 5. Scroll Up

**Gesture**

Raise:

* Index finger
* Middle finger
* Ring finger

**Action**

Scrolls upward.

---

## 6. Pause

**Gesture**

Close all fingers.

**Action**

Stops dragging and ignores mouse actions.

---

# On-Screen Information

The application currently displays:

* Hand Type
* Detected Gesture
* Number of Raised Fingers
* Index Finger Coordinates
* Hand Bounding Box

---

# Keyboard Shortcuts

| Key | Action               |
| --- | -------------------- |
| ESC | Exit the application |

---

# Recommended Camera Position

* Place the camera about 40–70 cm from your hand.
* Keep your hand inside the camera frame.
* Avoid dark environments.
* Avoid cluttered backgrounds.
* Use consistent lighting.

---

# Known Issues

* Left-click sensitivity is still being calibrated.
* Scroll direction is basic.
* Drag needs hold-time detection.
* Cursor smoothing will be improved.
* Multi-hand support is not yet enabled.

---

# Planned Features

* Stable left click
* Stable right click
* Double click
* Drag and drop
* Smooth scrolling
* Zoom gesture
* Volume control
* Brightness control
* Screenshot gesture
* Media controls
* FPS counter
* Settings window
* Calibration mode
* Multi-monitor support

---

# Project Roadmap

## Phase 1

* Camera
* Hand Detection
* Cursor Movement

**Status:** ✅ Complete

## Phase 2

* Gesture Recognition
* Mouse Actions

**Status:** 🚧 In Progress

## Phase 3

* Cursor Smoothing
* Gesture Calibration

**Status:** Planned

## Phase 4

* Professional UI
* Performance Optimization

**Status:** Planned

## Phase 5

* Packaging
* Windows Executable

**Status:** Planned

---

# Troubleshooting

## Camera does not open

* Close any other application using the webcam.
* Check the correct camera index in the configuration.

## Cursor does not move

* Ensure only one hand is visible.
* Keep your hand inside the tracking area.

## Left click does not work

* Ensure your thumb and index finger are touching.
* Verify the pinch distance threshold in the gesture engine.
* Improve lighting for more accurate landmark detection.

## Application crashes

Run:

```bash
python app.py
```

and review the error messages in the terminal.

---

# Author

**Maheswar**

Virtual Touchpad Pro

Built using:

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
