import streamlit as st
import pandas as pd
import pickle

# Load model
try:
    with open('Model/rf_model.pkl', 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"❌ Gagal memuat model: {e}")
    st.stop()

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Karyawan Keluar",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="auto"
)

# Styling manual dengan markdown CSS
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #4b6cb7;
        }
        .stButton>button {
            background-color: #4b6cb7;
            color: white;
            border-radius: 8px;
            padding: 0.5em 2em;
        }
        .result-box {
            background-color: #eaf2f8;
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
            border-left: 5px solid #4b6cb7;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">💼 Prediksi Karyawan Keluar atau Bertahan</p>', unsafe_allow_html=True)
st.markdown("Masukkan data karyawan dengan lengkap untuk mengetahui prediksi kemungkinan mereka keluar dari perusahaan.")

# Expander agar lebih rapi
with st.expander("📝 Isi Data Karyawan di Sini", expanded=True):

    col1, col2 = st.columns(2)

    with col1:
        Age = st.slider("Usia", 18, 60, 30)
        DailyRate = st.number_input("Gaji Harian", 100, 2000, 800)
        DistanceFromHome = st.slider("Jarak dari Rumah (km)", 0, 30, 10)
        Education = st.selectbox("Tingkat Pendidikan", [1, 2, 3, 4, 5])
        EnvironmentSatisfaction = st.selectbox("Kepuasan Lingkungan", [1, 2, 3, 4])
        Gender = st.radio("Jenis Kelamin", ["Female", "Male"])
        HourlyRate = st.number_input("Gaji per Jam", 10, 200, 60)
        JobInvolvement = st.selectbox("Keterlibatan Kerja", [1, 2, 3, 4])
        JobLevel = st.selectbox("Level Jabatan", [1, 2, 3, 4, 5])
        JobSatisfaction = st.selectbox("Kepuasan Jabatan", [1, 2, 3, 4])
        MonthlyIncome = st.number_input("Gaji Bulanan", 1000, 25000, 5000)

    with col2:
        BusinessTravel = st.selectbox("Frekuensi Perjalanan Dinas", ["Rarely", "Frequently", "Non-Travel"])
        Department = st.selectbox("Departemen", ["HR", "R&D", "Sales"])
        EducationField = st.selectbox("Bidang Pendidikan", ["HR", "Life Sciences", "Marketing", "Medical", "Other", "Technical Degree"])
        JobRole = st.selectbox("Peran Jabatan", ["HR", "Healthcare Rep", "Lab Technician", "Manager", "Manufacturing Director", "Research Director", "Research Scientist", "Sales Executive", "Sales Rep"])
        MaritalStatus = st.selectbox("Status Pernikahan", ["Divorced", "Married", "Single"])
        NumCompaniesWorked = st.slider("Jumlah Perusahaan Sebelumnya", 0, 10, 1)
        OverTime = st.radio("Lembur", ["No", "Yes"])
        PercentSalaryHike = st.slider("Kenaikan Gaji (%)", 10, 25, 15)
        PerformanceRating = st.selectbox("Penilaian Kinerja", [1, 2, 3, 4])
        RelationshipSatisfaction = st.selectbox("Kepuasan Relasi", [1, 2, 3, 4])
        StockOptionLevel = st.selectbox("Level Opsi Saham", [0, 1, 2, 3])

    TotalWorkingYears = st.slider("Total Tahun Pengalaman", 0, 40, 10)
    TrainingTimesLastYear = st.slider("Jumlah Pelatihan Tahun Ini", 0, 10, 3)
    WorkLifeBalance = st.selectbox("Keseimbangan Hidup-Kerja", [1, 2, 3, 4])
    YearsAtCompany = st.slider("Tahun di Perusahaan", 0, 40, 5)
    YearsInCurrentRole = st.slider("Tahun di Posisi Saat Ini", 0, 20, 3)
    YearsSinceLastPromotion = st.slider("Tahun Sejak Promosi Terakhir", 0, 15, 2)
    YearsWithCurrManager = st.slider("Tahun dengan Manager Saat Ini", 0, 20, 3)

# Tombol submit
if st.button("🔍 Prediksi Sekarang"):

    # Map input
    gender_map = {"Female": 0, "Male": 1}
    bt_map = {"Rarely": 0, "Frequently": 1, "Non-Travel": 2}
    dept_map = {"HR": 0, "R&D": 1, "Sales": 2}
    edu_field_map = {
        "HR": 0, "Life Sciences": 1, "Marketing": 2,
        "Medical": 3, "Other": 4, "Technical Degree": 5
    }
    jobrole_map = {
        "HR": 0, "Healthcare Rep": 1, "Lab Technician": 2, "Manager": 3,
        "Manufacturing Director": 4, "Research Director": 5, "Research Scientist": 6,
        "Sales Executive": 7, "Sales Rep": 8
    }
    marital_map = {"Divorced": 0, "Married": 1, "Single": 2}
    overtime_map = {"No": 0, "Yes": 1}

    input_data = pd.DataFrame([{
        'Age': Age,
        'BusinessTravel': bt_map[BusinessTravel],
        'DailyRate': DailyRate,
        'Department': dept_map[Department],
        'DistanceFromHome': DistanceFromHome,
        'Education': Education,
        'EducationField': edu_field_map[EducationField],
        'EnvironmentSatisfaction': EnvironmentSatisfaction,
        'Gender': gender_map[Gender],
        'HourlyRate': HourlyRate,
        'JobInvolvement': JobInvolvement,
        'JobLevel': JobLevel,
        'JobRole': jobrole_map[JobRole],
        'JobSatisfaction': JobSatisfaction,
        'MaritalStatus': marital_map[MaritalStatus],
        'MonthlyIncome': MonthlyIncome,
        'NumCompaniesWorked': NumCompaniesWorked,
        'OverTime': overtime_map[OverTime],
        'PercentSalaryHike': PercentSalaryHike,
        'PerformanceRating': PerformanceRating,
        'RelationshipSatisfaction': RelationshipSatisfaction,
        'StockOptionLevel': StockOptionLevel,
        'TotalWorkingYears': TotalWorkingYears,
        'TrainingTimesLastYear': TrainingTimesLastYear,
        'WorkLifeBalance': WorkLifeBalance,
        'YearsAtCompany': YearsAtCompany,
        'YearsInCurrentRole': YearsInCurrentRole,
        'YearsSinceLastPromotion': YearsSinceLastPromotion,
        'YearsWithCurrManager': YearsWithCurrManager
    }])

    # Prediksi
    try:
        prediction = model.predict(input_data)[0]
        result_text = "🌟 Karyawan ini diprediksi akan **BERTAHAN** di perusahaan." if prediction == 0 \
            else "⚠️ Karyawan ini diprediksi akan **KELUAR** dari perusahaan."

        st.markdown(f'<div class="result-box"><h4>{result_text}</h4></div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error saat memprediksi: {e}")
