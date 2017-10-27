import requests,json
class CurrencyOperations:

    @staticmethod
    def get_btc_usd(polo):
        return polo.returnTicker()["USDT_BTC"]['last']


    @staticmethod
    ## API - the information is got by interrupting with Belarussian National Bank  ------------ http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2
    def get_dol_uah():
        USD = requests.get("http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2").text
        usd = json.loads(USD)['Cur_OfficialRate']


        # 100 UAH's matches uah  BEL Rubs
        UAH = requests.get("http://www.nbrb.by/API/ExRates/Rates/UAH?ParamMode=2").text
        uah = json.loads(UAH)['Cur_OfficialRate']

        dol_uah = usd * 100 / uah

        return dol_uah


    @staticmethod
    def get_btc_transaction_fee(polo):
        return polo.returnCurrencies()['BTC']['txFee']