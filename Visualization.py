
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load dataset
base = Path(__file__).resolve().parent
df = pd.read_csv(base / "StudentsPerformance.csv")

# Create charts folder
output = Path(__file__).resolve().parent / "charts"
output.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")

subjects = ["math score", "reading score", "writing score"]

# Chart 1: Average Subject Scores
plt.figure(figsize=(8, 5))
df[subjects].mean().plot(kind="bar")
plt.title("Average Scores by Subject")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output / "average_scores.png")
plt.close()

# Chart 2: Gender Performance
plt.figure(figsize=(8, 5))
df.groupby("gender")[subjects].mean().plot(kind="bar")
plt.title("Student Performance by Gender")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output / "gender_performance.png")
plt.close()

# Chart 3: Test Preparation
plt.figure(figsize=(8, 5))
df.groupby("test preparation course")[subjects].mean().plot(kind="bar")
plt.title("Test Preparation vs Performance")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output / "test_preparation.png")
plt.close()

# Chart 4: Subject Correlation
plt.figure(figsize=(7, 5))
sns.heatmap(df[subjects].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Between Subjects")
plt.tight_layout()
plt.savefig(output / "subject_correlation.png")
plt.close()

print("DATA VISUALIZATION COMPLETED!")
print("4 charts saved successfully in charts folder.")
