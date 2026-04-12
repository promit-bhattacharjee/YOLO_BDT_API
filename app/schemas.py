from pydantic import BaseModel
from typing import List, Any

class PredictionInput(BaseModel):
    # If passing raw bytes (common for FastAPI file uploads)
    image_bytes: bytes 
    # Alternatively, use 'str' if passing a file path
    # image_path: str 

class PredictionOutput(BaseModel):
    detected_classes: List[str]
    confidence_scores: List[float]
    # Coordinates are usually a list of lists (e.g., [[x1, y1, x2, y2], ...])
    coordinates: List[List[float]]