# 📦 E-commerce Analytics & Experimentation

## 📖 Overview
This project simulates the role of a **data scientist at an e-commerce company**. The goal is to analyze customer behavior, design and evaluate an **A/B experiment**, and build predictive **machine learning models** to forecast customer purchasing propensity.

It covers the **entire data science workflow**:
- API → Data Collection
- Cleaning & Feature Engineering
- Hypothesis Testing
- A/B Testing (Simulated)
- Machine Learning
- Visualization & Dashboarding

## 🎯 Learning Objectives
- Practice **API data acquisition** using Python (`requests`).
- Apply **data cleaning and feature engineering** (RFM, AOV, category features).
- Design hypotheses and evaluate them with **statistical tests**.
- Simulate and analyze an **A/B experiment** (frequentist + bootstrap; optional Bayesian).
- Build ML models (Logistic Regression, Gradient Boosting) to predict **purchase propensity**.
- Communicate results through **visualizations** and an optional **Streamlit dashboard**.

## 📊 Dataset
We use the **Fake Store API**: https://fakestoreapi.com/  
It provides synthetic but realistic e-commerce data:
- **Products**: catalog, categories, prices
- **Users**: demographics, locations
- **Carts**: purchase transactions with products, quantities, and dates

## 🛠️ Project Structure
```
ecommerce-analytics-abtest/
├── data/                     # Saved raw and cleaned data (CSV files)
│   ├── products.csv
│   ├── users.csv
│   ├── transactions.csv
│   └── user_rfm.csv
├── notebooks/
│   ├── 01_data_pull.ipynb         # API fetch, raw → curated tables
│   ├── 02_clean_features.ipynb    # Cleaning, feature engineering
│   ├── 03_ab_test.ipynb           # Hypothesis tests, A/B testing
│   └── 04_ml_propensity.ipynb     # ML model training & evaluation
├── dashboard/
│   └── app.py                      # Optional Streamlit dashboard
├── report/
│   └── final_report.md             # Project summary & insights
├── requirements.txt                # Python dependencies
└── README.md                       # Project description
```

## 🚀 Quickstart
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ Run the Notebooks
Open the `notebooks/` in Jupyter and execute in order:
1) `01_data_pull.ipynb`
2) `02_clean_features.ipynb`
3) `03_ab_test.ipynb`
4) `04_ml_propensity.ipynb`

## 🖥️ Dashboard (optional)
```bash
cd dashboard
streamlit run app.py
```

## 📌 Deliverables
- Clean, reproducible notebooks
- A/B testing analysis with statistical rigor
- Predictive ML models with performance metrics
- Final report with actionable insights
- Optional interactive dashboard
