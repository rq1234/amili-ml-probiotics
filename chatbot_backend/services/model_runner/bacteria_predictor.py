import pandas as pd
import numpy as np
from pathlib import Path
from xgboost import XGBClassifier
import xgboost as xgb
import io
from fastapi import APIRouter, File

router = APIRouter()

# ─── PATHS ─────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODEL_PATH = BASE_DIR / "abund-16S-model.json"
TAXONOMY_FILE = DATA_DIR / "taxonomy_mapping.csv"

# ─── LOAD MODEL ────────────────────────────────────────
model = XGBClassifier()
model.load_model(MODEL_PATH)

# ─── OTU TO TAXONOMY MAPPING ──────────────────────────
OTU_TAXO_DICT = {}
if TAXONOMY_FILE.exists():
    taxonomy_df = pd.read_csv(TAXONOMY_FILE)
    OTU_TAXO_DICT = dict(zip(taxonomy_df["OTU"], taxonomy_df["taxonomy"]))

# ─── HELPER FUNCTIONS ─────────────────────────────────
def define_target(sample_id: str) -> int:
    return 1 if sample_id.startswith("A") else 0

def preprocess_16s_data(df: pd.DataFrame) -> pd.DataFrame:
    if 'OTU' in df.columns:
        df = df.set_index('OTU')
    if 'taxonomy' in df.columns:
        df = df.drop('taxonomy', axis=1)
    if df.shape[0] > df.shape[1]:
        df = df.transpose()
    df.insert(0, "AUTISM", [define_target(idx) for idx in df.index])
    return df

# ─── API ROUTE ────────────────────────────────────────
@router.post("/predict-bacteria")
def predict_bacteria(filename: str) -> dict:
    """
    Takes a filename (inside /data), returns a prediction dictionary with summary, top features, and results.
    """
    filepath = DATA_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    df = pd.read_csv(filepath)
    processed_df = preprocess_16s_data(df)
    X = processed_df.drop("AUTISM", axis=1) if "AUTISM" in processed_df else processed_df

    preds = model.predict(X)
    proba = model.predict_proba(X)

    booster = model.get_booster()
    dmatrix = xgb.DMatrix(X)
    shap_values = booster.predict(dmatrix, pred_contribs=True)
    shap_values = shap_values[:, :-1]  # Remove bias column
    mean_abs_shap = np.mean(np.abs(shap_values), axis=0)
    top_5_indices = np.argsort(mean_abs_shap)[::-1][:5]

    top_5_features = [
        {
            "otu": X.columns[i],
            "importance": float(mean_abs_shap[i]),
            "taxonomy": OTU_TAXO_DICT.get(X.columns[i], "Unknown")
        }
        for i in top_5_indices
    ]

    results = [
        {
            "sample_id": X.index[i],
            "autism_prediction": int(preds[i]),
            "autism_probability": float(proba[i][1])
        }
        for i in range(len(X))
    ]

    return {
        "summary": {
            "total_samples": len(preds),
            "autism_predicted": int(np.sum(preds)),
            "control_predicted": int(len(preds) - np.sum(preds))
        },
        "top_5_features": top_5_features,
        "results": results
    }



