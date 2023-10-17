import json
import os

folder_path = "/user_financial_data"


def get_current_dir():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path.replace("\\", "/")


# gold data is a dictionary {"name":name,"amount": amount}
def get_user_gold_data():
    cwd = get_current_dir()
    file_name = "gold_data.json"
    with open(f"{cwd}{folder_path}/{file_name}", "r", encoding='utf8') as json_file:
        json_data = json_file.read()
        data = json.loads(json_data)
        return data


def get_user_stock_data():
    cwd = get_current_dir()
    file_name = "stock_data.json"
    with open(f"{cwd}{folder_path}/{file_name}", "r", encoding='utf8') as json_file:
        json_data = json_file.read()
        data = json.loads(json_data)
        return data


def get_user_currency_data():
    cwd = get_current_dir()
    file_name = "currency_data.json"
    with open(f"{cwd}{folder_path}/{file_name}", "r", encoding='utf8') as json_file:
        json_data = json_file.read()
        data = json.loads(json_data)
        return data


def update_user_gold_data(new_gold_data):
    # new_gold_data = [{"name": name,"amount": amount}]
    cwd = get_current_dir()
    file_name = "gold_data.json"
    with open(f"{cwd}{folder_path}/{file_name}", "w", encoding='utf8') as json_file:
        json.dump(new_gold_data, json_file, indent=4, ensure_ascii=False)


def update_user_stock_data(new_stock_data):
    # new_stock_data is a list of dictionaries
    # new_stock_data = [{"code": code,  "amount": amount}]
    cwd = get_current_dir()
    file_name = "stock_data.json"
    with open(f"{cwd}{folder_path}/{file_name}", "w", encoding='utf8') as json_file:
        json.dump(new_stock_data, json_file, indent=4, ensure_ascii=False)


def update_user_currency_data(new_currency_data):
    # new_currency_data is a list of dictionary
    # new_currency_data = [{"code": code, "amount": amount}]
    cwd = get_current_dir()
    file_name = "currency_data.json"
    with open(f"{cwd}{folder_path}/{file_name}", "w", encoding='utf8') as json_file:
        json.dump(new_currency_data, json_file, indent=4, ensure_ascii=False)


def update_currency_history(transaction):
    # transaction is a dictionary
    #transaction = {"date": date, "currency": currency, "amount": amount, "price": price, "total": total, "type": type,"note": note}
    cwd = get_current_dir()
    file_name = "currency_history.json"
    with open(f"{cwd}{folder_path}/{file_name}", "r", encoding='utf8') as json_file:
        json_data = json_file.read()
        data = json.loads(json_data)
        data.append(transaction)
    with open(f"{cwd}{folder_path}/{file_name}", "w", encoding='utf8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def update_stock_history(transaction):
    # transaction is a dictionary
    #transaction = {"date": date, "stock": stock, "amount": amount, "price": price, "total": total, "type": type, "note": note}
    cwd = get_current_dir()
    file_name = "stock_history.json"
    with open(f"{cwd}{folder_path}/{file_name}", "r", encoding='utf8') as json_file:
        json_data = json_file.read()
        data = json.loads(json_data)
        data.append(transaction)
    with open(f"{cwd}{folder_path}/{file_name}", "w", encoding='utf8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def update_gold_history(transaction):
    # transaction is a dictionary
    #transaction = {"date": date, "name":name,"amount": amount, "price": price, "total": total, "type": type, "note": note}
    cwd = get_current_dir()
    file_name = "gold_history.json"
    with open(f"{cwd}{folder_path}/{file_name}", "r", encoding='utf8') as json_file:
        json_data = json_file.read()
        data = json.loads(json_data)
        data.append(transaction)
    with open(f"{cwd}{folder_path}/{file_name}", "w", encoding='utf8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


# TO-DO    GET_GOLD_HISTORY, GET_STOCK_HISTORY, GET_CURRENCY_HISTORY
