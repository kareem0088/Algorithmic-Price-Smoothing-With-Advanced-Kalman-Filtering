# Algorithmic-Price-Smoothing-With-Advanced-Kalman-Filtering

## Steps

1. Understanding the Business and the Problem:
 I always wonder if we can treat price like a radar, monitoring its movement, filtering it, and removing any noise to discover the true price direction at the moment. However, the problem lies in data processing, but the solution is simple. The problem is that if we want to deal with tick data, we will need massive storage and computing power, along with more microstructure noise in tick data, and the high cost of accessing it. Let's solve all these problems by using 1-minute or 5-minute data, which is perfectly adequate. It's also a strong challenge to extract and understand price movements, but with free data, unlike book level 1 or 2, or other data with strong information.

The goal is to classify signals as good, medium, or bad.

The goal is to filter out the bad signals as much as possible from the rest.

2. Data Acquisition and Ingestion

3. Exploratory Data Analysis (EDA)
   - EDA Report
   - Correlation Report

4. Data Preprocessing and Feature Engineering
   - Validation Report

5. Model Building and Training

6. Evaluation
   - Model Evaluation Report

7. Explainability Model
   - Explainability and Robustness Report

---

# Reports

1. EDA Report

2. Correlation Report

3. Validation Report

4. Model Evaluation Report

5. Explainability and Robustness Report

---
# Project Structure

```text
Algorithmic-Price-Smoothing-With-Advanced-Kalman-Filtering/
│
├── data/
│   └── XAUUSD_1m.csv
│
├── notebooks/
│   ├── 01_eda_and_correlation.ipynb
│   └── 02_model_exploration.ipynb
│
├── mlflow_runs/                          # experiment tracking
│
├── src/
│   ├── __init__.py
│   ├── data_ingestion.py                 # step 2 code
│   ├── eda_analysis.py                   # step 3 code - (MLflow)
│   ├── kalman_filter.py                  # step 4 code
│   ├── feature_engineering.py            # step 4 code
│   ├── radar_model.py                    # step 5 code
│   └── evaluation.py                     # step 6 and 7 code - (MLflow)
│
├── reports/                              
│   ├── 1_eda_report.md
│   ├── 2_correlation_report.md
│   ├── 3_validation_report.md
│   ├── 4_model_evaluation_report.md
│   └── 5_explainability_robustness_report.md
│
├── main.py                               # mlflow.start_run()
├── Docker-file                           # Containerization
└── requirements.txt
```
