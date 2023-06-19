import PySimpleGUI as sg

# Membuat layout GUI
layout = [[sg.Button('Klik saya!')]]

# Membuat jendela GUI
window = sg.Window('Program Sederhana', layout)

# Membaca inputan pengguna dan menangani event
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Klik saya!':
        print('Tombol diklik!')

# Menutup jendela GUI
window.close()
