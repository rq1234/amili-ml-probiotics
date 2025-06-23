from fastapi import APIRouter, UploadFile, File, HTTPException
from services.model_runner.hospital_predictor import predict_readmission, DATA_DIR
import uuid

router = APIRouter()

@router.post("/hospital_predict")
async def predict(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")

    try:
        
        filename = f"input_{uuid.uuid4().hex[:8]}.csv"
        file_path = DATA_DIR / filename

        
        with open(file_path, "wb") as f:
            f.write(await file.read())

        
        csv_with_preds = predict_readmission(filename)

        return {
            "filename": f"predictions_{file.filename}",
            "content": csv_with_preds
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
