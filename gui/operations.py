import tkinter as tk
import gui.currency_operations as currency_operations
import gui.gold_operations as gold_operations
import gui.portfolio_operations as portfolio_operations
import gui.stock_operations as stock_operations
import data.data_manager as data_manager


class MainInfoGui:

    def __init__(self, current_price_data):
        self.gold_gui = gold_operations.GoldOperations(current_price_data)
        self.stock_gui = stock_operations.StockOperations(current_price_data)
        self.currency_gui = currency_operations.CurrencyOperations(
            current_price_data)
        self.portfolio_gui = portfolio_operations.PortfolioOperations(
            current_price_data)

    def main_page(self):
        self.main_window = tk.Tk()
        self.main_window.title("Finansal Portföy")
        self.main_window.geometry("600x600")
        self.main_window.configure(background="light blue")
        self.main_window.resizable(False, False)

        # Butonları içeren bir çerçeve oluştur
        button_frame = tk.Frame(self.main_window, bg="light blue")
        button_frame.pack(side=tk.TOP, padx=10, pady=5)

        tk.Button(button_frame, text="Altın", command=self.gold_gui.show_gold_data, width=20, height=5).pack(
            side=tk.LEFT, padx=10, pady=10)
        tk.Button(button_frame, text="Hisse Senetleri", command=self.stock_gui.show_stock_data, width=20, height=5).pack(
            side=tk.LEFT, padx=10, pady=10)
        tk.Button(button_frame, text="Döviz", command=self.currency_gui.show_currency_data, width=20, height=5).pack(
            side=tk.LEFT, padx=10, pady=10)
        tk.Button(button_frame, text="Portföy", command=self.portfolio_gui.show_portfolio, width=20, height=5).pack(
            side=tk.LEFT, padx=10, pady=10)

        tk.Button(self.main_window, text="Anlık piyasa bilgisini kaydet", command=data_manager.add_new_financial_data, width=20, height=5).pack(
            side=tk.BOTTOM, padx=10, pady=10)

        self.main_window.mainloop()
