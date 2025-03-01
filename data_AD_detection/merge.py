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


#check if all datasets have the same column names
column_sets = [set(df.columns) for df in dfs]

if all(cols == column_sets[0] for cols in column_sets):
    
    merged_df = pd.concat(dfs, ignore_index=True)

    #remove duplicate entries based on Title
    merged_df.drop_duplicates(subset="Title", keep="first", inplace=True)

    #then replace missing values with "Unknown"
    merged_df.fillna("Unknown", inplace=True)

    #get missing DOI from CrossRef API
    def get_doi(title):
        url = f"https://api.crossref.org/works?query.title={title}"
        response = requests.get(url).json()
        try:
            return response['message']['items'][0]['DOI']
        except (KeyError, IndexError):
            return "Unknown"

    #update missing DOIs
    if "DOI" in merged_df.columns:
        merged_df["DOI"] = merged_df.apply(lambda row: get_doi(row["Title"]) if row["DOI"] == "Unknown" else row["DOI"], axis=1)

    #save cleaned dataset
    output_path = os.path.join(script_dir, "merged_cleaned_data.csv")
    merged_df.to_csv(output_path, index=False, encoding="utf-8")

else:
    exit("Column names are not equal across datasets. Merging aborted.")