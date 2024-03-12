def hitung_volume_permukaan(sisi_alas, tinggi):
    luas_permukaan = sisi_alas**2 + 4 * (sisi_alas * tinggi) / 2
    return luas_permukaan

def hitung_volume(sisi_alas, tinggi):
    volume = (sisi_alas**2 * tinggi) / 3
    return volume

sisi_alas = float(input("Masukkan panjang sisi alas limas segi empat: "))
tinggi = float(input("Masukkan tinggi limas segi empat: "))

luas_permukaan = hitung_volume_permukaan(sisi_alas, tinggi)
volume = hitung_volume(sisi_alas, tinggi)

print("Luas permukaan limas segi empat adalah:", luas_permukaan)
print("Volume limas segi empat adalah:", volume)

