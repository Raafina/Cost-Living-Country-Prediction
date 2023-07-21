import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pickle
from sklearn.linear_model import LinearRegression

model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title('Cost of Living Index Prediction')
st.image('img.jpg', use_column_width=True)
st.write('The Cost of Living Index is a relative indicator of consumer goods prices, including groceries, restaurants, transportation and utilities. The Cost of Living Index does not include accommodation expenses such as rent or mortgage. If a city has a Cost of Living Index of 120, it means Numbeo has an estimated cost that is 20% more expensive than New York (excluding rent).')

col1, col2 = st.columns(2)

# Function to validate input as numeric value
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
# C:\Users\asd\TA_Datamining>streamlit run main.py
# Input
Indeks_Sewa = st.text_input("Input Rent Index: ")
Indeks_Grosir = st.text_input("Input Groceries Index: ")
Indeks_Harga_Restoran = st.text_input("Input Restaurant Price Index: ")
Indeks_Daya_Beli_Lokal = st.text_input("Input Local Purchasing Power Index:  ")

# prediksi
prediksi_Indeks_biaya_hidup = ''

# tombol untuk prediksi
if st.button('Prediction'):
    # Validate inputs as numeric values
    if is_numeric(Indeks_Sewa) and is_numeric(Indeks_Grosir) and is_numeric(Indeks_Harga_Restoran) and is_numeric(Indeks_Daya_Beli_Lokal):
        # Convert inputs to float
        Indeks_Sewa = float(Indeks_Sewa)
        Indeks_Grosir = float(Indeks_Grosir)
        Indeks_Harga_Restoran = float(Indeks_Harga_Restoran)
        Indeks_Daya_Beli_Lokal = float(Indeks_Daya_Beli_Lokal)
        
        # Perform prediction
        prediksi_Indeks_biaya_hidup = model.predict([[Indeks_Sewa, Indeks_Grosir, Indeks_Harga_Restoran, Indeks_Daya_Beli_Lokal]])
        st.write('Hasil Prediksi: ', prediksi_Indeks_biaya_hidup)
    else:
        st.write('Masukkan nilai numerik untuk semua input')

