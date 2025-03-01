import os
import pandas as pd
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))
file_names = ["savedrecs.csv", "savedrecs_2.csv", "savedrecs_3.csv", "savedrecs_4.csv", "savedrecs_5.csv", "LRDetection.csv"]
files = [os.path.join(script_dir, f) for f in file_names]

dfs = []
for file in files:
    if os.path.exists(file):
        df = pd.read_csv(file, dtype=str)  
        dfs.append(df)
    else:
        print(f"File not found: {file}")
        exit()

#check if all datasets have the same column names and if not standarized them 
column_sets = [set(df.columns) for df in dfs]

if not all(cols == column_sets[0] for cols in column_sets):
    #standardize columns using the first file as reference
    standard_cols = dfs[0].columns
    dfs = [df.reindex(columns=standard_cols) for df in dfs]

merged_df = pd.concat(dfs, ignore_index=True)

#remove duplicate entries based on Title
merged_df.drop_duplicates(subset="Title", keep="first", inplace=True)

#replace missing values with "Unknown"
merged_df.fillna("Unknown", inplace=True)

#get missing DOI using CrossRef API
def get_doi(title):
    url = f"https://api.crossref.org/works?query.title={title}"
    response = requests.get(url).json()
    try:
        message = response.get('message')
        if not isinstance(message, dict):
            return "Unknown"
        items = message.get('items', [])
        if not items:
            return "Unknown"
        return items[0].get('DOI', "Unknown")
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error fetching DOI for {title}: {e}")
        return "Unknown"

#update missing DOIs (only if DOI column exists)
if "DOI" in merged_df.columns:
    merged_df["DOI"] = merged_df.apply(
        lambda row: get_doi(row["Title"]) if row["DOI"] == "Unknown" else row["DOI"],
        axis=1
    )

#save cleaned dataset
output_path = os.path.join(script_dir, "merged_cleaned_data.csv")
merged_df.to_csv(output_path, index=False, encoding="utf-8")
