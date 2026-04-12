# Aircraft Damage Detection (Computer Vision)

Computer vision system designed to analyze aircraft images and detect potential structural damage.

The project leverages a pre-trained YOLOv26n model for real-time object detection. Model weights are included in the repository for immediate use.

To improve detection performance on large or complex images, the system integrates SAHI (Slicing Aided Hyper Inference). When no damage is initially detected, SAHI is applied to perform inference on image slices, increasing the likelihood of identifying smaller or subtle defects.

## Tech Stack
- Python
- YOLOv26n
- SAHI
- OpenCV
