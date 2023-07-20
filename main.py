import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pickle
from sklearn.linear_model import LinearRegression

model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title('Prediksi Index Sewa')
st.write('Nama : Raafi Nur Adzani')
st.write('NIM : A11.2021.13536')

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
Indeks_Sewa = st.text_input("Masukkan Indeks Sewa: ")
Indeks_Grosir = st.text_input("Masukkan Indeks Grosir: ")
Indeks_Harga_Restoran = st.text_input("Masukkan Harga Restoran: ")
Indeks_Daya_Beli_Lokal = st.text_input("Masukkan Daya Beli Lokal: ")

# prediksi
prediksi_Indeks_biaya_hidup = ''

# tombol untuk prediksi
if st.button('Prediksi'):
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

