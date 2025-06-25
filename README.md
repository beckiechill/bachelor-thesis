# AD_Detection_Bias

This repository contains the codebase for the Bachelor Thesis by Rebeca Sanz titled **“Assessing Bias in Machine Learning Models for Alzheimer’s Disease Detection Across Gender and Age.”**

## Project Goals
This thesis explores and evaluates fairness of machine learning models in detecting Alzheimer’s Disease from speech data. It focuses particularly on potential bias across gender and age groups. It also explores model explainability.

## Datasets
The datasets used are: 
- DementiaBank Pitt Corpus Dataset provided by the TalkBank project: https://talkbank.org/
- ADReSS Dataset from the ADReSS Challenge: https://dementia.talkbank.org/ADReSS-2020/

These datasets are not openly available and require permission from TalkBank to access them. 


## Repository Structure
```
├── ADReSS-IS2020-data
├── Pitt
├── README.md
├── data
│   ├── features
│   └── raw
│       ├── labels.tsv
│       ├── manual_age_fix_pitt_ad.tsv
│       └── manual_age_fix_pitt_control.tsv
├── environment.yml
├── notebooks
│   ├── RoBERTa_adress.ipynb
│   ├── RoBERTa_pitt.ipynb
│   ├── adress_rf.ipynb
│   ├── pitt_rf.ipynb
│   ├── report.ipynb
│   └── preprocessing.ipynb
├── output
│   ├── fairness
│   ├── models
│   ├── plots
│   ├── predictions
│   ├── roberta
│   │   ├── adress
│   │   └── pitt
│   └── shap
│       ├── shap_adress
│       └── shap_pitt
├── project_config.py
├── roberta_requirements.txt
└── rf_requirements.txt
```

## Additional Data Notes 
- The data file used in the ADReSS experiments, `data/raw/labels.tsv`, can also be downloaded directly from the ADReSS Challenge website. 
- The files `manual_age_fix_pitt_ad.tsv` and `manual_age_fix_pitt_control.tsv` were created to manually correct some age values in the Pitt dataset. They are based on the demographic spreadsheet containing all the participant data for the Pitt Corpus. These additions are optional, so the corresponding cells in the notebook can be skipped. 
- The project structure and code assume that the folders `ADReSS-IS2020-data/` and `Pitt/` are located in the **same directory as the project root**.
- These datasets should be downloaded and placed manually as described in the [Datasets](#datasets) section.




## Environment Setup

This project is designed to be run in 2 separate environments: one for the Random Forest model and one for the RoBERTa model, in order to avoid dependency conflicts. 

### 1. Random Forest Env

Used for:
- `preprocessing.ipynb`
- `adress_rf.ipynb`
- `pitt_rf.ipynb`
- `report_rf.ipynb`

### 2. RoBERTa Env

Used for:
- `RoBERTa_adress.ipynb`
- `RoBERTa_pitt.ipynb`

Create and activate:
```bash
conda create -n rf python=3.9
conda activate rf
pip install -r rf_requirements.txt
```

```conda env create -f environment.yml``` 

```conda activate <env_name>```  # change <env_name> with your chosen name


Or using pip:
```pip install -r requirements.txt``` # use the correct txt file, either rf_requirements or roberta_requirements

Use ```roberta_requirements.txt``` to set up the environment for the RoBERTa models. 

## Running the code

- `project_config.py` defines utility functions to dynamically resolve and manage file paths relative to the project root. 
- Start by running `preprocessing.ipynb`, which cleans the raw transcripts, extracts features, and prepares the data for the pipeline. 
- `report.ipynb` is used to create the table with the distribution of the dataset for the report of the thesis.
- Then run either model:
    - `adress_rf.ipynb` for the ADReSS dataset using Random Forest
    - `pitt_rf.ipynb` for the Pitt dataset using Random Forest
    - `RoBERTa_adress.ipynb` for the ADReSS dataset using RoBERTa
    - `RoBERTa_pitt.ipynb` for the Pitt dataset using RoBERTa

These notebooks train either a Random Forest model or a RoBERTa model, evaluate its performance, analyze model explainability, and assess fairness across gender and age groups, including mitigation strategies.