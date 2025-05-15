This repository contains the codebase for the Bachelor Thesis by Rebeca Sanz titled **“Assessing Bias in Machine Learning Models for Alzheimer’s Disease Detection Across Gender and Age.”**

## Datasets
The datasets used are: 
- DementiaBank Pitt Corpus Dataset provided by the TalkBank project: https://talkbank.org/
- ADReSS Dataset from the ADReSS Challenge: https://dementia.talkbank.org/ADReSS-2020/

These datasets are not openly available and require permission from TalkBank to access them. 


## Repository Structure 

ADReSS-IS2020-data/ # Data from ADReSS dataset
├── data/
│ ├── features/ # Extracted features from raw data
│ └── raw/ # Manual age fix files (Pitt) + labels (ADReSS)
├── notebooks/ # Jupyter notebooks for the experiments
├── output/
│ ├── fairness/ # Fairness analysis results
│ ├── models/ # Saved models
│ ├── plots/ # Tree visualizations and graphs
│ ├── predictions/ # Model predictions
│ └── shap/ # SHAP plots for model explainability
├── Pitt/ # Data from the Pitt dataset
├── environment.yml # Conda environment specification
├── project_config.py # Utility functions manage file paths relative to project root
├── README.md
└── requirements.txt # Python dependencies

## Additional Data Notes 
- The data file used in the ADReSS experiments, data/raw/labels.tsv, can also be downloaded directly from the ADReSS Challenge website. 
- The files manual_age_fix_pitt_ad.tsv and manual_age_fix_pitt_control.tsv were created to manually correct some age values in the Pitt dataset. They are based on the demographic spreadsheet containing all the participant data for the Pitt Corpus. These additions are optional, so the corresponding cells in the notebook can be skipped. 


## Create Environment 

To set up the environment, if you are using conda you can run the following in the terminal: 

conda env create -f environment.yml
conda activate <env_name>  # change <env_name> with your chosen name

Or using pip:
pip install -r requirements.txt 

Start by running preprocessing.ipynb, which cleans the raw transcripts, extracts features, and prepares the data for the pipeline.
## Running the code
- project_config.py defines utility functions to dynamically resolve and manage file paths relative to the project root. 
- Start by running preprocessing.ipyn, which cleans the raw transcripts, extracts features, and prepares the data for the pipeline. 
- Then run either:
    - adress_rf.ipynb for the ADReSS dataset, or
    - pitt_rf.ipynb for the Pitt dataset. 

These notebooks train a Random Forest model, evaluate its performance, analyse model explainability, and assess fairness across gender and age groups, including mitigation strategies. 

## Project Goals
This thesis explores and evaluates fairness of machine learning models in detecting Alzheimer’s Disease from speech data. It focus particularly on potential bias across gender and age groups. It also explores model explainability. 
