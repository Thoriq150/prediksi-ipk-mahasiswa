# 🎓 Prediksi IPK Mahasiswa dengan Streamlit

Aplikasi ini dibuat untuk memprediksi **IPK semester ini** berdasarkan tiga parameter:
- Jumlah kehadiran (`VisITedResources`)
- Jumlah pengumpulan tugas (`raisedhands`)
- Jumlah partisipasi diskusi (`Discussion`)

Model ini menggunakan pendekatan **regresi linier** dan dibangun dalam konteks praktikum Data Mining.

---

## 🚀 Demo Aplikasi

🌐 Akses langsung aplikasi Streamlit di:
👉 [Klik di sini untuk mencoba aplikasinya](https://prediksi-ipk-mahasiswa-khdwval3exehjkwz5rs5tv.streamlit.app/)

---

## 🧪 Dataset

Dataset yang digunakan:
- 📥 **Nama:** [Student Performance Dataset (xAPI-Edu-Data)](https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data)
- 📄 Sumber: Kaggle

Fitur input yang digunakan:
- `VisITedResources` → jumlah akses materi (sebagai proxy kehadiran)
- `raisedhands` → jumlah pengumpulan tugas
- `Discussion` → keaktifan dalam diskusi kelas

Target/output:
- `Class` → dikonversi ke skor IPK (H = 4.0, M = 3.0, L = 2.0)

---

## 🛠 Teknologi yang Digunakan

- Python
- Scikit-Learn
- Pandas
- NumPy
- Streamlit
- Joblib

---

## 🧾 Cara Menjalankan (Local)
1. Clone repository ini:

2. Install dependencies:

3. Jalankan aplikasi:

---

## 📦 Struktur Folder

├── app.py # Aplikasi Streamlit
├── model.pkl # Model regresi yang sudah dilatih
├── requirements.txt # Daftar dependensi Python
└── xAPI-Edu-Data.csv # Dataset asli (opsional)

---

## 📚 Penjelasan Model

- Menggunakan **Linear Regression** dari Scikit-Learn
- Model dilatih menggunakan 80% data dan diuji dengan 20% data sisanya
- Target IPK dihitung dari label `Class` → dikonversi ke nilai IPK numerik

---

## 📌 Kontributor

Kelompok 10 – Praktikum Data Mining 2025  
Universitas [Nama Kampusmu]

---

## 🏁 Lisensi

Proyek ini dibuat untuk keperluan edukasi dan praktikum.

