import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="E-commerce Analytics & Experimentation", layout="wide")
st.title("📦 E-commerce Analytics & Experimentation")

data_dir = Path(__file__).resolve().parents[1] / "data"
tx_path = data_dir / "transactions.csv"

if tx_path.exists():
    df = pd.read_csv(tx_path)
    st.metric("Total Revenue", f"${df['line_revenue'].sum():,.2f}" if "line_revenue" in df else "N/A")
    if "category" in df and "line_revenue" in df:
        by_cat = df.groupby("category")["line_revenue"].sum().sort_values(ascending=False)
        st.bar_chart(by_cat)
    st.caption("Tip: Populate data by running the notebooks first.")
else:
    st.warning("No transactions found. Run the notebooks to generate curated data.")
