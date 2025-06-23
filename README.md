# 🧠 amili-ml-probiotics

Machine Learning Models used for formulating Probiotics.

This project contains a FastAPI + React-based chatbot system that:
- Predicts **autism-related gut microbiome composition** based on 16S rRNA OTU data
- Predicts **hospital readmission risks** based on patient health records
- Aims to recommend suitable probiotic strategies by combining these insights

---

## 🚀 Features

- ✅ XGBoost model for autism-related gut bacteria prediction
- ✅ XGBoost model for hospital readmission risk classification
- ✅ FastAPI backend with structured API routes
- ✅ Docker + `docker-compose` support for deployment

---

## 📦 Installation

### Clone the repository
```bash
git clone https://github.com/rq1234/amili-ml-probiotics.git
cd amili-ml-probiotics

⚙️ Set up the backend (FastAPI)

cd chatbot_backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt


📁 Project Structure
AMILI-ML-PROBIOTICS/
├── chatbot_backend/                   # Backend logic
│   ├── main.py                        # FastAPI app setup
│   ├── router_bacteria.py             # API route for bacteria prediction
│   ├── router_hospital.py             # API route for readmission prediction
│   ├── requirements.txt               # Python dependencies
│   └── services/
│       └── model_runner/
│           ├── bacteria_predictor.py  # Autism ML model logic
│           ├── hospital_predictor.py  # Readmission ML model logic
│           ├── data/
│               ├── abund-16S-model.json     # Trained autism model
│               ├── xgb_model.json           # Trained hospital model
│               └── taxonomy_mapping.csv     # OTU to taxonomy map
│
├── working_drafts/                   # Notebooks & exploration
│   ├── Gut_Microbiome_ASD.ipynb       # Autism ML training and EDA
│   ├── Hospital.ipynb                 # Readmission ML training and EDA
│   └── datasets/
│       ├── 16S_RNA/                   # 16S OTU datasets
│       └── hospital_readmission/      # Hospital datasets
│
│
├── README.md                         # You're here!
