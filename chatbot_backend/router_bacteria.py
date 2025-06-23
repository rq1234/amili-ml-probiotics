from fastapi import APIRouter, UploadFile, File, HTTPException
from services.model_runner.bacteria_predictor import predict_bacteria, DATA_DIR
import uuid

router = APIRouter()

@router.post("/bacteria_predict")
async def predict(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")

    try:
        filename = f"input_bacteria_{uuid.uuid4().hex[:8]}.csv"
        file_path = DATA_DIR / filename

        with open(file_path, "wb") as f:
            f.write(await file.read())

        results = predict_bacteria(file_path)
        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Bacteria prediction failed: {str(e)}")
