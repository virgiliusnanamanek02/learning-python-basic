
def hitung_barang_dan_biaya(jumlah_sepatu):
    harga_per_pasang = 50000
    jumlah_dapat = 0

    if jumlah_sepatu % 2 == 0:  # Jika jumlah sepatu dibeli adalah bilangan genap
        # Jumlah dapat = jumlah sepatu dibagi 2 * 3
        jumlah_dapat = jumlah_sepatu // 2 * 3
    else:
        jumlah_dapat = jumlah_sepatu

    biaya_total = jumlah_sepatu * harga_per_pasang
    return jumlah_dapat, biaya_total


jumlah_sepatu = int(input("Jumlah sepatu yang dibeli (pasang): "))
jumlah_dapat, biaya_total = hitung_barang_dan_biaya(jumlah_sepatu)
print("Jumlah sepatu yang diperoleh adalah", jumlah_dapat, "pasang")
print("Biaya yang harus dibayarkan adalah Rp.", biaya_total)
