# import random

def main():
    # menghitung dan menampilkan nilai mhs
    # membutuhkan nama, nilai UTS dan nila UAS
    nama = input("Nama: ")
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    # membuat turunan dari objek muridLG
    st = muridLG(nama, uts, uas)
    print("\nNama\tNilai")
    # menampilkan nama dan nilai (grade)
    print(st)


class muridLG:
    # constructor ini akan dijalankan saat objek pertama kali dibuat.
    def __init__(self, nama="",  uts=0, uas=0):
        self._nama = nama                      # self._nama adalah variabel instance
        self._uts = uts                       # nama, uts, dan uas adalah variabel lokal
        self._uas = uas

    def aturNama(self, nama):       # method ini akan mengatur nama
        self._nama = nama         # self._nama adalah variabel instance, nama adalah variabel lokal

    def aturUts(self, uts):
        self._uts = uts

    def aturUas(self, uas):
        self._uas = uas

# method ini akan menghitung nilai. self sebagai parameter pertama
# adalah variabel instance.
    def hitungNilai(self):
        ratarata = (self._uts + self._uas)/2
        ratarata = round(ratarata)
        if ratarata >= 90:
            return "A"
        if ratarata >= 80:
            return "B"
        if ratarata >= 70:
            return "C"
        if ratarata >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):  # state representasi method
        return (self._nama + "\t" + self.hitungNilai())


main()

# masih ada error

# Class merupakan blueprint dari objek. Class mendefinisikan atribut dan method
# yang akan dimiliki oleh objek.
# Class dapat memiliki atribut dan method. Atribut adalah variabel yang
# dimiliki oleh class. Method adalah fungsi yang dimiliki oleh class.
# Objek adalah instance dari class. Objek memiliki atribut dan method yang
# sama dengan class.
# Constructor adalah method yang akan dijalankan saat objek pertama
# kali dibuat.
# Variabel instance adalah variabel yang dimiliki oleh objek.
# Variabel lokal adalah variabel yang dimiliki oleh method.
# Variabel global adalah variabel yang dapat diakses oleh semua
# method dan class.
# Encapsulation adalah cara untuk menyembunyikan variabel dan method agar
# tidak dapat diakses secara langsung dari luar class.
# Inheritance adalah cara untuk membuat class baru yang merupakan turunan dari
# class yang sudah ada.
# Polymorphism adalah kemampuan untuk membuat method dengan nama yang sama pada
# class yang berbeda.
# Overloading adalah kemampuan untuk membuat method dengan nama yang sama,
# tetapi dengan parameter yang berbeda.
# Overriding adalah kemampuan untuk membuat method dengan nama yang sama pada
# class yang berbeda, dengan isi yang berbeda pula.
