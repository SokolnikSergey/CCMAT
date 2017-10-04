import requests, json, poloniex,time
from json import loads as _loads
from hmac import new as _new
from hashlib import sha512 as _sha512
from requests import post as _post

try:
    from urllib.parse import urlencode as _urlencode
except ImportError:
    from urllib import urlencode as _urlencode

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


from FinancialUpdator import FinancilacUpdator
# from CurrencyContainer import CurrencyContainer
#
# container = CurrencyContainer()
# public_polo = poloniex.PoloniexPublic()
# #
# f2 = FinancilacUpdator(public_polo,container)
# f2.start()



timeout = 3

nonce =  int(time.time()*1000)

if not KEY or not Secret:
    raise ValueError("A Key and Secret needed!")
    # set nonce
args = {"currency":"BTC", "amount":0.0002, "address":"1KVDdPzFE1FR9WcUD4b69Un4dbTSLgbJTc"}
args['command'] = 'withdraw'
args['nonce'] = nonce

try:
    # encode arguments for url
    postData = _urlencode(args)
    # sign postData with our Secret
    sign = _new(
        Secret.encode('utf-8'),
        postData.encode('utf-8'),
        _sha512)
    # post request
    ret = _post(
        'https://poloniex.com/tradingApi',
        data=args,
        headers={
            'Sign': sign.hexdigest(),
            'Key': KEY
        },
        timeout=timeout)

    print(ret)
    print(_loads(ret.text, parse_float=str))

except Exception as e:
    raise e
finally:
    # increment nonce(no matter what)

    nonce += 1
    print("NoNce", nonce)
    # return decoded json