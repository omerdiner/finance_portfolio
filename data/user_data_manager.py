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


def stock_operation(transaction):
    # {"code": code, "quantity": quantity, "price": price, "transaction_type": transaction_type.get()}

    code = transaction["code"]
    quantity = transaction["quantity"]
    transaction_type = transaction["transaction_type"]

    user_stock_data = get_user_stock_data()

    for stock in user_stock_data:
        if stock["code"] == code:
            if transaction_type == "Buy":
                stock["amount"] = int(stock["amount"]) + int(quantity)
            else:
                if int(stock["amount"]) < int(quantity):
                    return False
                stock["amount"] = int(stock["amount"]) - int(quantity)
                if int(stock["amount"]) == 0:
                    user_stock_data.remove(stock)
            update_user_stock_data(user_stock_data)
            return True

    if transaction_type == "Sell":
        return False

    new_stock = {"code": code, "amount": int(quantity)}
    user_stock_data.append(new_stock)
    update_user_stock_data(user_stock_data)
    return True


# TO-DO    GET_GOLD_HISTORY, GET_STOCK_HISTORY, GET_CURRENCY_HISTORY
