import io
import os
from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException, status
from PIL import Image
from model.model import load_model
from app.schemas import PredictionOutput  # Use the Output schema we fixed earlier

# 1. Load your model globally
# This ensures it's only loaded once when the server starts



app = FastAPI(title="Bangladeshi Taka Note Detection API")

@app.get("/")
def home():
    return {"message": "Bangladeshi Taka Note Detection API is Live"}

@app.post("/predict/", response_model=PredictionOutput)
async def predict(file: UploadFile = File(...)):
    loaded_model = load_model()
    # 2. Validate Input (File Extension)
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Invalid file type. Only JPEG and PNG are supported."
        )

    # 3. Handle the model not being loaded
    if loaded_model is None:
        return HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model is not initialized."
        )

    try:
        # 4. Read the uploaded file into PIL
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Ensure image is in RGB (YOLO prefers this over RGBA/Grayscale)
        if image.mode != "RGB":
            image = image.convert("RGB")

        # 5. Run prediction
        # Use stream=True for better memory management
        results = loaded_model.predict(source=image, conf=0.25)

        detected_classes = []
        confidence_scores = []
        coordinates = []

        # 6. Process results correctly
        # YOLO results is a list, usually with one element for one image
        for result in results:
            for box in result.boxes:
                # .item() or float() converts torch tensors to standard Python types
                cls_id = int(box.cls[0].item())
                detected_classes.append(result.names[cls_id])
                confidence_scores.append(float(box.conf[0].item()))
                coordinates.append(box.xyxy[0].tolist())

        return {
            "detected_classes": detected_classes,
            "confidence_scores": confidence_scores,
            "coordinates": coordinates
        }

    except Exception as e:
        # 7. Graceful error handling for corrupt images or internal crashes
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Prediction failed: {str(e)}"
        )