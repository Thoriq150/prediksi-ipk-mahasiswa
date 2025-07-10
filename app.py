import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load("model.pkl")

# Judul Aplikasi
st.title("🎓 Prediksi IPK Mahasiswa")
st.markdown("""
Aplikasi ini menggunakan model regresi linear untuk memprediksi **IPK semester ini**
berdasarkan 3 variabel:
- Jumlah kehadiran (`VisITedResources`)
- Jumlah pengumpulan tugas (`raisedhands`)
- Partisipasi diskusi (`Discussion`)
""")

st.sidebar.header("Input Nilai Mahasiswa")

# Input Form
visited = st.sidebar.slider("📘 Jumlah kehadiran (VisITedResources)", 0, 100, 50)
tugas = st.sidebar.slider("📝 Jumlah tugas dikumpulkan (raisedhands)", 0, 100, 50)
diskusi = st.sidebar.slider("💬 Partisipasi diskusi (Discussion)", 0, 100, 50)

# Prediksi
if st.sidebar.button("🔮 Prediksi IPK"):
    data = np.array([[visited, tugas, diskusi]])
    pred = model.predict(data)[0]
    
    st.subheader("🎯 Hasil Prediksi")
    st.success(f"Prediksi IPK: **{pred:.2f}**")

    # Interpretasi sederhana
    if pred >= 3.5:
        kategori = "Sangat Baik"
    elif pred >= 3.0:
        kategori = "Baik"
    elif pred >= 2.5:
        kategori = "Cukup"
    else:
        kategori = "Perlu Perbaikan"
    
    st.info(f"Kategori: **{kategori}**")

# Optional: Tampilkan Koefisien Model
st.markdown("---")
if st.checkbox("📊 Tampilkan Koefisien Model"):
    fitur = ["VisITedResources", "raisedhands", "Discussion"]
    koef = model.coef_
    intercept = model.intercept_

    df_coef = pd.DataFrame({
        "Fitur": fitur,
        "Koefisien": koef
    })

    st.write("Koefisien Regresi Linear:")
    st.dataframe(df_coef, use_container_width=True)
    st.caption(f"Intercept: {intercept:.2f}")
