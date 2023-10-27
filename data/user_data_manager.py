import json
import os

folder_path = "/user_financial_data"


def get_current_dir():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path.replace("\\", "/")


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


def get_user_crypto_data():
    current_dir = get_current_dir()
    file_name = "crypto_data.json"
    with open(f"{current_dir}{folder_path}/{file_name}", "r", encoding='utf8') as json_file:
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
    # new_stock_data = [{"code": code,  "amount": amount}]
    cwd = get_current_dir()
    file_name = "stock_data.json"
    with open(f"{cwd}{folder_path}/{file_name}", "w", encoding='utf8') as json_file:
        json.dump(new_stock_data, json_file, indent=4, ensure_ascii=False)


def update_user_currency_data(new_currency_data):
    # new_currency_data = [{"code": code, "amount": amount}]
    cwd = get_current_dir()
    file_name = "currency_data.json"
    with open(f"{cwd}{folder_path}/{file_name}", "w", encoding='utf8') as json_file:
        json.dump(new_currency_data, json_file, indent=4, ensure_ascii=False)


def update_user_crypto_data(new_crypto_data):
    # new_crypto_data = [{"symbol": symbol, "amount": amount}]
    cwd = get_current_dir()
    file_name = "crypto_data.json"
    with open(f"{cwd}{folder_path}/{file_name}", "w", encoding='utf8') as json_file:
        json.dump(new_crypto_data, json_file, indent=4, ensure_ascii=False)


def update_currency_history(transaction):
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
    #transaction = {"date": date, "name":name,"amount": amount, "price": price, "total": total, "type": type, "note": note}
    cwd = get_current_dir()
    file_name = "gold_history.json"
    with open(f"{cwd}{folder_path}/{file_name}", "r", encoding='utf8') as json_file:
        json_data = json_file.read()
        data = json.loads(json_data)
        data.append(transaction)
    with open(f"{cwd}{folder_path}/{file_name}", "w", encoding='utf8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def update_crypto_history(transaction):
    #transaction = {"date": date, "symbol":symbol,"amount": amount, "price": price, "total": total, "type": type, "note": note}
    cwd = get_current_dir()
    file_name = "crypto_history.json"
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


def currency_operation(transaction):
    code = transaction["code"]
    quantity = transaction["quantity"]
    transaction_type = transaction["transaction_type"]

    user_currency_data = get_user_currency_data()

    for currency in user_currency_data:
        if currency["code"] == code:
            if transaction_type == "Buy":
                currency["amount"] = int(currency["amount"])+int(quantity)
            else:
                if int(currency["amount"]) < int(quantity):
                    return False
                currency["amount"] = int(currency["amount"])-int(quantity)
                if int(currency["amount"]) == 0:
                    user_currency_data.remove(currency)
            update_user_currency_data(user_currency_data)
            return True

    if transaction_type == "Sell":
        return False

    new_currency = {"code": code, "amount": int(quantity)}
    user_currency_data.append(new_currency)
    update_user_currency_data(user_currency_data)
    return True


def gold_operation(transaction):
    name = transaction["name"]
    quantity = transaction["quantity"]
    transaction_type = transaction["transaction_type"]

    user_gold_data = get_user_gold_data()

    for gold in user_gold_data:
        if gold["name"] == name:
            if transaction_type == "Buy":
                gold["amount"] = float(gold["amount"]) + float(quantity)
            else:
                if float(gold["amount"]) < float(quantity):
                    return False
                gold["amount"] = float(gold["amount"]) - float(quantity)
                if float(gold["amount"]) == 0.0:
                    user_gold_data.remove(gold)
            update_user_gold_data(user_gold_data)
            return True

    if transaction_type == "Sell":
        return False

    new_gold = {"name": name, "amount": float(quantity)}
    user_gold_data.append(new_gold)
    update_user_gold_data(user_gold_data)
    return True


def crypto_operation(transaction):

    symbol = transaction["symbol"]
    quantity = transaction["quantity"]
    transaction_type = transaction["transaction_type"]

    user_crypto_data = get_user_crypto_data()

    for crypto in user_crypto_data:
        if crypto["symbol"] == symbol:
            if transaction_type == "Buy":
                crypto["amount"] = float(crypto["amount"]) + float(quantity)
            else:
                if float(crypto["amount"]) < float(quantity):
                    return False
                crypto["amount"] = float(crypto["amount"]) - float(quantity)
                if float(crypto["amount"]) == 0.0:
                    user_crypto_data.remove(crypto)
            update_user_crypto_data(user_crypto_data)
            return True

    if transaction_type == "Sell":
        return False

    new_crypto = {"symbol": symbol, "amount": float(quantity)}
    user_crypto_data.append(new_crypto)
    update_user_crypto_data(user_crypto_data)
    return True


# TO-DO    GET_GOLD_HISTORY, GET_STOCK_HISTORY, GET_CURRENCY_HISTORY
