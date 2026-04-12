from ultralytics import YOLO
import joblib


model = YOLO('./model/weights/best.pt')
joblib.dump(model, 'model.joblib')
