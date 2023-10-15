import api.get_prices as get_prices
import json
import datetime
import os


def get_cwd():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path.replace("\\", "/")


def add_new_financial_data():
    # Get data from API
    currency_prices = get_prices.get_currency_prices()
    stock_prices = get_prices.get_stock_prices()
    gold_price = get_prices.get_gold_price()

    if currency_prices is None or stock_prices is None or gold_price is None:
        print("Veri alınamadı.")
        return
    add_currency_prices(currency_prices)
    add_stock_prices(stock_prices)
    add_gold_price(gold_price)


def add_currency_prices(currency_prices):

    save_array_to_json(currency_prices, "/financial_data/currency_prices")


def add_stock_prices(stock_prices):
    save_array_to_json(stock_prices, "/financial_data/stock_prices")


def add_gold_price(gold_price):
    save_array_to_json(gold_price, "/financial_data/gold_price")


def save_array_to_json(data, folder_path):
    try:
        # Diziyi JSON formatına dönüştür
        json_data = json.dumps(data, indent=4, ensure_ascii=False)

        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        cwd = get_cwd()
        file_name = f"{cwd}{folder_path}/{formatted_datetime}.json"

        with open(file_name, "w", encoding='utf8') as json_file:
            json_file.write(json_data)

        print(f"Veri başarıyla '{file_name}' dosyasına kaydedildi.")
        return True

    except Exception as e:
        print(f"Hata oluştu: {e}")
        return False


def get_all_data_for_a_stock(stock_code):
    cwd = get_cwd()
    folder_path = "/financial_data/stock_prices"
    file_names = os.listdir(f"{cwd}{folder_path}")
    file_names.sort()

    stock_data = []

    for file_name in file_names:
        with open(f"{cwd}{folder_path}/{file_name}", "r", encoding='utf8') as json_file:
            json_data = json_file.read()
            data = json.loads(json_data)
            for stock in data:
                if stock["code"] == stock_code:
                    stock["date"] = file_name[:10]
                    stock_data.append(stock)
                    break

    return stock_data


def get_all_data_for_a_currency(currency_code):
    cwd = get_cwd()
    folder_path = "/financial_data/currency_prices"
    file_names = os.listdir(f"{cwd}{folder_path}")
    file_names.sort()

    currency_data = []

    for file_name in file_names:
        with open(f"{cwd}{folder_path}/{file_name}", "r", encoding='utf8') as json_file:
            json_data = json_file.read()
            data = json.loads(json_data)
            for currency in data:
                if currency["code"] == currency_code:
                    currency_data.append(currency)
                    break

    return currency_data


def get_all_data_for_gold():
    cwd = get_cwd()
    folder_path = "/financial_data/gold_price"
    file_names = os.listdir(f"{cwd}{folder_path}")
    file_names.sort()

    gold_data = []

    for file_name in file_names:
        with open(f"{cwd}{folder_path}/{file_name}", "r", encoding='utf8') as json_file:
            json_data = json_file.read()
            data = json.loads(json_data)
            gold_data.append(data)

    return gold_data
