# Laporan
# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

### Latar Belakang Bisnis
Jaya Jaya Maju adalah perusahaan edutech multinasional yang berfokus pada penyediaan platform pembelajaran online untuk lebih dari 1000 karyawan di berbagai departemen, seperti pengembangan konten, teknologi, dan dukungan pelanggan. Perusahaan ini berkembang pesat, namun menghadapi tantangan signifikan akibat tingginya *attrition rate* (tingkat turnover karyawan) yang melebihi 10%. Tingginya turnover ini mengakibatkan hilangnya keahlian, biaya rekrutmen yang besar, dan gangguan dalam operasional, yang pada akhirnya dapat memengaruhi kualitas layanan edukasi yang diberikan kepada pengguna.

### Permasalahan Bisnis
1. Tingginya *attrition rate* (>10%) yang menyebabkan kehilangan talenta berpengalaman.
2. Kurangnya pemahaman mendalam tentang faktor-faktor yang memicu karyawan keluar, seperti kepuasan kerja, gaji, lembur, atau masa kerja.
3. Ketidakmampuan departemen HR untuk memantau dan mengambil tindakan preventif terhadap *attrition* secara real-time.
4. Biaya operasional yang meningkat akibat proses rekrutmen dan pelatihan karyawan baru.

### Cakupan Proyek
Proyek ini mencakup:
- Analisis data karyawan untuk mengidentifikasi faktor-faktor utama yang memengaruhi *attrition*.
- Pengembangan model machine learning untuk memprediksi kemungkinan karyawan keluar.
- Pembuatan *business dashboard* menggunakan Metabase untuk memantau faktor-faktor *attrition* secara visual.
- Dokumentasi temuan dan rekomendasi action items untuk membantu HR mengurangi *attrition rate*.

## Persiapan
- **Sumber Data**: Dataset berisi informasi karyawan (`employee.db`) dengan 1470 baris dan 35 kolom, meliputi data demografi, gaji, kepuasan kerja, dan status *attrition*. Data diambil dari [Dicoding Academy - Employee Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee) dan data yang sudah dikonversi menjadi `employee.db` diambil dari [https://github.com/MHafisAfrizal/Dataset_Employe].
- **Setup Environment**:
  - **Pilihan 1: Menggunakan Anaconda**
    1. Instal Anaconda dari [situs resmi](https://www.anaconda.com/products/distribution).
    2. Buat virtual environment:
    conda create -n edutech_project python=3.9
    3. Aktifkan virtual environment:
    conda activate edutech_project

    - **Pilihan 2: Menggunakan Shell/Terminal**
    1. Pastikan Python terinstall di sistem Anda.
    2. Buat virtual environment:
    python -m venv venv
    3. Aktifkan virtual environment:

    - **Windows**:
    venv\Scripts\activate
    - **Linux/macOS**:
    source venv/bin/activate
    4. Pastikan prompt terminal menunjukkan `(venv)` atau nama environment di awal.

- **Menginstal Dependensi dari requirements.txt**:
  - Pastikan file `requirements.txt` ada di direktori proyek.
  - Instal semua dependensi yang dibutuhkan dengan perintah:
    pip install -r requirements.txt
  - Catatan: File `requirements.txt` berisi `pandas` dan `scikit-learn`. Jika ada masalah kompatibilitas dengan model, instal versi spesifik `scikit-learn` (misalnya 1.6.1) dengan:
    pip install scikit-learn==1.6.1

- **Mengatur Docker dan Metabase**:
  - Pastikan Docker terinstall di sistem Anda.
  - Jalankan Metabase dengan perintah:
    docker run -d -p 4000:3000 -v C:/Users/HP/Downloads:/data --name metabase metabase/metabase
  - Tunggu beberapa detik sampai Metabase aktif, lalu akses di `http://localhost:4000`.
  - Impor file `employee.db` ke Metabase melalui **Admin settings > Databases**.

## Business Dashboard
Dashboard interaktif dibuat menggunakan Metabase sebagai tool utama untuk memantau faktor-faktor utama yang memengaruhi *attrition rate* di Jaya Jaya Maju. Dashboard ini mencakup visualisasi berikut:
- **Attrition berdasarkan Pendapatan Bulanan**: Mengindikasikan bahwa karyawan dengan pendapatan rendah memiliki risiko *attrition* lebih tinggi.
- **Attrition berdasarkan Kepuasan Kerja**: Menunjukkan bahwa karyawan dengan kepuasan kerja rendah (1-2) lebih cenderung keluar.
- **Attrition berdasarkan Lembur**: Menyoroti bahwa karyawan yang sering lembur (OverTime = Yes) lebih mungkin keluar.
- **Attrition berdasarkan Masa Kerja**: Mengungkapkan bahwa karyawan dengan masa kerja pendek (0-5 tahun) lebih rentan keluar.

Screenshot tersedia di file `hafis_afriz2l-dashboard.png`. Untuk mengakses dashboard interaktif, gunakan file `metabase.db.mv.db` dan kredensial berikut:
- Username: hafisafrizal10@gmail.com
- Password: Naras123!
- URL: http://localhost:4000
(Kredensial ini juga tersedia di file `credentials.txt` untuk kemudahan akses.) Jalankan Metabase sesuai instruksi di atas, lalu impor database melalui antarmuka Metabase.

## Menjalankan Prediksi
Setelah setup environment selesai, jalankan berkas `prediction.py` (file utama untuk prediksi) dengan perintah berikut di terminal:

python prediction.py
atau klik https://projek-prediction-karyawan-e6vdzsdim3wdvivauzm3c6.streamlit.app/

- Pastikan virtual environment aktif sebelum menjalankan perintah di atas (lihat instruksi di "Setup Environment").
- **Prasyarat Penting**: 
  - File model `rf_model.pkl` diperlukan untuk menjalankan prediksi. Pastikan file ini tersedia di folder `model` dalam direktori proyek (misalnya `C:\Users\HP\Downloads\SubmissionUno\model\rf_model.pkl`). Jika belum ada, unduh dari Colab (https://colab.research.google.com/drive/1ajdUPc0OeGYRKLIwaIZyFjn6iX2sGLH1) dengan langkah berikut:
    - Buka link Colab di atas.
    - Cari bagian penyimpanan model (biasanya `pickle.dump`).
    - Unduh file `rf_model.pkl` dan simpan ke folder `model`.
  - Jika path berbeda, sesuaikan di kode `prediction.py` sesuai lokasi file.
- **Dependensi**: Pastikan dependensi berikut sudah terinstall. Instal dengan:
    pip install -r requirements.txt

Catatan: Model mungkin memerlukan versi spesifik `scikit-learn` (misalnya 1.6.1). Jika ada masalah kompatibilitas, instal dengan:
    pip install scikit-learn==1.6.1


## Conclusion
Berdasarkan analisis data dan pemodelan, ditemukan bahwa faktor utama *attrition* meliputi kepuasan kerja rendah, pendapatan bulanan rendah, kebiasaan lembur, dan masa kerja yang singkat. Model machine learning (Random Forest) yang dikembangkan mencapai akurasi sekitar 85%, memungkinkan prediksi *attrition* dengan baik. Dashboard Metabase memberikan alat visual untuk HR guna memantau tren *attrition* secara berkala. Proyek ini berhasil memberikan wawasan yang dapat digunakan untuk mengurangi turnover karyawan dan meningkatkan retensi.

### Rekomendasi Action Items (Optional)
- **Meningkatkan Kepuasan Kerja**: Mengadakan survei rutin dan program kesejahteraan karyawan, seperti pelatihan atau dukungan mental, untuk meningkatkan kepuasan kerja.
- **Menyesuaikan Gaji**: Meninjau ulang struktur gaji agar kompetitif, terutama untuk karyawan dengan pendapatan rendah.
- **Mengurangi Lembur**: Membatasi jam lembur dan memberikan kompensasi yang adil untuk karyawan yang bekerja ekstra.
- **Program Retensi Awal**: Mengimplementasikan program orientasi dan *mentoring* untuk karyawan baru agar mereka lebih betah di perusahaan.
