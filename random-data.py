import random
import string

n = int(input("How many numbers do you want to generate? "))


def generate_random_letters():
    letters = []
    for _ in range(n):
        letters.append(random.choice(string.ascii_lowercase))
    return letters


def count_selected_letter(letters, selected_letter):
    count = 0
    for letter in letters:
        if letter == selected_letter:
            count += 1
    return count


random_letters = generate_random_letters()

# Tampilkan huruf-huruf acak
print("Huruf-huruf acak:", random_letters)

# Menghitung jumlah huruf yang dipilih (contoh: 'a')
selected_letter = input("Pilih huruf: ")
count = count_selected_letter(random_letters, selected_letter)

# Menampilkan hasil
print(f"Jumlah huruf '{selected_letter}' yang dipilih: {count}")
