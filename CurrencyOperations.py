class CurrencyOperations:

    @staticmethod
    def get_btc_usd(polo):
        return polo.returnTicker()["USDT_BTC"]['last']