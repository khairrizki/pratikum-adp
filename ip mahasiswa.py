def hitung_bobot(nilai_huruf):
    bobot = {'A': 4.0, 'A-': 3.75, 'B+': 3.5, 'B': 3.0, 'B-': 2.75, 'C+': 2.5, 'C': 2.0, 'C-': 1.75, 'D+': 1.5, 'D': 1.0, 'D-':0.75 ,'E': 0.0}
    return bobot.get(nilai_huruf, 0.0)

def hitung_ip(nilai, sks):
    total_sks = sum(sks)
    total_bobot = sum(nilai[i] * sks[i] for i in range(len(nilai)))
    ip = total_bobot / total_sks
    return ip

def main():
    matkul = {
        "Agama": 2,
        "Fisika dasar": 2,
        "Kimia dasar": 2,
        "Pengmat": 3,
        "Bahasa Inggris": 2,
        "Kakulus 1":3,
        "Andat":3,
        "Bahasa Indonesia" :2,
    }

    nilai = []
    sks = []

    for mk, jml_sks in matkul.items():
        nilai_mata_kuliah = input(f"Masukkan nilai mata kuliah ").upper()
        while nilai_mata_kuliah not in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'E']:
            print("Nilai yang dimasukkan harus dalam format yang valid.")
            nilai_mata_kuliah = input(f"Masukkan nilai mata kuliah  ").upper()
        nilai.append(hitung_bobot(nilai_mata_kuliah))
        sks.append(jml_sks)

    print("\nNilai dan SKS untuk setiap mata kuliah:")
    for mk, jml_sks in matkul.items():
        idx = list(matkul.keys()).index(mk)
        print(f"Mata kuliah {mk}: Nilai = {nilai[idx]}, SKS = {jml_sks}")

    ip = hitung_ip(nilai, sks)
    print("\nIndeks Prestasi (IP) Anda adalah:", ip)

if __name__ == "__main__":
    main()