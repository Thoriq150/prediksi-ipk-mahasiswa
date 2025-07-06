
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

# Judul Aplikasi
st.title("Prediksi IPK Mahasiswa 📚")
st.write("Masukkan nilai berikut untuk memprediksi IPK semester ini:")

# Input user
visited = st.slider("Jumlah kehadiran (VisITedResources)", 0, 100)
tugas = st.slider("Jumlah pengumpulan tugas (raisedhands)", 0, 100)
diskusi = st.slider("Jumlah partisipasi diskusi", 0, 100)

# Prediksi saat tombol ditekan
if st.button("Prediksi IPK"):
    data = np.array([[visited, tugas, diskusi]])
    prediksi_ipk = model.predict(data)[0]
    st.success(f"✅ Prediksi IPK kamu adalah: **{prediksi_ipk:.2f}**")
