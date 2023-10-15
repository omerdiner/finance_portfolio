import http.client
import json

conn = http.client.HTTPSConnection("api.collectapi.com")
headers = {
    'content-type': "application/json",
    'authorization': "apikey 2MBeOiZ3cJIAcPtK730zWn:1LrUrqmwvnpBdrtRyOSzU8"
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
