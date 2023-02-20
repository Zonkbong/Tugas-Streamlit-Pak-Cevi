import streamlit as st
import pandas as pd
import numpy as np

# LineChart
st.header("Latihan 1 - Chart (Line Chart dan Bar Chart)")
st.write("#")

st.header("Line Chart Penjualan Bunga")

st.subheader("Januari")
jan_bunga = pd.DataFrame({
    "Minggu" : [1, 2, 3, 4],
    "Jual" : [12, 15, 8, 10]
})

st.line_chart(jan_bunga)

# BarChart

st.write("##")

st.header("Bar Chart Penjualan Bunga")
st.subheader("Februari")

feb_bunga = pd.DataFrame(
    np.random.randn(28, 4),
    columns=["Minggu 1", "Minggu 2", "Minggu 3", "Minggu 4"]
)

st.bar_chart(feb_bunga)

