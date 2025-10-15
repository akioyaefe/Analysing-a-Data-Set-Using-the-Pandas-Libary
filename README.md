# # PLP Assignment – Student Performance Data Analysis

This repository contains a Python program analyzing **student performance** using a CSV dataset.  
The assignment demonstrates **data loading, cleaning, basic analysis, and visualization** in a school context.

---

## Dataset

**File:** `student_scores.csv`  

**Columns:**

| Column      | Description                         |
|------------|-------------------------------------|
| StudentID  | Unique ID for each student           |
| Name       | Student name                         |
| Grade      | Grade level (10, 11, 12, etc.)      |
| Math       | Math score                           |
| English    | English score                        |
| Science    | Science score                        |

---

## Tasks Completed

### Task 1: Load and Explore Dataset
- Loaded dataset using **pandas**.
- Displayed first few rows using `.head()`.
- Checked dataset structure and data types using `.info()`.
- Identified missing values using `.isnull().sum()`.
- Cleaned missing data by filling numerical columns with column mean.

### Task 2: Basic Data Analysis
- Computed basic statistics (`mean`, `median`, `std`) using `.describe()`.
- Grouped data by `Grade` and computed mean scores for Math, English, and Science.
- Identified patterns:
  - Grade 12 students generally have higher scores.
  - Some variation in Math scores within Grade 10.

### Task 3: Data Visualization
- **Line Chart:** Math score trends across StudentID by Grade.  
- **Bar Chart:** Average English score per Grade.  
- **Histogram:** Distribution of Science scores.  
- **Scatter Plot:** Math vs Science scores colored by Grade.  

All plots include **titles, axis labels, and legends** for clarity.  

---

## How to Run

1. Ensure you have Python 3 installed.
2. Install required libraries if not already installed:

```bash
pip install pandas matplotlib seaborn-a-Data-Set-Using-the-Pandas-Libary
Python programs analyzing student performance using a CSV dataset, demonstrating data loading, cleaning, basic analysis, and visualizations with Pandas, Matplotlib, and Seaborn.
