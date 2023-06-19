# Program untuk mengecek tahun kabisat (Leap year)
# Contoh input:
# Tahun yang akan diuji: 2000
# Contoh output:
# Tahun 2000 adalah tahun kabisat
# NB. Tahun kabisat adalah periode waktu di mana satu tahun terdiri dari 366 hari.


tahun_uji = int(input("Masukan tahunn yang akan diuji: "))


def tahun_kabisat(tahun):
    """Menghitung tahun kabisat"""
    if tahun % 4 == 0:
        if tahun % 100 == 0:
            if tahun % 400 == 0:
                print("Tahun", tahun, "adalah tahun kabisat")
            else:
                print("Tahun", tahun, "bukan tahun kabisat")
        else:
            print("Tahun", tahun, "adalah tahun kabisat")
    else:
        print("Tahun", tahun, "bukan tahun kabisat")


tahun_kabisat(tahun_uji)
