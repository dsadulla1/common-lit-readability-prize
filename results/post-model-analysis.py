import pandas as pd
import numpy as np
import os

list_of_files = os.listdir('./results/results/')
list_of_files = ['./results/results/'+f for f in list_of_files]

def read_(file_):
    df = pd.read_csv(file_)
    filename = file_.split('/')[-1]
    strategy, dataset, *_ = filename.split("-")
    return df, strategy, dataset

list_of_files = [read_(f) for f in list_of_files if f.endswith('.csv') and f != './results/results/submission.csv']

def analyze_(df):
    print("\t Correlation:")
    print(df.corr())
    print("\t Describe:")
    print(df.describe())

pd.DataFrame.describe
for df, strategy, dataset in list_of_files:
    print(f"====== {strategy} - {dataset} =======")
    analyze_(df)
    print("===============")