import torch
from ultralytics import YOLO


def main():
    # Set device to CPU explicitly
    device = torch.device("cpu")

    # Load a model
    # model = YOLO('yolov8.yaml', device=device)  # build a new model from YAML
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
    # model = YOLO('yolov8n.yaml', device=device).load('yolov8n.pt')  # build from YAML and transfer weights

    # Train the model
    results = model.train(
        data="D:/project_and_code/ultralytics-main/ultralytics/cfg/datasets/mycoco128.yaml",
        epochs=300,
        imgsz=(640, 384),
        device=device,
    )


if __name__ == "__main__":
    main()
# yolo detect train data=D:/project_and_code/ultralytics-main/ultralytics/cfg/datasets/mycoco128.yaml model=yolov8n.pt epochs=100 imgsz=640
# 0 device=CPU
