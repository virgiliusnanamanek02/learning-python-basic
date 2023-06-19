"""
Di sebuah toko tertera promosi pembelian sepatu beli 2 dapat 3 dengan harga per pasang Rp.
50.000,-. Buatkan program untuk membantu menghitung barang yang didapat dan biaya yang
harus dibayarkan.
Contoh
Jumlah sepatu yang dibeli (pasang): 3
Jumlah sepatu yang diperoleh adalah 3 pasang
Biaya yang harus dibayarkan adalah Rp. 150.000,-.
"""
jumlah_sepatu = int(input("Jumlah sepatu yang dibeli (pasang): "))

BIAYA_PER_PASANG = 50000


def jumlah_pasang(pasang):
    """Menghitung jumlah pasang sepatu"""
    for i in range(pasang // 2):
        pasang += 1
        return pasang


def biaya(pasang):
    """Menghitung biaya yang harus dibayar"""
    # Jika pasang  merupakan bilangan genap, maka pasangnya selalu ditambah 1
    # 2 maka 3, 4 maka 6, 6 maka 9

    if pasang % 2 == 0:
        pasang += 1
    return BIAYA_PER_PASANG * pasang


print(
    f"Jumlah sepatu yang diperoleh adalah {jumlah_pasang(jumlah_sepatu)} pasang")
print(f"Biaya yang harus dibayarkan adalah Rp. {biaya(jumlah_sepatu)}")
