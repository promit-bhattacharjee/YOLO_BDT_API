import os
from ultralytics import YOLO

# This gets 'D:\Code\YOLO_BDT_API\model' (where your script is)
def load_model():
        SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

        # Move UP one level to 'D:\Code\YOLO_BDT_API'
        ROOT_DIR = os.path.dirname(SCRIPT_DIR)

        # Now build the path correctly
        MODEL_PATH = os.path.join(ROOT_DIR, 'model', 'weights', 'best.pt')

        print(f"Corrected Path: {MODEL_PATH}")
        try:
            model = YOLO(MODEL_PATH)
            print("Model Loaded Successfully!")
            return model
        except Exception as e:
            print(f"Still failing: {e}")
            return None
        