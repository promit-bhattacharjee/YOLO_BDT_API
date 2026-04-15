# Bangladeshi Taka (BDT) Note Detection API

A professional FastAPI-based service for detecting and classifying Bangladeshi Taka notes using the YOLO object detection model.

## 📌 Project Overview
This project provides a REST API that accepts an image of Bangladeshi currency and returns the detected denominations along with confidence scores and bounding box coordinates. It leverages **FastAPI** for high-performance web serving and **Ultralytics YOLO** for state-of-the-art computer vision.

### Key Features:
- **Fast Detection:** Real-time note detection.
- **Dockerized:** Easy deployment using Docker and Docker Compose.
- **Robust API:** Validates file types and handles image processing automatically.

---

## 📁 Folder Structure Map
```text
YOLO_BDT_API/
├── app/
│   ├── main.py             # Main FastAPI application and API routes
│   └── schemas.py          # Pydantic schemas for data validation
├── model/
│   ├── model.py            # Utility to load and initialize the YOLO model
│   └── weights/
│       └── best.pt         # Trained YOLO model weights
├── test/                   # Folder containing test images and labels
├── Dockerfile              # Docker configuration for building the image
├── docker-compose.yml      # Orchestration for the containerized service
├── requirements.txt        # List of Python dependencies
├── BDT_YOLO_API.pdf        # Documentation for assignment requirements (PDF)
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Step-by-Step Build and Run
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd YOLO_BDT_API
   ```

2. **Build and start the container:**
   ```bash
   docker-compose up --build
   ```
   *The API will be available at `http://localhost:8080`.*

3. **Verify the service:**
   Visit `http://localhost:8080/` in your browser. You should see:
   ```json
   { "message": "Bangladeshi Taka Note Detection API is Live" }
   ```

---

## 🛠 API Usage

### Example Request (curl)
To predict a note from an image file, use the following `curl` command:

```bash
curl -X 'POST' \
  'http://localhost:8080/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/path/to/your/note_image.jpg'
```

### Response Format
```json
{
  "detected_classes": ["100", "500"],
  "confidence_scores": [0.95, 0.88],
  "coordinates": [
    [x1, y1, x2, y2],
    [x1, y1, x2, y2]
  ]
}
```

---

## 📚 API Documentation
Once the server is running, you can access the interactive API documentation at:
- **Swagger UI:** `http://localhost:8080/docs`
- **ReDoc:** `http://localhost:8080/redoc`

---

## 📄 Project Report (Google Doc)
This project includes a detailed report accessible via Google Docs, serving as evidence of work and in-depth analysis.

**[Access the Project Report Here](https://docs.google.com/document/d/1AmAVsAppivjSxpq5VefHz5Ghe18od0JWj5VEHYwCQL4/edit?usp=sharing)**

The report contains the following sections:

### 1. Model Inference Documentation
- **Inference Script:** A Python script for performing model inference and object detection.
- **Detection Example:** Visual evidence (e.g., screenshots) showcasing successful detection of Bangladeshi Taka notes, highlighting the model's capabilities.

### 2. API Endpoint Validation
- **Response Validation:** JSON responses from the `/predict` endpoint, tested with five distinct images, demonstrating the API's functionality and response structure.
- **Testing Tools:** Screenshots from Postman or terminal commands (e.g., `curl`) validating the API responses.

### 3. Docker Deployment Verification
- **Build and Run Logs:** Terminal outputs confirming successful execution of `docker build` and `docker run` commands.
- **Service Verification:** Logs indicating the operational status of the API (e.g., "Uvicorn running on...").

### 4. Model Performance Analysis
- **Performance Summary:** A brief analysis of the model's accuracy, highlighting strengths (e.g., high precision on specific denominations) and limitations (e.g., challenges with folded or obscured notes).

### 5. Cloud Deployment
- **Application URL:** The publicly accessible URL of the deployed application (e.g., hosted on Render or similar platforms).
- **Operational Evidence:** Screenshots demonstrating the application's successful operation and accessibility in the cloud.

---

## 6. Public API URL
The application is live and accessible via the following endpoint. The Swagger UI has been enabled to allow for interactive testing of the model.

- **Base URL:** `https://yolo-bdt-api.onrender.com`
- **Interactive Documentation (Swagger):** `https://yolo-bdt-api.onrender.com/docs`
- **Prediction Endpoint:** `POST /predict/`
