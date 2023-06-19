for j in range(1, 5, 1):
    print(j)

for i in range(1, 4):
    print("i: ", 2**i)


list1 = [2, 3, 7, 2, 7, 8]
list2 = []

for item in list1:
    if item not in list2:
        list2.append(item)
    print(list2)


# Buatlah untuk meminta masukan dan menghilangkan tanda "-" dari masukan
# tersebut dan menampilkan kembali masukan tersebut.

# Masukan: 0812-1234-5678
# Keluaran: 081212345678

# Masukan: 0812-1234-5678

masukan = input("Masukkan nomor telepon: ")
KELUARAN = ""

for i in range(len(masukan)):
    if masukan[i] != "-":
        KELUARAN += masukan[i]
print(KELUARAN)

# Buatlah program untuk menjumlahkan nilai 1 + 1/2 + 1/3 + ... + 1/100 dengan
# hasil 5 digit di belakang koma.

# Keluaran: 5.18738

# Keluaran: 5.18738

jumlah = 0
for i in range(1, 101):
    jumlah += 1/i
print(round(jumlah, 5))
