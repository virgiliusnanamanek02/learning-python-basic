def hitung_luas_alas(diameter):
    # Menghitung jari-jari dari diameter
    jari_jari = diameter / 2
    # Menghitung luas alas menggunakan rumus luas lingkaran
    luas_alas = 3.14 * jari_jari * jari_jari
    return luas_alas

def hitung_volume_tabung(diameter, tinggi):
    # Menghitung jari-jari dari diameter
    jari_jari = diameter / 2
    # Menghitung volume tabung menggunakan rumus volume tabung
    volume_tabung = 3.14 * jari_jari * jari_jari * tinggi
    return volume_tabung

# Program utama
pilihan = 0

while pilihan != 5:
    print("*** PROGRAM TABUNG ***")
    print("1. Masukan Diameter Alas")
    print("2. Masukan Tinggi Tabung")
    print("3. Luas Alas")
    print("4. Volume Tabung")
    print("5. Keluar")

    pilihan = int(input("Pilih menu 1-5: "))

    if pilihan == 1:
        diameter = float(input("Masukkan diameter alas: "))
    elif pilihan == 2:
        tinggi = float(input("Masukkan tinggi tabung: "))
    elif pilihan == 3:
        luas_alas = hitung_luas_alas(diameter)
        print("Luas alas: ", luas_alas)
    elif pilihan == 4:
        volume_tabung = hitung_volume_tabung(diameter, tinggi)
        print("Volume tabung: ", volume_tabung)
    elif pilihan == 5:
        print("Terima kasih sudah menggunakan program ini!")
    else:
        print("Pilihan tidak valid. Silahkan coba lagi.")
       
    # ini comment



