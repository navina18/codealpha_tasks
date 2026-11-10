
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load dataset
file_path = Path(__file__).resolve().parent / "StudentsPerformance.csv"
df = pd.read_csv(file_path)

print("STUDENT PERFORMANCE DATA ANALYSIS")
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

# Average marks
subjects = ["math score", "reading score", "writing score"]
print("\nAverage Subject Scores:")
print(df[subjects].mean())

# Performance by gender
print("\nAverage Scores by Gender:")
print(df.groupby("gender")[subjects].mean())

# Test preparation analysis
print("\nTest Preparation Analysis:")
print(df.groupby("test preparation course")[subjects].mean())

# Correlation
print("\nSubject Correlation:")
print(df[subjects].corr())

# Save analysis results
output = Path(__file__).resolve().parent / "analysis_results"
output.mkdir(exist_ok=True)

df.describe().to_csv(output / "summary.csv")
df.groupby("gender")[subjects].mean().to_csv(
    output / "gender_analysis.csv"
)
df.groupby("test preparation course")[subjects].mean().to_csv(
    output / "preparation_analysis.csv"
)

print("\nEDA Analysis Completed Successfully!")
print("Results saved in analysis_results folder.")
