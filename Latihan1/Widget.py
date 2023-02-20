import streamlit as st 
import pandas as pd
import numpy as np

st.header("Latihan 1 - Widget")
st.write("##")

with open("Gambar/8d5ed67105bfdf4b1116e2486b504847.jpg", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data = file.read(),
            file_name="8d5ed67105bfdf4b1116e2486b504847.jpg",
            mime="image/jpg"
          )