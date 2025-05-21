# ✈️ Smart Flight Dashboard

**Smart Flight** adalah aplikasi dashboard interaktif berbasis Streamlit yang dirancang untuk membantu pengguna dalam memprediksi harga tiket pesawat dari Jakarta ke berbagai kota populer di Indonesia. Dashboard ini memanfaatkan model time series Prophet dan akan dikembangkan lebih lanjut dengan fitur klasifikasi harga serta sistem rekomendasi.

---

## 🔧 Fitur Utama

- 📈 **Price Forecasting**  
  Prediksi harga tiket untuk 7 hari ke depan dari Jakarta ke kota-kota tujuan populer seperti Surabaya (SUB), Bali (DPS), Bandung (BDO), dan lainnya.

- 💰 **Price Classification** *(Coming Soon)*  
  Klasifikasi harga tiket ke dalam kategori: murah, sedang, atau mahal berdasarkan input pengguna.

- 🎯 **Recommendation System** *(Coming Soon)*  
  Memberikan saran waktu terbaik untuk membeli tiket dengan harga terendah.

- ℹ️ **About Page**  
  Informasi pengembang dan deskripsi aplikasi.

---

## 🗂️ Struktur Proyek

smart-flight-dashboard/

├── pages/

│ ├── homepage.py

│ ├── forecast.py

│ ├── classification.py

│ ├── recommendation.py

│ └── about.py

├── models/

│ └── predict_popular_ticket/

│ ├── prophet_model_SUB.pkl

│ ├── prophet_model_DPS.pkl

│ └── ... lainnya

├── app.py

├── README.md

└── requirements.txt


---

## 🚀 Cara Menjalankan

1. **Clone repositori ini**

   ```bash
   git clone https://github.com/username/smart-flight-dashboard.git
   cd smart-flight-dashboard
   ```
2. **Buat virtual environment (opsional)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
3. **Install dependensi**

    ```bash
    pip install -r requirements.txt
    ```

4. **Jalankan Aplikasi**

    ```bash
    streamlit run app.py
    ```

## 📦 Dependensi Utama
- streamlit
- pandas
- prophet
- plotly
- pickle

Lihat requirements.txt untuk daftar lengkap.

## 🧠 Teknologi yang Digunakan
- **Streamlit** – Untuk UI dashboard interaktif.
- **Facebook Prophet** – Untuk model prediksi harga tiket.
- **Plotly** – Untuk visualisasi data yang interaktif.

## 📝 Catatan Pengembangan
Fitur klasifikasi harga dan sistem rekomendasi masih dalam tahap pengembangan dan akan segera ditambahkan pada versi mendatang.

## 👨‍💻 Creator
Defrizal Yahdiyan Risyad – Student