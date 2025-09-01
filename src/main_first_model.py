






from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(data="outputs\model_output\data.yaml", epochs=100, imgsz=640, batch=16)