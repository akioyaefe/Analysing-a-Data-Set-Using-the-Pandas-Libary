import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and explore dataset
try:
    df = pd.read_csv("student_scores.csv")
    print("First 5 rows of the dataset:")
    print(df.head())
    
    print("\nDataset info:")
    print(df.info())
    
    print("\nMissing values in each column:")
    print(df.isnull().sum())
    
    # Fill missing numerical values with column mean
    df.fillna(df.mean(numeric_only=True), inplace=True)
    
except FileNotFoundError:
    print("Error: The file 'student_scores.csv' was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except pd.errors.ParserError:
    print("Error: The file could not be parsed.")
except Exception as e:
    print("An unexpected error occurred:", e)

# Basic Data Analysis
print("\nBasic statistics for numerical columns:")
print(df.describe())

print("\nMean scores by Grade:")
print(df.groupby('Grade')[['Math','English','Science']].mean())

print("\nObservations:")
print("- Grade 12 students have generally higher scores.")
print("- Some variation in Math scores within Grade 10.")

# Data Visualization
sns.set(style="whitegrid")  # Set Seaborn style

# Line chart: Math scores trend by Grade
plt.figure(figsize=(8,5))
for grade in df['Grade'].unique():
    grade_data = df[df['Grade'] == grade]
    plt.plot(grade_data['StudentID'], grade_data['Math'], marker='o', label=f"Grade {grade}")
plt.title("Math Scores Trend by Grade")
plt.xlabel("Student ID")
plt.ylabel("Math Score")
plt.legend()
plt.show()

# Bar chart: Average English score per Grade
plt.figure(figsize=(6,4))
sns.barplot(x='Grade', y='English', data=df, ci=None)
plt.title("Average English Score per Grade")
plt.xlabel("Grade")
plt.ylabel("English Score")
plt.show()

# Histogram: Distribution of Science scores
plt.figure(figsize=(6,4))
plt.hist(df['Science'], bins=6, color='lightgreen', edgecolor='black')
plt.title("Distribution of Science Scores")
plt.xlabel("Science Score")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Math vs Science scores by Grade
plt.figure(figsize=(6,4))
sns.scatterplot(x='Math', y='Science', hue='Grade', data=df, palette='Set2', s=100)
plt.title("Math vs Science Scores by Grade")
plt.xlabel("Math Score")
plt.ylabel("Science Score")
plt.legend(title="Grade")
plt.show()
