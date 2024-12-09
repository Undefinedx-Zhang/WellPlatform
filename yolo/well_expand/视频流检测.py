# from ultralytics import YOLO
#
# # Load a pretrained YOLOv8n model
# model = YOLO('../runs/detect/train1/weights/best.pt')
#
# # Define path to video file
# source = r"C:\Users\zdj2003\Desktop\WeChat_20240515193007.mp4"
#
# # Run inference on the source
# results = model(source, stream=True)  # generator of Results objects


from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO(r"../runs/detect//train8/weights/best.pt")

# Run inference on 'bus.jpg' with arguments
model.predict(r"../image/人拍.mp4", save=True, imgsz=640, conf=0.5)