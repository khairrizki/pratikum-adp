data_nilai = [
    {"nama": "rizki", "nilai": [80, 75, 90, 85]},
    {"nama": "riski", "nilai": [70, 85, 80, 90]},
    {"nama": "rizky", "nilai": [60, 70, 75, 80]},
    {"nama": "risky", "nilai": [90, 95, 85, 90]},
]

mata_kuliah = ["Kalkulus 2", "Matdis", "ADP", "Geonal"]

print("Data Nilai Ujian:")
print("=================")
for data in data_nilai:
    print(f"{data['nama']}: {data['nilai']}")

print("\nRata-rata Nilai Ujian Setiap Mahasiswa:")
print("=======================================")
for data in data_nilai:
    nama = data["nama"]
    rata = sum(data["nilai"]) / 4
    print(f"{nama}: {rata}")

nilai_tertinggi_mata_kuliah = [data_nilai[0]["nilai"][i] for i in range(4)]
nilai_terendah_mata_kuliah = [data_nilai[0]["nilai"][i] for i in range(4)]
nama_tertinggi_mata_kuliah = [data_nilai[0]["nama"] for _ in range(4)]
nama_terendah_mata_kuliah = [data_nilai[0]["nama"] for _ in range(4)]

for data in data_nilai[1:]:
    for i in range(4):
        nilai = data["nilai"][i]
        if nilai > nilai_tertinggi_mata_kuliah[i]:
            nilai_tertinggi_mata_kuliah[i] = nilai
            nama_tertinggi_mata_kuliah[i] = data["nama"]
        if nilai < nilai_terendah_mata_kuliah[i]:
            nilai_terendah_mata_kuliah[i] = nilai
            nama_terendah_mata_kuliah[i] = data["nama"]

print("\nNilai Tertinggi dan Terendah dari Setiap Mata Kuliah:")
print("=====================================================")
for i in range(4):
    print(f"{mata_kuliah[i]}: Nilai Tertinggi = {nilai_tertinggi_mata_kuliah[i]} (oleh {nama_tertinggi_mata_kuliah[i]}), Nilai Terendah = {nilai_terendah_mata_kuliah[i]} (oleh {nama_terendah_mata_kuliah[i]})")