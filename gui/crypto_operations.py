import matplotlib.pyplot as plt
import data.user_data_manager as user_data_manager
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk


class CryptoOperations:
    def __init__(self, current_price_data):
        self.current_prices = current_price_data[3]

    def calculate_total_amount_for_a_crypto(self, crypto_code, amount):
        # api does not return data for these cryptos
        unavailable_cryptos_from_api = {'HOT': 0.1092,'CHZ':3.51}

        crypto_price = 0
        for i in range(len(self.current_prices)):
            if self.current_prices[i]["symbol"] == crypto_code:
                crypto_price = self.current_prices[i]["quote"]["TRY"]["price"]
                break

        if crypto_price == 0:
            crypto_price = unavailable_cryptos_from_api[crypto_code]
        total_amount = crypto_price * amount

        return total_amount

    def all_crypto_data(self):
        crypto_data = user_data_manager.get_user_crypto_data()
        total_crypto_data = {}
        for i in range(len(crypto_data)):
            crypto_code = crypto_data[i]["symbol"]
            crypto_amount = crypto_data[i]["amount"]
            total_amount = self.calculate_total_amount_for_a_crypto(
                crypto_code, crypto_amount)
            total_crypto_data[crypto_code] = [
                crypto_amount, total_amount]
        return total_crypto_data

    def show_crypto_data(self):
        root = tk.Tk()
        root.title("Kripto Para Portföyü")

        frame_left = ttk.Frame(root)
        frame_left.pack(side=tk.LEFT, padx=10, pady=10)

        table = ttk.Treeview(frame_left, columns=(
            "Sembol", "Adet", "Toplam Fiyat"), show="headings")
        table.heading("Sembol", text="Sembol")
        table.heading("Adet", text="Adet")
        table.heading("Toplam Fiyat", text="Toplam Fiyat")
        table.pack(side=tk.TOP, fill=tk.Y)

        total_crypto_data = self.all_crypto_data()
        
        # SORT CRYPTO DATA BY TOTAL VALUE
        total_crypto_data = dict(sorted(total_crypto_data.items(), key=lambda x: x[1][1], reverse=True))
        
        crypto_codes = list(total_crypto_data.keys())
        crypto_amounts = [i[0] for i in total_crypto_data.values()]
        crypto_total_values = [i[1] for i in total_crypto_data.values()]

        for i in range(len(crypto_codes)):
            formatted_total_value = "{:.2f}".format(crypto_total_values[i])
            table.insert("", "end", values=(
                crypto_codes[i], crypto_amounts[i], formatted_total_value))

        total_value = sum(crypto_total_values)
        total_value_label = tk.Label(
            frame_left, text="Toplam Değer: {:.2f}".format(total_value))
        total_value_label.pack(side=tk.BOTTOM)
        total_value_label.config(font=("Courier", 20))

        frame_right = ttk.Frame(root)
        frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

        fig, ax = plt.subplots()
        ax.pie(crypto_total_values, labels=crypto_codes,
               autopct='%1.1f%%', startangle=90)
        i = 0
        for text in ax.texts:
            if i % 2 == 1:
                t = text.get_text()
                try:
                    ratio = float(t[:-1])
                except ValueError:
                    ratio = 5

                if ratio < 5:
                    text.set_fontsize(5)
                elif ratio < 7:
                    text.set_fontsize(6)
                elif ratio < 9:
                    text.set_fontsize(7)
                elif ratio < 10:
                    text.set_fontsize(8)
                else:
                    text.set_fontsize(10)
            else:
                text.set_fontsize(7)
            i += 1

        ax.axis('equal')
        canvas = FigureCanvasTkAgg(fig, master=frame_right)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        root.mainloop()
