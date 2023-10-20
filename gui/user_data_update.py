import tkinter as tk
from tkinter import messagebox
import data.user_data_manager as user_data_manager
import datetime


class Exchange:
    def __init__(self, root):
        self.root = root
        self.root.title("Portföy Yönetimi")
        self.root.geometry("400x500")

        self.stock_button = tk.Button(
            root, text="Hisse işlemleri", command=self.stock_page, width=20, height=5, font=("Arial", 14))
        self.stock_button.pack(pady=20)

        self.gold_button = tk.Button(
            root, text="Altın İşlemleri", command=self.gold_page, width=20, height=5, font=("Arial", 14))
        self.gold_button.pack()

        self.currency_button = tk.Button(
            root, text="Döviz İşlemleri", command=self.currency_page, width=20, height=5, font=("Arial", 14))
        self.currency_button.pack()

    def stock_page(self):
        stock_window = tk.Toplevel(self.root)
        stock_window.title("HİSSE TAKİP")
        stock_window.geometry("600x400")

        stock_data = user_data_manager.get_user_stock_data()

        if stock_data:
            stock_info_frame = tk.Frame(stock_window)
            stock_info_frame.pack(side=tk.LEFT, padx=10, pady=1)

            for index, item in enumerate(stock_data):
                label_text = f"{item['code']} : {item['amount']} Adet"
                label = tk.Label(stock_info_frame,
                                 text=label_text, font=("Arial", 8))
                label.pack(pady=2)
        else:
            no_data_label = tk.Label(
                stock_window, text="Hisse bilgisi yok.", font=("Arial", 14))
            no_data_label.pack(pady=50)

        transaction_frame = tk.Frame(stock_window)
        transaction_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        label_code = tk.Label(transaction_frame, text="Hisse Kodu:")
        label_code.pack()
        entry_code = tk.Entry(transaction_frame, width=20)
        entry_code.pack()

        label_quantity = tk.Label(transaction_frame, text="Adet:")
        label_quantity.pack()
        entry_quantity = tk.Entry(transaction_frame, width=20)
        entry_quantity.pack()

        label_price = tk.Label(transaction_frame, text="Birim fiyat:")
        label_price.pack()
        entry_price = tk.Entry(transaction_frame, width=20)
        entry_price.pack()

        transaction_type = tk.StringVar()
        transaction_type.set("Al")

        radio_buy = tk.Radiobutton(
            transaction_frame, text="Al", variable=transaction_type, value="Buy")
        radio_buy.pack(side=tk.LEFT, padx=10)
        radio_sell = tk.Radiobutton(
            transaction_frame, text="Sat", variable=transaction_type, value="Sell")
        radio_sell.pack(side=tk.LEFT, padx=10)

        def take_and_check_input():
            code = entry_code.get()
            quantity = entry_quantity.get()
            price = entry_price.get()

            if code == "" or quantity == "" or price == "":
                messagebox.showerror("Hata", "Tüm alanları doldur.")
                return False

            if not quantity.isdigit():
                messagebox.showerror("Hata", "Miktar sayı olmalıdır.")
                return False

            if not price.isdigit():
                messagebox.showerror(
                    "Hata", "Birim fiyat bilgisi sayı olmalıdır.")
                return False

            return {"code": code, "quantity": quantity, "price": price, "transaction_type": transaction_type.get()}

        def perform_transaction():
            transaction_data = take_and_check_input()
            if not transaction_data:
                messagebox.showerror("Hata", "Girilen bilgileri gözden geçir.")
                return

            if user_data_manager.stock_operation(transaction_data):
                transaction_history = {"date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "stock": transaction_data["code"], "amount": int(transaction_data["quantity"]), "price": int(transaction_data["price"]),
                                       "total": int(transaction_data["price"]) * int(transaction_data["quantity"]), "type": transaction_data["transaction_type"], "note": ""}
                user_data_manager.update_stock_history(transaction_history)
                messagebox.showinfo("Başarılı", "İşlem başarılı.")
                stock_window.destroy()
            else:
                messagebox.showerror("Hata", "İşlem başarısız.")

        transaction_button = tk.Button(
            transaction_frame, text="İşlemi gerçekleştir", command=perform_transaction)
        transaction_button.pack(pady=10)

    def gold_page(self):
        gold_window = tk.Toplevel(self.root)
        gold_window.title("Gold Tracker")
        gold_window.geometry("600x400")

        pass

    def currency_page(self):
        currency_window = tk.Toplevel(self.root)
        currency_window.title("Currency Tracker")
        currency_window.geometry("600x400")

        pass

    def run(self):
        self.root.mainloop()
