
# Freshify

Freshify adalah software berbasis CLI untuk sistem toko online yang memudahkan pengelolaan inventaris dan transaksi. Aplikasi ini menyediakan fitur autentikasi pengguna, sistem CRUD untuk pengelolaan item, penyimpanan data dalam format JSON, dan proses checkout yang terintegrasi dengan Firebase.

## Features

- **Autentikasi Pengguna**  
  Memungkinkan pengguna untuk mendaftar dan login ke akun mereka.
  
- **Sistem CRUD User**  
  Pengguna dapat memilih item yang akan disimpan, dengan teknologi relasional untuk memastikan data tidak tertukar antar pengguna.

- **Penyimpanan Data dalam JSON**  
  Data disimpan dalam format JSON untuk pengelolaan yang efisien.

- **Proses Checkout**  
  Setelah memilih item, data checkout akan disimpan di Firebase untuk pengelolaan lebih lanjut.

## Prasyarat

- **Git** versi terbaru.
- **Python 3.11.10** atau versi terbaru.
- **pip** (pengelola paket Python) diperbarui ke versi terbaru.

## Installation

1. **Clone repository ini** ke komputer Anda:
   ```bash
   git clone https://github.com/ersaridhofangestu/Freshify.git
   cd Freshify
   ```

2. **Buat dan aktifkan virtual environment** (opsional, disarankan):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Untuk pengguna MacOS/Linux
   venv\Scriptsctivate      # Untuk pengguna Windows
   ```

3. **Instal dependensi yang dibutuhkan**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**:
   ```bash
   python main.py
   ```

## Run Locally

1. Clone project:
   ```bash
   git clone https://github.com/ersaridhofangestu/Freshify.git
   ```

2. Masuk ke direktori proyek:
   ```bash
   cd Freshify
   ```

3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan server:
   ```bash
   python main.py
   ```

## Tech Stack

Berikut adalah teknologi yang digunakan dalam proyek ini:

- **CLI:** Python (utama)
- **Pandas:** Untuk pengolahan data
- **Prompt-toolkit:** Untuk interaksi berbasis teks
- **Rich:** Untuk tampilan CLI yang lebih menarik
- **Tabulate:** Untuk format tampilan tabel yang lebih rapi

### ![Python](https://img.icons8.com/?size=100&id=13441&format=png&color=000000)  
**Python** adalah bahasa pemrograman yang digunakan untuk mengembangkan aplikasi ini.  

### ![Pandas](https://img.icons8.com/?size=100&id=xSkewUSqtErH&format=png&color=000000)  
**Pandas** digunakan untuk mengelola dan menganalisis data dalam aplikasi ini.

### ![Firebase](https://img.icons8.com/?size=100&id=62452&format=png&color=000000)  
**Firebase** digunakan untuk menyimpan data checkout dan manajemen pengguna.

## Team Pembuat

1. **Ersa Ridho fangestu** - Project Lead, Pengembangan Fitur Autentikasi dan Sistem CRUD
2. **Rendy Ferdiansyah** - Backend Developer, Pengembangan API dan Firebase Integration
3. **Risandi Arfanni** - Frontend Developer, Implementasi Antarmuka CLI
4. **Kasih setia gaho** - Data Specialist, Pengolahan dan Penyimpanan Data
5. **Yoseph Wai** - QA & Testing, Pengujian Sistem dan Debugging

## License

Distributed under the MIT License. See `LICENSE` for more information.
