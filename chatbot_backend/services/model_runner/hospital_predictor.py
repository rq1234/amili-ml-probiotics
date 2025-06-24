import pandas as pd
import os
import io
from pathlib import Path
from xgboost import XGBClassifier



# ─── PATHS ─────────────────────────────────────────────
DATA_DIR = Path(__file__).resolve().parent / "data"
MODEL_PATH = Path(__file__).resolve().parent / "xgb_model.json"

# ─── LOAD MODEL ────────────────────────────────────────
model = XGBClassifier()
try:
    print(f" Loading model from: {MODEL_PATH}")
    model.load_model(MODEL_PATH)
    print(" Model loaded successfully")
except Exception as e:
    print(f" Failed to load model: {e}")
    raise


# ─── FEATURES USED IN TRAINING ─────────────────────────
FEATURES = [
    'race', 'gender', 'age', 'admission_type_id', 'discharge_disposition_id',
    'admission_source_id', 'time_in_hospital', 'num_lab_procedures',
    'num_procedures', 'num_medications', 'number_outpatient', 'number_emergency',
    'number_inpatient', 'number_diagnoses', 'max_glu_serum', 'A1Cresult',
    'metformin', 'insulin', 'change', 'diabetesMed'
]

# ─── ENCODING CATEGORICAL FEATURES ─────────────────────
def simple_label_encode(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include='object').columns:
        df[col] = pd.factorize(df[col])[0]
    return df


# ─── PREDICTION FUNCTION ───────────────────────────────
def predict_readmission(filename: str) -> dict:
    filepath = DATA_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    df = pd.read_csv(filepath)
    df_encoded = simple_label_encode(df.copy())
    preds = model.predict(df_encoded[FEATURES])

    label_map = {0: "<30", 1: ">30", 2: "NO"}
    mapped_preds = [label_map[p] for p in preds]

    df["readmission_prediction"] = mapped_preds

    summary = {
        "total_samples": len(preds),
        "predicted_<30": mapped_preds.count("<30"),
        "predicted_>30": mapped_preds.count(">30"),
        "predicted_NO": mapped_preds.count("NO")
    }

    results = [
        {
            "patient_id": int(i),
            "readmission_prediction": mapped_preds[i]
        }
        for i in range(len(df))
    ]

    return {
        "summary": summary,
        "results": results
    }