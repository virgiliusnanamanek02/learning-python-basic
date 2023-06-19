# pylint: disable=import-error
import matplotlib.pyplot as plt
import tkinter as tk


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bar Chart")
        self.window.geometry("500x500")

        # Get data
        data = self.get_data()

        # Sort data by value
        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

        # Get top 10 data
        top_data = dict(sorted_data[:10])

        # Create bar chart
        plt.bar(top_data.keys(), top_data.values())
        plt.xticks(rotation=90)
        plt.xlabel("Data")
        plt.ylabel("Count")
        plt.title("Top 10 Data")

        # Embed bar chart in Tkinter window
        canvas = plt.gcf().canvas
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.window.mainloop()

    def get_data(self):
        # Code to get data from file or database
        # Here, we use sample data
        data = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "A", "B", "C", "D", "E", "F", "G", "H", "I", "A", "B", "C", "D", "E", "F", "G",
                "H", "A", "B", "C", "D", "E", "F", "G", "A", "B", "C", "D", "E", "F", "A", "B", "C", "D", "E", "A", "B", "C", "D", "A", "B", "C", "A", "B"]
        data_dict = {}
        for d in data:
            if d in data_dict:
                data_dict[d] += 1
            else:
                data_dict[d] = 1
        return data_dict


if __name__ == "__main__":
    gui = GUI()
