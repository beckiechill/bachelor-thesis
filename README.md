# AD_Detection_Bias

This repository contains the codebase for the Bachelor Thesis by Rebeca Sanz titled **“Assessing Bias in Machine Learning Models for Alzheimer’s Disease Detection Across Gender and Age.”**

## Datasets
The datasets used are: 
- DementiaBank Pitt Corpus Dataset provided by the TalkBank project: https://talkbank.org/
- ADReSS Dataset from the ADReSS Challenge: https://dementia.talkbank.org/ADReSS-2020/

These datasets are not openly available and require permission from TalkBank to access them. 


## Repository Structure
```
├── ADReSS-IS2020-data
├── data
│   ├── features
│   └── raw
│       ├── labels.tsv
│       ├── manual_age_fix_pitt_ad.tsv
│       └── manual_age_fix_pitt_control.tsv
├── environment.yml
├── notebooks
│   ├── adress_rf.ipynb
│   ├── pitt_rf.ipynb
│   └── preprocessing.ipynb
├── output
│   ├── fairness
│   ├── models
│   ├── plots
│   ├── predictions
│   └── shap
│       ├── shap_adress
│       └── shap_pitt
├── Pitt
├── project_config.py
├── README.md
└── requirements.txt
```

## Additional Data Notes 
- The data file used in the ADReSS experiments, `data/raw/labels.tsv`, can also be downloaded directly from the ADReSS Challenge website. 
- The files `manual_age_fix_pitt_ad.tsv` and `manual_age_fix_pitt_control.tsv` were created to manually correct some age values in the Pitt dataset. They are based on the demographic spreadsheet containing all the participant data for the Pitt Corpus. These additions are optional, so the corresponding cells in the notebook can be skipped. 
- The project structure and code assume that the folders `ADReSS-IS2020-data/` and `Pitt/` are located in the **same directory as the project root**.
- These datasets should be downloaded and placed manually as described in the [Datasets](#datasets) section.




## Create Environment 

To set up the environment, if you are using conda you can run the following in the terminal: 

```conda env create -f environment.yml``` 

```conda activate <env_name>```  # change <env_name> with your chosen name


Or using pip:
```pip install -r requirements.txt``` 

Start by running preprocessing.ipynb, which cleans the raw transcripts, extracts features, and prepares the data for the pipeline.
## Running the code
- `project_config.py` defines utility functions to dynamically resolve and manage file paths relative to the project root. 
- Start by running `preprocessing.ipynb`, which cleans the raw transcripts, extracts features, and prepares the data for the pipeline. 
- Then run either:
    - `adress_rf.ipynb` for the ADReSS dataset, or
    - `pitt_rf.ipynb` for the Pitt dataset. 

These notebooks train a Random Forest model, evaluate its performance, analyse model explainability, and assess fairness across gender and age groups, including mitigation strategies. 

## Project Goals
This thesis explores and evaluates fairness of machine learning models in detecting Alzheimer’s Disease from speech data. It focus particularly on potential bias across gender and age groups. It also explores model explainability. 