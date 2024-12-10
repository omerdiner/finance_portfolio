import matplotlib.pyplot as plt
import data.user_data_manager as user_data_manager
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk


class StockOperations:
    def __init__(self, current_price_data):
        self.current_prices = current_price_data[1]

    def calculate_total_amount_for_a_stock(self, stock_code, amount):
        for i in range(len(self.current_prices)):
            if self.current_prices[i]["code"] == stock_code:
                stock_price = self.current_prices[i]["lastprice"]
                break
        total_amount = stock_price * amount
        return total_amount

    def all_stock_data(self):
        stock_data = user_data_manager.get_user_stock_data()
        total_stock_data = {}
        for i in range(len(stock_data)):
            stock_code = stock_data[i]["code"]
            stock_amount = stock_data[i]["amount"]
            total_amount = self.calculate_total_amount_for_a_stock(
                stock_code, stock_amount)
            total_stock_data[stock_code] = [
                stock_amount, total_amount]
        return total_stock_data

    def show_stock_data(self):
        root = tk.Tk()
        root.title("Hisse Senedi Portföyü")

        frame_left = ttk.Frame(root)
        frame_left.pack(side=tk.LEFT, padx=10, pady=10)

        table = ttk.Treeview(frame_left, columns=(
            "Hisse Kodu", "Adet", "Toplam Fiyat"), show="headings")
        table.heading("Hisse Kodu", text="Hisse Kodu")
        table.heading("Adet", text="Adet")
        table.heading("Toplam Fiyat", text="Toplam Fiyat")
        table.pack(side=tk.TOP, fill=tk.Y)

        total_stock_data = self.all_stock_data()
        #2.12.2024 tarihinden itibaren verilerin ekranda sıralı şekilde gözükmesi için aşağıdaki 10 satır kodu yazdım.
        sorted_total_stock_data = dict(
            sorted(total_stock_data.items(), key=lambda item: item[1][1], reverse=True))
        
        stock_codes = list(sorted_total_stock_data.keys())
        stock_amounts = [sorted_total_stock_data[code][0]
                         for code in stock_codes]
        stock_total_values = [sorted_total_stock_data[code][1]
                              for code in stock_codes]
        

        for i in range(len(stock_codes)):
            formatted_total_value = "{:.2f}".format(stock_total_values[i])
            table.insert("", "end", values=(
                stock_codes[i], stock_amounts[i], formatted_total_value))

        total_value = sum(stock_total_values)
        total_value_label = tk.Label(
            frame_left, text="Toplam Değer: {:.2f}".format(total_value))
        total_value_label.pack(side=tk.BOTTOM)
        total_value_label.config(font=("Courier", 20))

        frame_right = ttk.Frame(root)
        frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

        fig, ax = plt.subplots()
        ax.pie(stock_total_values, labels=stock_codes,
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
