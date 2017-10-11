# try:
#     from urllib.parse import urlencode as _urlencode
# except ImportError:
#     from urllib import urlencode as _urlencode

### API - для информации о валюте НБРБ ------------ http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2

#
# USD = requests.get("http://www.nbrb.by/API/ExRates/Rates/USD?ParamMode=2").text
# usd = json.loads(USD)['Cur_OfficialRate']
#
#
# # 100 UAH's matches uah  BEL Rubs
# UAH = requests.get("http://www.nbrb.by/API/ExRates/Rates/UAH?ParamMode=2").text
# uah = json.loads(UAH)['Cur_OfficialRate']
# print(usd,100 / uah)
#
# dol_uah = usd * 100 / uah
#
# print( "Rates amount of UAH to USD -> ",dol_uah)


##################### Получаем отчисления за перевод

#btc_tax = polo.returnCurrencies()['BTC']['txFee'] # get bitcoin taxes
#eth_tax = polo.returnCurrencies()['ETH']['txFee'] # get etherium taxes


####################################### Получаем курс BTC относительно доллара для Poloniex
# Какой именно параметр нас инетерсует ?????????????  'last': 4282.0,
# 'lowestAsk': 4281.98999994, 'high24hr': 4434.01234, 'highestBid': 4279.00000013

# print("Rates amount of dollars to BTC -> ", polo.returnTicker()["USDT_BTC"]['last'])
#
#
# def calculate_complete_amount(UAH,fee_percent_on_exchange,fee_owner_percent):
#     exchange_tax =  (UAH*fee_percent_on_exchange)
#     owners_tax =(UAH*fee_owner_percent)
#
#     complete_uah = UAH - (exchange_tax  + owners_tax)
#
#     return complete_uah

import poloniex
from Client.CurrencyContainer import CurrencyContainer
from Client.FinancialUpdator import FinancialUpdator
from Client.Subs import Subs

# container = CurrencyContainer()
# public_polo = poloniex.PoloniexPublic()
#
# s = Subs(container)
#
# f2 = FinancialUpdator(public_polo,container)
# f2.start()
