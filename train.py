from roboflow import Roboflow
import torch
from ultralytics import YOLO

rf = Roboflow(api_key="xMvbcbJrmCTycKpyRL5l")
project = rf.workspace("maradys-project-7hybh").project("aircraft-surface-defect-detection-hw3mw")
version = project.version(3)
dataset = version.download("yolov11")

model = YOLO('yolo26n.pt')

model.train(data='/content/Aircraft-Surface-Defect-Detection-3/data.yaml',
            epochs=200,
            imgsz=640,
            patience=10,
            batch=128,
            workers=8)