import streamlit as st
from utils.data_loader import load_data
from utils.chart_builder import build_chart

st.title("Modular Streamlit App")

df = load_data()
st.write("Here is the data:", df)

chart = build_chart(df)
st.altair_chart(chart, use_container_width=True)