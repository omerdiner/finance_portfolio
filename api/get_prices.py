import http.client
import json

conn = http.client.HTTPSConnection("api.collectapi.com")
headers = {
    'content-type': "application/json",
    'authorization': "apikey 0XLv8qibx1Gl1F5PtgdUwv:3DrLrHcaw5eiDBlJkP5zZB"
}


def get_currency_prices():
    try:
        conn.request("GET", "/economy/allCurrency", headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data.decode("utf-8"))
        return data["result"]

    except ConnectionError as ce:
        print("Bağlantı hatası oluştu:", ce)
        return None

    except json.JSONDecodeError as je:
        print("JSON çözme hatası oluştu:", je)
        return None


def get_stock_prices():
    try:
        conn.request("GET", "/economy/hisseSenedi", headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data.decode("utf-8"))
        return data["result"]

    except ConnectionError as ce:
        print("Bağlantı hatası oluştu:", ce)
        return None

    except json.JSONDecodeError as je:
        print("JSON çözme hatası oluştu:", je)
        return None


def get_gold_price():
    try:
        conn.request("GET", "/economy/goldPrice", headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data.decode("utf-8"))
        return data["result"]

    except ConnectionError as ce:
        print("Bağlantı hatası oluştu:", ce)
        return None

    except json.JSONDecodeError as je:
        print("JSON çözme hatası oluştu:", je)
        return None


def get_current_prices():
    currency_prices = get_currency_prices()
    stock_prices = get_stock_prices()
    gold_price = get_gold_price()
    current_prices = [currency_prices, stock_prices, gold_price]
    return current_prices
