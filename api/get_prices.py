import api.get_key_from_file as gkff
import api.get_stock_prices as stock
import api.get_gold_prices as gold
import api.get_crypto_prices as crypto
import api.get_currency_prices as currency


def get_current_prices():
    currency_prices = currency.get_currency_prices()
    stock_prices = stock.get_stock_prices()
    gold_price = gold.get_gold_price()
    crypto_prices = crypto.get_crypto_prices()
    current_prices = [currency_prices, stock_prices, gold_price, crypto_prices]
    return current_prices
