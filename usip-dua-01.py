# TODO: Buat program untuk menghitung kecepatan benda saat menyentuh tanah
# rumus: vf = sqrt(vi^2 + 2ad)
# vf = kecepatan akhir
# vi = kecepatan awal
# a = percepatan
# d = jarak


import math

kec_awal = float(input("Masukan kecepatan awal (m/s): "))
percepatan = float(input("Masukan percepatan (m/s^2): "))
jarak = float(input("Masukan jarak (m): "))


def kecepatan_akhir(vi, a, d):
    """Hitung nilai kecepatan akhir"""
    return math.sqrt((vi ** 2) + (2 * a * d))


vf = kecepatan_akhir(kec_awal, percepatan, jarak)

print(f"Kecepatan pada jarak {jarak} m adalah {round(vf, 3)} m/s")
