from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(
    data="YOLOv8-taco.v4-best-recommended-yolov8-taco.yolov8/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    device=0
)