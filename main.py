import api.get_prices as get_prices
import data.data_manager as data_manager
import data.user_data_manager as user_data_manager
import tkinter as tk
import gui.operations as operations
import gui.currency_operations as currency_operations
import gui.stock_operations as stock_operations
import gui.gold_operations as gold_operations
import matplotlib.pyplot as plt
#akbank = data_manager.get_all_data_for_a_stock("AKBNK")
#usd = data_manager.get_all_data_for_a_currency("USD")
#gold = data_manager.get_all_data_for_gold()


def main():
    # data_manager.add_new_financial_data()

    currency_chart = currency_operations.CurrencyOperations()
    currency_chart.show_currency_data()

    stock_Chart = stock_operations.StockOperations()
    stock_Chart.show_stock_data()

    gold_chart = gold_operations.GoldOperations()
    gold_chart.show_gold_data()


if __name__ == "__main__":
    main()
