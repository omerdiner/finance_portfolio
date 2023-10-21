import tkinter as tk
import gui.operations as operations
import api.get_prices as get_prices
import gui.user_data_update as user_data_update


class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ana Sayfa")
        self.configure(bg="#E1D3D0")
        self.button_show_user_data = tk.Button(
            self, text="Portföy Görüntüle", command=self.show_user_portfolio, font=("Arial", 15), bd=5, relief=tk.GROOVE, width=50)

        self.button_show_user_data.pack(pady=50, padx=50)

        self.button_user_finance_operations = tk.Button(
            self, text="İşlem Yap", command=self.update_user_finance_data, font=("Arial", 15), bd=5, relief=tk.GROOVE, width=50)

        self.button_user_finance_operations.pack(pady=50, padx=50)

    def show_user_portfolio(self):
        current_price_data = get_prices.get_current_prices()
        portfolio_page = operations.MainInfoGui(current_price_data)
        portfolio_page.main_page()

    def update_user_finance_data(self):
        user_gui = user_data_update.Exchange(tk.Tk())
        user_gui.run()

    def run(self):

        self.geometry("300x300")
        self.mainloop()
