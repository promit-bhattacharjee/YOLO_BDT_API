from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
import io
from PIL import Image

# 1. Load your model
# Ensure the file 'model.weights.best.pt' is in your project folder


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bangladeshi Taka Note Detection API is Live"}
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # 2. Read the uploaded file
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    # 3. Run prediction
    results = model(image)

    # 4. Process results
    detected_classes = []
    confidence_scores = []
    coordinates = []

    for result in results:
        for box in result.boxes:
            detected_classes.append(result.names[int(box.cls[0])])  # Get class name
            confidence_scores.append(float(box.conf[0]))  # Get confidence score
            coordinates.append(box.xyxy[0].tolist())  # Get bounding box coordinates

    return {
        "detected_classes": detected_classes,
        "confidence_scores": confidence_scores,
        "coordinates": coordinates
    }