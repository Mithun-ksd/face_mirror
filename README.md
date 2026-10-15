# Face Mirror

Face Mirror displays a horizontally mirrored webcam feed, detects faces, draws a rectangle around each detected face, and shows the current face count.

## Concept

This project demonstrates basic real-time face detection using OpenCV. The live camera image behaves like a mirror, while detected faces are highlighted with a label.

## Model Definition

The program uses OpenCV's built-in **Haar cascade frontal-face detector**, loaded from `haarcascade_frontalface_default.xml` through `cv2.data.haarcascades`.

This is a pretrained classical computer-vision detector, not a custom model trained by this project. The detector runs on grayscale frames using OpenCV's `detectMultiScale()` method.

## How It Works

1. Open the default webcam.
2. Load the frontal-face Haar cascade XML file bundled with OpenCV.
3. Read each camera frame and flip it horizontally.
4. Convert the frame to grayscale.
5. Run the detector to locate faces.
6. Draw a rectangle and the label `Face detected` around each face.
7. Display the number of faces found and the live mirrored video.
8. Release the camera and close the display window when the user quits.

## Requirements

- Python 3.9 or newer is a reasonable starting point.
- A working webcam and camera permissions.
- A desktop environment capable of displaying OpenCV windows.
- Python package:
  - `opencv-python`

The script also uses the Python standard-library module `sys`.

## Installation

Creating a virtual environment is recommended.

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install OpenCV:

```bash
python -m pip install --upgrade pip
python -m pip install opencv-python
```

## Running the Program

If the script is named `face_mirror.py`:

```bash
python face_mirror.py
```


## Controls

- Press `Q` in the camera window to quit.

## Configuration

- `cv2.VideoCapture(0)`: selects the default camera. Try index `1` if needed.
- `scaleFactor=1.15`: controls image scaling between detection passes.
- `minNeighbors=5`: helps filter weak candidate detections.
- `minSize=(60, 60)`: sets the minimum face-detection window size.

## Troubleshooting

- **Webcam unavailable:** Check camera permissions, close other applications using the camera, or try camera index `1`.
- **Cascade cannot load:** Reinstall `opencv-python` and verify that OpenCV's data files are available.
- **Faces are missed:** Improve lighting, face the camera, and remember that this frontal-face detector may not work well at steep angles.

## Limitations

- Detection quality varies with lighting, camera angle, and face visibility.
- A Haar cascade may miss faces at unusual angles or under difficult conditions.
- This project performs face detection only; it does not identify who a person is.
