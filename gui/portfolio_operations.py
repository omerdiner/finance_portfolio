import matplotlib.pyplot as plt
import gui.stock_operations as stock_operations
import gui.currency_operations as currency_operations
import gui.gold_operations as gold_operations
import gui.crypto_operations as crypto_operations


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

    def get_total_of_cryptos(self):
        crypto_operation = crypto_operations.CryptoOperations(
            self.current_prices)
        crypto_data = crypto_operation.all_crypto_data()
        total_crypto_amount = sum([i[1] for i in crypto_data.values()])
        return total_crypto_amount

    def show_portfolio(self):
        gold_price = self.get_total_of_golds()
        stock_price = self.get_total_of_stocks()
        currency_price = self.get_total_of_currencies()
        crypto_price = self.get_total_of_cryptos()
        total_portfolio_value = gold_price + stock_price + currency_price+crypto_price

        colors = ['#FFD700', '#FF4500', '#00CED1', '#42F545']
        labels = ['Altın', 'Hisse Senetleri', 'Döviz', 'Kripto']
        sizes = [gold_price, stock_price, currency_price, crypto_price]

        plt.figure(figsize=(8, 8))
        plt.text(0, -1.2, f'Altın: {gold_price:.2f} TL',
                 ha='center', va='center', fontsize=12, color='#FFD700')
        plt.text(0, -1.35, f'Hisse senetleri: {stock_price:.2f} TL',
                 ha='center', va='center', fontsize=12, color='#FF4500')
        plt.text(0, -1.50, f'Dövizler: {currency_price:.2f} TL',
                 ha='center', va='center', fontsize=12, color='#00CED1')
        plt.text(0, -1.65, f'Kripto: {crypto_price:.2f} TL',
                 ha='center', va='center', fontsize=12, color='#42F545')

        plt.text(0, -1.8, f'Toplam portföy değeri: {total_portfolio_value:.2f} TL',
                 ha='center', va='center', fontsize=14, color='black')

        plt.pie(sizes, labels=labels, autopct='%1.1f%%',
                startangle=140, colors=colors)

        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        plt.axis('equal')
        plt.gca().set_facecolor('#F5F5DC')
        plt.tight_layout()

        plt.show()
