import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# JUDUL
st.title("Evaluasi Akademik")

st.write("Aplikasi sederhana berbasis Matematika Terapan")

# INPUT
nama = st.text_input("Masukkan Nama Siswa")

tugas = st.number_input("Nilai Tugas", 0, 100)
uts = st.number_input("Nilai UTS", 0, 100)
uas = st.number_input("Nilai UAS", 0, 100)

# TOMBOL
if st.button("Hitung"):

    # MODEL MATEMATIKA / SPL
    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

    st.subheader("Model Matematis")

    st.latex(r"NA = 0.3(Tugas) + 0.3(UTS) + 0.4(UAS)")

    # LOGIKA
    if nilai_akhir >= 85:
        kategori = "Sangat Baik"
    elif nilai_akhir >= 70:
        kategori = "Baik"
    else:
        kategori = "Perlu Evaluasi"

    st.success(f"Nama Siswa : {nama}")
    st.success(f"Nilai Akhir : {nilai_akhir:.2f}")
    st.success(f"Kategori : {kategori}")

    # MATRIKS
    st.subheader("Matriks Nilai")

    matriks = np.array([
        [tugas, uts, uas]
    ])

    st.write(matriks)

    # DETERMINAN
    st.subheader("Determinan")

    A = np.array([
        [1, 2, 3],
        [0, 1, 4],
        [5, 6, 0]
    ])

    determinan = np.linalg.det(A)

    st.write("Nilai Determinan =", round(determinan, 2))

    # VEKTOR
    st.subheader("Magnitude Vektor")

    vektor = np.array([tugas, uts, uas])

    magnitude = np.linalg.norm(vektor)

    st.write("Magnitude =", round(magnitude, 2))

    # HIMPUNAN
    st.subheader("Operasi Himpunan")

    A = {"Matematika", "Fisika", "Kimia"}
    B = {"Fisika", "Biologi"}

    st.write("Gabungan (A ∪ B) =", A.union(B))
    st.write("Irisan (A ∩ B) =", A.intersection(B))

    # GRAFIK
    st.subheader("Grafik Nilai")

    fig, ax = plt.subplots()

    pelajaran = ["Tugas", "UTS", "UAS"]
    nilai = [tugas, uts, uas]

    ax.bar(pelajaran, nilai)

    ax.set_ylabel("Nilai")
    ax.set_title("Grafik Nilai Siswa")

    st.pyplot(fig)