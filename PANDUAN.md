# Panduan Modifikasi Dashboard

## Struktur File

```
Final/
├── streamlit\\\_app.py          ← Entry point utama
├── requirements.txt
├── .streamlit/
│   └── config.toml           ← Tema warna dasar Streamlit
├── data/                     ← File CSV \\\& JSON dari notebook
└── components/
    ├── loader.py             ← (1) Baca data \\\& hitung parameter terbaik
    ├── styles.py             ← (2) Semua CSS \\\& navbar
    ├── section\\\_params.py     ← (3) Kartu dataset + kartu parameter terbaik + tabel 10 terbaik
    ├── section\\\_grid.py       ← (4) Line chart \\\& heatmap K x Alpha
    └── section\\\_model.py      ← (5) Bar chart \\\& tabel perbandingan model
```

\---

## Mau ubah apa? Buka file mana?

### Judul / nama sistem di navbar

→ `components/styles.py` — cari fungsi `navbar()` di bagian bawah file

### Warna tema (biru navy, putih, dsb)

→ `components/styles.py` — ubah nilai hex seperti `#0F2D6B` (navy gelap) atau `#1D4ED8` (biru terang)
→ `.streamlit/config.toml` — untuk warna dasar Streamlit (background, primary color)

### Kartu ringkasan dataset (Kombinasi Diuji, Jumlah User, dst)

→ `components/section\\\_params.py` — fungsi `render\\\_dataset\\\_stats()`

### Kartu parameter terbaik (K, Alpha, RMSE, MAE)

→ `components/section\\\_params.py` — fungsi `render\\\_best\\\_params\\\_with\\\_table()`

### Tabel 10 kombinasi terbaik

→ `components/section\\\_params.py` — bagian bawah fungsi `render\\\_best\\\_params\\\_with\\\_table()`

### Line chart \& heatmap grid search

→ `components/section\\\_grid.py`

* Ganti warna garis: ubah list `NAVY\\\_PALETTE`
* Ubah judul chart: cari parameter `title=`
* Ubah label sumbu: cari parameter `labels=`

### Bar chart \& tabel perbandingan model

→ `components/section\\\_model.py`

* Ganti warna bar RMSE: `marker\\\_color="#0F2D6B"`
* Ganti warna bar MAE: `marker\\\_color="#60A5FA"`

### Sumber data / folder CSV

→ `streamlit\\\_app.py` — baris `DATA\\\_DIR = "data"`, ganti nama foldernya

### Menambah section baru

1. Buat file baru di `components/`, misalnya `section\\\_baru.py`
2. Buat fungsi `render()` di dalamnya
3. Import dan panggil di `streamlit\\\_app.py`

\---

## Cara menjalankan

```bash
streamlit run streamlit\\\_app.py
```

Pastikan sudah install dependencies:

```bash
pip install -r requirements.txt
```

