import PySimpleGUI as sg

# Membuat layout GUI
layout = [[sg.Text('Masukkan teks di bawah ini:')],
        [sg.Multiline()],
        [sg.Button('Simpan'), sg.Button('Batal')]]

# Membuat jendela GUI
window = sg.Window('Aplikasi Simpan Teks', layout)

# Membaca inputan pengguna dan menangani event
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Batal':
        break
    if event == 'Simpan':
        # Mengambil teks yang dimasukkan pengguna
        text = values[0]

        # Menuliskan teks ke dalam file
        with open('teks.txt', 'w') as file:
            file.write(text)

        # Menampilkan pesan konfirmasi
        sg.popup('Teks berhasil disimpan ke dalam file!')

# Menutup jendela GUI
window.close()

