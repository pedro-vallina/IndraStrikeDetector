# Aircraft Damage Detection (Computer Vision)

Computer vision system designed to analyze aircraft images and detect potential structural damage.

The project leverages a pre-trained YOLOv26n model for real-time object detection. Model weights are included in the repository for immediate use.

## Pipeline:
1. Apply a mask to the image so that only the plane stays (YOLO-seg pre-trained model).
2. Run the YOLO model through the hole image.
3. In case it fails, apply SAHI (run the model through smaller windows iteratively)
4. Show and save results.

## Tech Stack
- Python
- YOLOv26n
- SAHI
- OpenCV
