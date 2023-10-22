import tkinter as tk
from tkinter import messagebox
import data.user_data_manager as user_data_manager
import datetime
import tkinter.ttk as ttk


class Exchange:
    def __init__(self, root):
        self.root = root
        self.root.title("Portföy Yönetimi")
        self.root.geometry("400x500")

        self.stock_button = tk.Button(
            root, text="Hisse işlemleri", command=self.stock_page, width=20, height=5, font=("Arial", 14))
        self.stock_button.pack(pady=10)

        self.stock_button.config(relief=tk.RAISED, borderwidth=5)

        self.gold_button = tk.Button(
            root, text="Altın İşlemleri", command=self.gold_page, width=20, height=5, font=("Arial", 14))
        self.gold_button.pack(pady=10)
        self.gold_button.config(relief=tk.RAISED, borderwidth=5)

        self.currency_button = tk.Button(
            root, text="Döviz İşlemleri", command=self.currency_page, width=20, height=5, font=("Arial", 14))
        self.currency_button.pack(pady=10)
        self.currency_button.config(relief=tk.RAISED, borderwidth=5)

    def stock_page(self):
        stock_window = tk.Toplevel(self.root)
        stock_window.title("HİSSE TAKİP")
        stock_window.geometry("600x400")
        stock_window.configure(bg="light blue")

        stock_data = user_data_manager.get_user_stock_data()

        if stock_data:
            stock_info_frame = tk.Frame(stock_window)
            stock_info_frame.pack(side=tk.LEFT)

            columns = ("Hisse Kodu", "Adet")
            tree = ttk.Treeview(
                stock_info_frame, columns=columns, show="headings")
            tree.heading("Hisse Kodu", text="Hisse Kodu")
            tree.heading("Adet", text="Adet")

            scrollbar = ttk.Scrollbar(
                stock_info_frame, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)

            tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            for row in stock_data:
                tree.insert("", "end", values=(row["code"], row["amount"]))

        else:
            no_data_label = tk.Label(
                stock_window, text="Hisse bilgisi yok.", font=("Arial", 14))
            no_data_label.pack(pady=50)

        transaction_frame = tk.Frame(stock_window)
        transaction_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        label_code = tk.Label(transaction_frame, text="Hisse Kodu")
        label_code.pack()
        entry_code = tk.Entry(transaction_frame, width=20)
        entry_code.pack()

        label_quantity = tk.Label(transaction_frame, text="Adet")
        label_quantity.pack()
        entry_quantity = tk.Entry(transaction_frame, width=20)
        entry_quantity.pack()

        label_price = tk.Label(transaction_frame, text="Birim fiyat")
        label_price.pack()
        entry_price = tk.Entry(transaction_frame, width=20)
        entry_price.pack()

        label_type = tk.Label(transaction_frame, text="Al/Sat")
        label_type.pack()
        transaction_type = tk.Entry(transaction_frame, width=20)
        transaction_type.insert(0, "AL")
        transaction_type.pack()

        def take_and_check_input():
            code = entry_code.get().upper()
            quantity = entry_quantity.get()
            price = entry_price.get()
            buy_or_sell = transaction_type.get().strip().upper()

            if code == "" or quantity == "" or price == "" or buy_or_sell == "":
                messagebox.showerror("Hata", "Tüm alanları doldur.")
                return False

            if not quantity.isdigit():
                messagebox.showerror("Hata", "Miktar sayı olmalıdır.")
                return False

            try:
                price = float(price)
            except:
                messagebox.showerror(
                    "Hata", "Birim fiyat bilgisi sayı olmalıdır.")
                return False

            if buy_or_sell != "AL" and buy_or_sell != "SAT":
                messagebox.showerror("Hata", "Al/Sat alanı bilgisi yanlış.")
                return False

            buy_or_sell = "Sell" if buy_or_sell == "SAT" else "Buy"

            return {"code": code, "quantity": quantity, "price": price, "transaction_type": buy_or_sell}

        def perform_transaction():
            transaction_data = take_and_check_input()
            if not transaction_data:
                messagebox.showerror("Hata", "Girilen bilgileri gözden geçir.")
                return

            if user_data_manager.stock_operation(transaction_data):
                transaction_history = {"date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "stock": transaction_data["code"], "amount": int(transaction_data["quantity"]), "price": float(transaction_data["price"]),
                                       "total": float(transaction_data["price"]) * int(transaction_data["quantity"]), "type": transaction_data["transaction_type"], "note": ""}
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
        gold_window.configure(bg="gold")

        gold_data = user_data_manager.get_user_gold_data()

        if gold_data:

            gold_info_frame = tk.Frame(gold_window)
            gold_info_frame.pack(side=tk.LEFT, padx=50, pady=1)

            for index, item in enumerate(gold_data):
                label_text = f"{item['name']} : {item['amount']:0.2f}"
                label = tk.Label(
                    gold_info_frame, text=label_text, font=("Arial", 8))
                label.pack(pady=1)
        else:
            no_data_label = tk.Label(
                gold_window, text="Altın bilgisi yok.", font=("Arial", 14))
            no_data_label.pack(pady=50)

        transaction_frame = tk.Frame(gold_window)
        transaction_frame.pack(side=tk.RIGHT, padx=50, pady=10)

        label_name = tk.Label(transaction_frame, text="Altın Adı")
        label_name.pack()
        entry_name = tk.Entry(transaction_frame, width=20)
        entry_name.pack()

        label_quantity = tk.Label(transaction_frame, text="Adet")
        label_quantity.pack()
        entry_quantity = tk.Entry(transaction_frame, width=20)
        entry_quantity.pack()

        label_price = tk.Label(transaction_frame, text="Birim fiyat")
        label_price.pack()
        entry_price = tk.Entry(transaction_frame, width=20)
        entry_price.pack()

        label_type = tk.Label(transaction_frame, text="Al/Sat")
        label_type.pack()
        transaction_type = tk.Entry(transaction_frame, width=20)
        transaction_type.insert(0, "AL")
        transaction_type.pack()

        def take_and_check_input():

            name = entry_name.get()
            quantity = entry_quantity.get()
            price = entry_price.get()
            buy_or_sell = transaction_type.get().strip().upper()

            if name == "" or quantity == "" or price == "" or buy_or_sell == "":
                messagebox.showerror("Hata", "Tüm alanları doldur.")
                return False

            if buy_or_sell != "AL" and buy_or_sell != "SAT":
                messagebox.showerror("Hata", "Al/Sat alanı bilgisi yanlış.")
                return False

            try:
                quantity = float(quantity)
            except:
                messagebox.showerror("Hata", "Miktar sayı olmalıdır.")
                return False

            try:
                price = float(price)
            except:
                messagebox.showerror(
                    "Hata", "Birim fiyat bilgisi sayı olmalıdır.")
                return False

            buy_or_sell = "Sell" if buy_or_sell == "SAT" else "Buy"

            return {"name": name, "quantity": quantity, "price": price, "transaction_type": buy_or_sell}

        def perform_transaction():
            transaction_data = take_and_check_input()
            if not transaction_data:
                messagebox.showerror("Hata", "Girilen bilgileri gözden geçir.")
                return

            if user_data_manager.gold_operation(transaction_data):
                transaction_history = {"date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "gold": transaction_data["name"], "amount": float(transaction_data["quantity"]), "price": float(
                    transaction_data["price"]), "total": float(transaction_data["price"])*float(transaction_data["quantity"]), "type": transaction_data["transaction_type"], "note": ""}
                user_data_manager.update_gold_history(transaction_history)
                messagebox.showinfo("Başarılı", "İşlem başarılı.")
                gold_window.destroy()
            else:
                messagebox.showerror("Hata", "İşlem başarısız.")

        transaction_button = tk.Button(
            transaction_frame, text="İşlemi gerçekleştir", command=perform_transaction)
        transaction_button.pack(pady=10)

    def currency_page(self):
        currency_window = tk.Toplevel(self.root)
        currency_window.title("DÖVİZ TAKİP")
        currency_window.geometry("600x400")
        currency_window.configure(bg="light green")

        currency_data = user_data_manager.get_user_currency_data()

        if currency_data:
            currency_info_frame = tk.Frame(currency_window)
            currency_info_frame.pack(side=tk.LEFT, padx=50, pady=1)

            for index, item in enumerate(currency_data):
                label_text = f"{item['code']} : {item['amount']} Adet"
                label = tk.Label(currency_info_frame,
                                 text=label_text, font=("Arial", 8))
                label.pack(pady=1)
        else:
            no_data_label = tk.Label(
                currency_window, text="Döviz bilgisi yok.", font=("Arial", 14))
            no_data_label.pack(pady=50)

        transaction_frame = tk.Frame(currency_window)
        transaction_frame.pack(side=tk.RIGHT, padx=50, pady=10)

        label_code = tk.Label(transaction_frame, text="Döviz Kodu")
        label_code.pack()
        entry_code = tk.Entry(transaction_frame, width=20)
        entry_code.pack()

        label_quantity = tk.Label(transaction_frame, text="Adet")
        label_quantity.pack()

        entry_quantity = tk.Entry(transaction_frame, width=20)
        entry_quantity.pack()

        label_price = tk.Label(transaction_frame, text="Birim fiyat")
        label_price.pack()

        entry_price = tk.Entry(transaction_frame, width=20)
        entry_price.pack()

        transaction_type = tk.StringVar()
        transaction_type.set("Buy")

        label_type = tk.Label(transaction_frame, text="Al/Sat")
        label_type.pack()
        transaction_type = tk.Entry(transaction_frame, width=20)
        transaction_type.insert(0, "AL")
        transaction_type.pack()

        def take_and_check_input():
            code = entry_code.get().upper()
            quantity = entry_quantity.get()
            price = entry_price.get()
            buy_or_sell = transaction_type.get().strip().upper()

            if code == "" or quantity == "" or price == "" or buy_or_sell == "":
                messagebox.showerror("Hata", "Tüm alanları doldur.")
                return False

            if not quantity.isdigit():
                messagebox.showerror("Hata", "Miktar sayı olmalıdır.")
                return False

            try:
                price = float(price)
            except:
                messagebox.showerror(
                    "Hata", "Birim fiyat bilgisi sayı olmalıdır.")
                return False
            if buy_or_sell != "AL" and buy_or_sell != "SAT":
                messagebox.showerror("Hata", "Al/Sat alanı bilgisi yanlış.")
                return False

            buy_or_sell = "Sell" if buy_or_sell == "SAT" else "Buy"
            return {"code": code, "quantity": quantity, "price": price, "transaction_type": buy_or_sell}

        def perform_transaction():

            transaction_data = take_and_check_input()
            if not transaction_data:
                messagebox.showerror("Hata", "Girilen bilgileri gözden geçir.")
                return

            if user_data_manager.currency_operation(transaction_data):
                transaction_history = {"date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "currency": transaction_data["code"], "amount": int(transaction_data["quantity"]), "price": float(transaction_data["price"]),
                                       "total": float(transaction_data["price"]) * int(transaction_data["quantity"]), "type": transaction_data["transaction_type"], "note": ""}
                user_data_manager.update_currency_history(transaction_history)
                messagebox.showinfo("Başarılı", "İşlem başarılı.")
                currency_window.destroy()
            else:
                messagebox.showerror("Hata", "İşlem başarısız.")

        transaction_button = tk.Button(
            transaction_frame, text="İşlemi gerçekleştir", command=perform_transaction)
        transaction_button.pack(pady=10)

    def run(self):
        self.root.mainloop()
