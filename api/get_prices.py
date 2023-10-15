import http.client
import json
conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 2MBeOiZ3cJIAcPtK730zWn:1LrUrqmwvnpBdrtRyOSzU8"
}


def get_currency_prices():

    conn.request("GET", "/economy/allCurrency", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    return data


def get_stock_prices():
    conn.request("GET", "/economy/hisseSenedi", headers=headers)

    res = conn.getresponse()
    data = res.read()

    data = json.loads(data.decode("utf-8"))
    return data


def get_gold_price():
    conn.request("GET", "/economy/goldPrice", headers=headers)

    res = conn.getresponse()
    data = res.read()

    data = json.loads(data.decode("utf-8"))
    return data
