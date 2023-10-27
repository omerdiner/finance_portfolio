import http.client
import json
import api.get_key_from_file as gkff
conn = http.client.HTTPSConnection("api.collectapi.com")
headers = {
    'content-type': "application/json",
    'authorization': gkff.get_key("collect_api_economy.txt"),
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
