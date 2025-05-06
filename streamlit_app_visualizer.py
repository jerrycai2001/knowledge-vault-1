# %%
import streamlit as st
import pandas as pd
import altair as alt

# %%
st.title("Computational Intensity Analysis Across Scientific Domains")

st.markdown("""
Upload a dataset of parsed research papers/reports with the following recommended columns:
- `domain` (e.g. 'protein modeling', 'neural signal processing')
- `algorithm` (e.g. 'AlphaFold', 'RNN', 'PPO')
- `compute_hours` (float)
- `memory_GB` (float)
- `accuracy` or `performance_score` (float, normalized 0-1)
""")

uploaded_file = st.file_uploader("Upload CSV or JSON data", type=["csv", "json"])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_json(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    st.subheader("Aggregate Metrics per Domain")
    agg = df.groupby("domain").agg({
        "compute_hours": "mean",
        "memory_GB": "mean",
        "performance_score": "mean"
    }).reset_index()
    st.dataframe(agg)

    st.subheader("Compute Efficiency: Performance per Compute Hour")
    df["efficiency"] = df["performance_score"] / df["compute_hours"]

    chart = alt.Chart(df).mark_circle(size=100).encode(
        x="compute_hours",
        y="performance_score",
        color="domain",
        tooltip=["algorithm", "domain", "compute_hours", "performance_score", "efficiency"]
    ).interactive()

    st.altair_chart(chart, use_container_width=True)

    st.subheader("Top Algorithms by Efficiency")
    top_eff = df.sort_values(by="efficiency", ascending=False).head(10)
    st.dataframe(top_eff[["domain", "algorithm", "efficiency"]])
else:
    st.warning("Upload data to begin analysis.")

# %%
