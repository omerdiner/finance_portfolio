import matplotlib.pyplot as plt
import data.data_manager as data_manager
import data.user_data_manager as user_data_manager


class CurrencyOperations:

    def __init__(self):
        self.current_prices = data_manager.get_current_prices()[0]

    def calculate_total_amount_for_a_currency(self, currency_code, amount):
        for i in range(len(self.current_prices)):
            if self.current_prices[i]["code"] == currency_code:
                currency_price = self.current_prices[i]["buying"]
                break
        total_amount = currency_price * amount
        return total_amount

    #  "code": [amount, total_amount] şeklinde bir dictionary listesi döndürür

    def all_currency_data(self):
        currency_data = user_data_manager.get_user_currency_data()
        total_currency_data = {}
        for i in range(len(currency_data)):
            currency_code = currency_data[i]["code"]
            currency_amount = currency_data[i]["amount"]
            total_amount = self.calculate_total_amount_for_a_currency(
                currency_code, currency_amount)
            total_currency_data[currency_code] = [
                currency_amount, total_amount]
        return total_currency_data

    def show_currency_data(self):
        total_currency_data = self.all_currency_data()
        currency_codes = list(total_currency_data.keys())
        currency_amounts = [i[0] for i in total_currency_data.values()]
        currency_total_values = [i[1] for i in total_currency_data.values()]

        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)

        bars = plt.bar(currency_codes, currency_amounts, color='skyblue')
        plt.xlabel('Döviz Kodları')
        plt.ylabel('Adet')
        plt.title('Döviz Adetleri')

        for bar, amount in zip(bars, currency_amounts):
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval,
                     str(amount), ha='center', va='bottom')

        plt.subplot(1, 2, 2)
        plt.pie(currency_total_values, labels=currency_codes, autopct='%1.1f%%',
                startangle=140, colors=['yellowgreen', 'coral', 'lightskyblue'])
        plt.axis('equal')  # Daireyi dairesel yapar
        plt.title('Döviz Oransal Dağılımı')

        # Dövizlerin toplam miktarlarını metin olarak gösterme
        total = sum(currency_total_values)
        textstr = '\n'.join(f'{code}: {total_value:.1f} TL' for code, total_value in zip(
            currency_codes, currency_total_values))
        textstr += f'\nToplam: {total:.1f} TL'
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        plt.figtext(0.95, 0.01, textstr, bbox=props,
                    verticalalignment='bottom', horizontalalignment='right')

        plt.suptitle('Dövizlerim', fontsize=16, fontweight='bold')

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
