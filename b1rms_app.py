#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

# B1RMS Calculation Function
def b1rms(a, tr, te, ns, st, pes, etl, na):
    return round(1.788 + 0.064*ns + 0.012*st - 0.00047*tr + 0.00094*te 
                 - 0.666*na - 0.00029*pes + 0.0145*a + 0.089*etl, 3)

# Streamlit App UI
st.set_page_config(page_title="B1RMS Calculator", layout="centered")

st.title("🧠 B1RMS Prediction Tool")
st.markdown("Enter the MRI sequence parameters below to calculate the **predicted B1RMS** value.")

# User Inputs
ns = st.number_input("Number of Slices", min_value=1, max_value=100, value=16)
st_ = st.number_input("Slice Thickness (mm)", min_value=0.1, max_value=10.0, value=3.0, step=0.1)
tr = st.number_input("TR (ms)", min_value=1, value=2000)
te = st.number_input("TE (ms)", min_value=0.1, value=80.0)
na = st.number_input("Number of Averages (NEX)", min_value=1, max_value=10, value=2)
pes = st.number_input("Phase Encoding Steps", min_value=1, value=256)
fa = st.number_input("Flip Angle (°)", min_value=0, max_value=360, value=150)
etl = st.number_input("Echo Train Length", min_value=1, max_value=64, value=16)

# Calculate
if st.button("Calculate B1RMS"):
    result = b1rms(fa, tr, te, ns, st_, pes, etl, na)
    st.success(f"✅ Predicted B1RMS: **{result}**")



# In[ ]:




