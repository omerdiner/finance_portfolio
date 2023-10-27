from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import api.get_key_from_file as gkff


def get_crypto_prices():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=TRY'
    parameters = {

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': gkff.get_key("crypto.txt")
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data["data"]

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
