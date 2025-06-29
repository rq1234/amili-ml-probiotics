# 🧠 amili-ml-probiotics

Machine Learning Models used for formulating Probiotics.

This project contains a FastAPI + React-based chatbot system that:
- Predicts **autism-related gut microbiome composition** based on 16S rRNA OTU data
- Predicts **hospital readmission risks** based on patient health records
- Aims to recommend suitable probiotic strategies by combining these insights

---

## Features

- ✅ XGBoost model for autism-related gut bacteria prediction
- ✅ XGBoost model for hospital readmission risk classification
- ✅ FastAPI backend with structured API routes

---

##  Installation

### Clone the repository
```bash
git clone https://github.com/rq1234/amili-ml-probiotics.git
cd amili-ml-probiotics

```

## ⚙️ Set up the backend (FastAPI)
```bash
cd chatbot_backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

```
---

## 📁 Project Structure
```bash
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
```
## 📌 Possible Areas of Analysis

---

## 16S rRNA Gene Sequencing

- Targets the conserved 16S rRNA gene to identify bacterial taxa, typically at the genus level
- Produces Operational Taxonomic Unit (OTU) counts per sample
- Contains highly conserved and hypervariable regions, allowing classification of bacteria

**Advantages:**
- Cost-effective
- Useful for taxonomic profiling

---

## Shotgun Metagenomics

- Sequences all microbial DNA in a sample
- Provides functional and taxonomic information:
  - Identifies genes and metabolic pathways present
  - Enables strain-level resolution

**Advantages:**
- Captures functional potential (e.g., butyrate synthesis, antibiotic resistance genes)
- Enables reconstruction of metabolic interaction networks

**Example outputs:**
- Abundance tables for gene families and metabolic pathways

---

## Host Metadata and Clinical Labels

Includes variables such as:
- Disease status
- Age
- BMI
- Diet
- Medication use
- Immune status

Typically merged with microbiome data (e.g., taxonomic abundance, gene pathways) for **joint analysis**.
