import matplotlib.pyplot as plt
import data.data_manager as data_manager
import gui.stock_operations as stock_operations
import gui.currency_operations as currency_operations
import gui.gold_operations as gold_operations


class PortfolioOperations():
    def __init__(self, current_price_data):
        self.current_prices = current_price_data

    def get_total_of_stocks(self):
        stock_operation = stock_operations.StockOperations(
            self.current_prices)
        stock_data = stock_operation.all_stock_data()
        total_stock_amount = sum([i[1] for i in stock_data.values()])
        return total_stock_amount

    def get_total_of_currencies(self):
        currency_operation = currency_operations.CurrencyOperations(
            self.current_prices)
        currency_data = currency_operation.all_currency_data()
        total_currency_amount = sum([i[1] for i in currency_data.values()])
        return total_currency_amount

    def get_total_of_golds(self):
        gold_operation = gold_operations.GoldOperations(
            self.current_prices)
        gold_data = gold_operation.all_gold_data()
        total_gold_amount = sum([i[1] for i in gold_data.values()])
        return total_gold_amount

    def show_portfolio(self):
        gold_price = self.get_total_of_golds()
        stock_price = self.get_total_of_stocks()
        currency_price = self.get_total_of_currencies()
        total_portfolio_value = gold_price + stock_price + currency_price

        colors = ['#FFD700', '#FF4500', '#00CED1']
        labels = ['Altın', 'Hisse Senetleri', 'Döviz']
        sizes = [gold_price, stock_price, currency_price]

        plt.figure(figsize=(8, 8))
        plt.text(0, -1.3, f'Altın: {gold_price:.2f} TL',
                 ha='center', va='center', fontsize=12, color='#FFD700')
        plt.text(0, -1.45, f'Hisse senetleri: {stock_price:.2f} TL',
                 ha='center', va='center', fontsize=12, color='#FF4500')
        plt.text(0, -1.6, f'Dövizler: {currency_price:.2f} TL',
                 ha='center', va='center', fontsize=12, color='#00CED1')
        plt.text(0, -1.8, f'Toplam portföy değeri: {total_portfolio_value:.2f} TL',
                 ha='center', va='center', fontsize=14, color='black')

        plt.pie(sizes, labels=labels, autopct='%1.1f%%',
                startangle=140, colors=colors)

        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        plt.title('Portföy', fontsize=16)
        plt.axis('equal')
        plt.gca().set_facecolor('#F5F5DC')
        plt.tight_layout()

        plt.show()
