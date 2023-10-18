import matplotlib.pyplot as plt
import data.data_manager as data_manager
import data.user_data_manager as user_data_manager


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
        total_stock_data = self.all_stock_data()
        stock_codes = list(total_stock_data.keys())
        stock_amounts = [i[0] for i in total_stock_data.values()]
        stock_total_values = [i[1] for i in total_stock_data.values()]

        total_portfolio_value = sum(stock_total_values)

        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        cell_text = []
        for i in range(len(stock_codes)):
            cell_text.append(
                [stock_codes[i], stock_amounts[i], stock_total_values[i]])

        table = plt.table(cellText=cell_text, colLabels=["Hisse Kodu", "Adet", "Toplam Tutar (TL)"],
                          cellLoc='center', loc='center', colColours=['#f3f3f3']*3, cellColours=[['#f9f9f9', '#f9f9f9', '#f9f9f9']]*len(stock_codes))
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.auto_set_column_width(col=list(range(3)))
        table.scale(1, 2)

        plt.title("Hisse Senedi Bilgileri")

        plt.subplot(1, 2, 2)
        plt.axis('equal')
        plt.rcParams['font.size'] = 12
        plt.pie(stock_total_values, labels=stock_codes,
                autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
        plt.title("Hisselerin Oransal Dağılımı")

        plt.figtext(
            0.5, 0.02, f"Toplam Hisse Senedi Değeri: {total_portfolio_value} TL", ha='center', fontsize=14)

        plt.subplot(1, 2, 1)
        plt.gca().set_facecolor('#f2f2f2')

        plt.subplot(1, 2, 2)
        plt.gca().set_facecolor('#f2f2f2')

        plt.subplots_adjust(wspace=0.4)

        plt.show()
