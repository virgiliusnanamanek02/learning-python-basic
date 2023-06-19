"""Data Analyzer"""
import tkinter as tk  # Mengimport tkinter
from collections import Counter  # Mengimport Counter

# pylint: disable=import-error
import matplotlib.pyplot as plt  # Mengimport matplotlib


class DataAnalyzerApp:  # Membuat class DataAnalyzerApp
    """Data Analyzer App"""

    def __init__(self, master):  # Membuat method __init__
        self.master = master  # Mengassign variabel master
        self.master.title("Data Analyzer")  # Menampilkan judul "Data Analyzer"

        self.data_label = tk.Label(
            self.master, text="Masukkan data (pisahkan dengan spasi):")
        self.data_label.pack()

        self.data_entry = tk.Entry(self.master, width=50)
        self.data_entry.pack()

        self.analyze_button = tk.Button(
            self.master, text="Analyze", command=self.analyze_data)
        self.analyze_button.pack()

        self.result_label = tk.Label(self.master, text="Hasil Analisis:")
        self.result_label.pack()

        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.pack()

        self.plot_button = tk.Button(
            self.master, text="Plot Chart", command=self.plot_chart)
        self.plot_button.pack()

    def analyze_data(self):
        """Analyze data"""
        data = self.data_entry.get().split()
        counter = Counter(data)
        most_common = counter.most_common(10)

        result = ""
        for item, count in most_common:
            result += f"{item}: {count}\n"

        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, result)

    def plot_chart(self):
        """Plot chart"""
        data = self.data_entry.get().split()
        counter = Counter(data)
        most_common = counter.most_common(10)

        labels = [item[0] for item in most_common]
        values = [item[1] for item in most_common]

        plt.bar(labels, values)
        plt.xlabel('Data')
        plt.ylabel('Count')
        plt.title('Top 10 Most Common Data')
        plt.xticks(rotation=45)

        plt.show()


root = tk.Tk()
app = DataAnalyzerApp(root)
root.mainloop()
