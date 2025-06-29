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

cd chatbot_backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

---

## 📁 Project Structure
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

## 📓 Notebooks Overview
Gut_Microbiome_ASD.ipynb
This notebook analyzes gut microbiome composition from 16S rRNA OTU data to infer Autism Spectrum Disorder (ASD) using machine learning.

Based on the study: Altered gut microbial profile is associated with abnormal metabolism activity of Autism Spectrum Disorder

Applies preprocessing, label encoding, and XGBoost classification

Includes SHAP for interpretability to identify top microbial predictors

Uses abund-16S-model.json as the trained model

Hospital.ipynb
This notebook processes structured hospital data to predict 30-day readmission risk using features such as diagnosis codes, age, and discharge type.

Includes steps for data cleaning, encoding, and feature engineering

Trains an XGBoost model for multiclass classification (<30, >30, or NO readmission)

Final model is saved as xgb_model.json

Metagenomics Disease.ipynb
A recent study from the Segata Lab analyzes human microbiome data obtained using shotgun metagenomic analysis.
The goal of the above mentioned study was to correctly predict whether a patient had a given disease or was healthy from the species abundance data for the patient's microbiome sample, after training on healthy samples and samples from patients with the given disease.

The dataset used in the study is available freely at MetAML - Metagenomic prediction Analysis based on Machine Learning and on kaggle.


## Possible areas of analysis
1. 16S rRNA Gene Sequencing
Targets the conserved 16S rRNA gene to identify bacterial taxa, typically at the genus level.

Produces Operational Taxonomic Unit (OTU) counts of bacterial taxa per sample.

Contains highly conserved and hypervariable regions, allowing classification of bacteria.

Advantages:

Cost-effective.

Useful for taxonomic profiling.

2. Shotgun Metagenomics
Sequences all microbial DNA in a sample.

Provides functional and taxonomic information:

Identifies genes and metabolic pathways present.

Enables strain-level resolution.

Advantages:

Captures functional potential (e.g., butyrate synthesis, antibiotic resistance genes).

Enables reconstruction of metabolic interaction networks.

Example outputs:

Abundance tables for gene families and metabolic pathways.

3. Host Metadata and Clinical Labels
Includes variables such as:

Disease status

Age

BMI

Diet

Medication use

Immune status

Typically merged with microbiome data (e.g., taxonomic abundance, gene pathways) for joint analysis.
