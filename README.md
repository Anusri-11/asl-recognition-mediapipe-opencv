# Sign Language Detector

A computer vision project to detect and classify hand signs for the alphabets A, B, C, D, E, F, and L using a webcam, OpenCV, and MediaPipe. The model is trained using scikit-learn.

## Features
- Collect your own dataset for 7 sign language classes (A, B, C, D, E, F, L)
- Train a Random Forest classifier on the collected data
- Real-time sign prediction using your webcam

## Setup

1. **Clone the repository** (if needed) and navigate to the project directory.
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Data Collection

Use `collect_images.py` to collect images for each sign:

- Press `0` for A
- Press `1` for B
- Press `2` for L
- Press `3` for D
- Press `4` for E
- Press `5` for F
- Press `6` for C
- Press `q` to quit

Images will be saved in the corresponding `data/<class_number>/` folders.

## Dataset Preparation

Run `create_ds.py` to process the collected images and extract hand landmarks:
```bash
python create_ds.py
```
This will create a `data.pickle` file with the features and labels.

## Model Training

Train the classifier using:
```bash
python train.py
```
This will create a `model.p` file with the trained model.

## Real-Time Testing

Run the sign language detector in real time:
```bash
python test.py
```
Show a hand sign to your webcam. The predicted letter will be displayed on the video feed.

## Notes
- Make sure your webcam is connected and accessible.
- Collect a sufficient number of images for each class for best results.
- The model uses only the first detected hand in the frame.

## Dependencies
- opencv-python
- mediapipe
- numpy
- scikit-learn

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## License
This project is for educational purposes. 