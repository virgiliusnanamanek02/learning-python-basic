"""
Soal 5. (wajib membuat fungsi, minimal 2 buah)
Menghitung jumlah bilangan prima yang ada dari daŌar angka acak yang dibuat dalam jumlah
tertentu.
Contoh:
Jumlah bilangan acak dari 1 sd 20: 10
Bilangan acak yang terbentuk: [2, 15, 9, 14, 11, 5, 8, 9, 1, 12]
Terdapat 3 buah bilangan prima
"""

import random

bil_acak = int(input("Jumlah bilangan acak dari 1 sd 20: "))

list_bil_acak = []


def cek_prima(bil):
    if bil == 1:
        return False
    for i in range(2, bil):
        if bil % i == 0:
            return False
    return True


def hitung_jumlah_prima():
    jumlah_prima = 0
    for bil in list_bil_acak:
        if cek_prima(bil):
            jumlah_prima += 1
    return jumlah_prima


def generate_random_numbers(acak):
    for _ in range(acak):
        list_bil_acak.append(random.randint(1, 20))


generate_random_numbers(bil_acak)
print(f"Bilangan acak yang terbentuk: {list_bil_acak}")
print(f"Terdapat {hitung_jumlah_prima()} buah bilangan prima")
