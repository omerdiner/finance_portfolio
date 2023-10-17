import api.get_prices as get_prices
import data.data_manager as data_manager
import data.user_data_manager as user_data_manager
import tkinter as tk
import gui.operations as operations
import gui.currency_operations as currency_operations
import gui.stock_operations as stock_operations
import gui.gold_operations as gold_operations
import matplotlib.pyplot as plt


def main():
    # data_manager.add_new_financial_data()
    '''
    currency_chart = currency_operations.CurrencyOperations()
    currency_chart.show_currency_data()

    stock_Chart = stock_operations.StockOperations()
    stock_Chart.show_stock_data()

    gold_chart = gold_operations.GoldOperations()
    gold_chart.show_gold_data()
    '''
    user_gold_data = user_data_manager.get_user_gold_data()
    user_stock_data = user_data_manager.get_user_stock_data()
    user_currency_data = user_data_manager.get_user_currency_data()

    thyao = data_manager.get_all_data_for_a_stock("THYAO")
    usd = data_manager.get_all_data_for_a_currency("USD")
    gold = data_manager.get_all_data_for_gold("Gram Altın")

    print(len(thyao))
    print(thyao)
    print(len(usd))
    print("----------------")
    print(usd)
    print(len(gold))
    print("----------------")
    print(gold)
    print("----------------")
    print(user_gold_data)
    print("----------------")
    print(user_stock_data)
    print("----------------")
    print(user_currency_data)


if __name__ == "__main__":
    main()
