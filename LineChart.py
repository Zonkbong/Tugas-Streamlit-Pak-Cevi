import streamlit as st
import pandas as pd
import numpy as np
import random as rd

st.header("Data penjualan")
st.subheader("")

data = pd.DataFrame({
   "Bulan": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
   "Unit" : [100, 200, 135, 310, 240, 330, 210, 70, 541, 293, 118, 666]
})

st.write(data)

dataframe = np.random.randn(5, 10)
st.dataframe(dataframe)


st.subheader("Line chart Penjualan Upin Ipin")
st.line_chart(data)