#  Face Detection with OpenCV (Python)

A simple face detection application built with **OpenCV** using **Haar Cascade classifiers**.  
This project detects human faces in a video file and displays real-time **FPS (Frames Per Second)**.

This repository is created as a **first learning-oriented OpenCV project**.

---

##  Features
- Face detection using Haar Cascade
- Video file input
- Real-time FPS calculation
- Bounding boxes and face labels
- Lightweight and beginner-friendly implementation

---

##  Requirements
- Python 3.x
- OpenCV

Install dependency:
```bash
pip install opencv-python

---

## How to Run:

1. Clone the repository:
```
git clone https://github.com/ms-sc0field/facedetector.git
cd facedetector
```

Run the script:
`python detect_faces.py`
Press Q to quit the application.

---

## How It Works:

Reads frames from a video file
- Resizes frames for performance
- Converts frames to grayscale
- Detects faces using Haar Cascade classifier
- Draws bounding boxes and labels
- Calculates FPS using frame time difference

---

## Notes:
* Haar Cascades are fast but not highly accurate compared to modern deep learning models.
* This project focuses on simplicity and learning rather than production-level performance.

---

## Possible Improvements:
- Webcam support
- Deep learning–based face detection (DNN / YOLO / MediaPipe)
- Face recognition
- Performance optimization
