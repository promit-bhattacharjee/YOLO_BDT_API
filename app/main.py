from fastapi import FastAPI
from joblib import load
from ultralytics import YOLO

model = joblib.load("model.yolo26m.pt")
model.train(data="data.yaml", epochs=100, imgsz=640, batch=8, device=0)

api=FastAPI()
@api.get("/")
def home():
    return {"message":"Hello World"}