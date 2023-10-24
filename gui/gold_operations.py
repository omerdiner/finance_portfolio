import matplotlib.pyplot as plt
import data.data_manager as data_manager
import data.user_data_manager as user_data_manager


class GoldOperations:
    def __init__(self, current_price_data):
        self.current_prices = current_price_data[2]

    def calculate_total_amount_for_gold(self, amount):
        gold_price = self.current_prices[0]["buying"]*1000.0
        total_amount = gold_price * amount
        return total_amount

    def all_gold_data(self):
        gold_data = user_data_manager.get_user_gold_data()
        total_gold_data = {}
        for i in range(len(gold_data)):
            gold_type = gold_data[i]["name"]
            gold_amount = gold_data[i]["amount"]
            total_amount = self.calculate_total_amount_for_gold(gold_amount)
            total_gold_data[gold_type] = [gold_amount, total_amount]
        return total_gold_data

    def show_gold_data(self):
        total_gold_data = self.all_gold_data()
        gold_types = list(total_gold_data.keys())
        gold_amounts = [i[0] for i in total_gold_data.values()]
        gold_total_values = [i[1] for i in total_gold_data.values()]

        total_portfolio_value = sum(gold_total_values)

        plt.figure(figsize=(12, 6))

        gold_colors = ['#FFD700', '#DAA520', '#FFBF00', '#FF4500', '#FFA500']

        plt.subplot(1, 2, 1)
        cell_text = []
        for i in range(len(gold_types)):
            formatted_total_value = "{:.2f}".format(gold_total_values[i])
            cell_text.append(
                [gold_types[i], gold_amounts[i], formatted_total_value])

        table = plt.table(cellText=cell_text, colLabels=["Altın Tipi", "Adet", "Toplam Tutar (TL)"],
                          cellLoc='center', loc='center', colColours=gold_colors)
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.auto_set_column_width(col=list(range(3)))
        table.scale(1, 2)

        plt.title("Altın Bilgileri", fontsize=14)
        plt.subplot(1, 2, 2)
        plt.axis('equal')
        plt.rcParams['font.size'] = 12
        plt.pie(gold_total_values, labels=gold_types,
                autopct='%1.1f%%', startangle=140, colors=gold_colors)
        plt.title("Altınların Oransal Dağılımı", fontsize=14)

        plt.figtext(
            0.5, 0.01, "Toplam Portföy Değeri: {:.2f} TL".format(
                total_portfolio_value),
            ha="center", fontsize=12, bbox={"facecolor": "#FFD700", "alpha": 0.5, "pad": 5})

        plt.suptitle("Altın Portföyü", fontsize=18)
        plt.subplots_adjust(left=0.2, bottom=0.2)
        plt.show()
