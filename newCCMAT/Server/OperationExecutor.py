import time
from hashlib import sha512 as _sha512
from hmac import new as _new
from json import loads as _loads

from requests import post as _post

from ENUMS.CURRENCIES import CURRENCIES

try:
    from urllib.parse import urlencode as _urlencode
except ImportError:
    from urllib import urlencode as _urlencode

class OperationExecutor:

    def __init__(self,api_key,secret_key,aux_info_container = None,balance_info_container  = None, timeout = 15):
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.__timeout = timeout
        
        self.__aux_info_container = aux_info_container
        self.__balance_information_container  = balance_info_container

    def get_nonce(self):
        return int(time.time() * 1000)

    def get_currency_name(self,currency):
        if currency in CURRENCIES:
            currency_name = CURRENCIES.BitCoin.value
            return currency_name
        return None


    def withdraw(self,currency,reciever_address,amount_of_crypto):

        print("Withdraw with currency {} reciever_address = {} amount_of_crypto={}".format(currency,reciever_address,amount_of_crypto))
        currency_name = self.get_currency_name(currency)

        if self.__aux_info_container.test_mode == '1':
            print("In test mode !!!!!!!")
            return {"currency": currency, "amount": amount_of_crypto, "address": reciever_address}

        args = {"currency": currency_name, "amount": amount_of_crypto, "address": reciever_address,
                'command' : 'withdraw' , 'nonce' : self.get_nonce() }

        try:
            # encode arguments for url
            postData = _urlencode(args)
            # sign postData with our Secret
            sign = _new(
                self.__secret_key.encode('utf-8'),
                postData.encode('utf-8'),
                _sha512)
            # post request
            ret = _post(
                'https://poloniex.com/tradingApi',
                data=args,
                headers={
                    'Sign': sign.hexdigest(),
                    'Key': self.__api_key
                },
                timeout=self.__timeout)
            print("Transaction successfully performed crypto {}  recieved {} currency  {} ".format(amount_of_crypto,reciever_address,currency))
            return _loads(ret.text, parse_float=str)

        except Exception as ex:
            print(ex)

        
    def get_btc_balance(self):
        pass
        args = {'command': 'returnBalances', 'nonce': self.get_nonce()}

        try:
            # encode arguments for url
            postData = _urlencode(args)
            # sign postData with our Secret
            sign = _new(
                self.__secret_key.encode('utf-8'),
                postData.encode('utf-8'),
                _sha512)
            # post request
            ret = _post(
                'https://poloniex.com/tradingApi',
                data=args,
                headers={
                    'Sign': sign.hexdigest(),
                    'Key': self.__api_key
                },
                timeout=self.__timeout)

            return _loads(ret.text, parse_float=str)['BTC']

        except Exception as ex:
            print(ex)
            return 0.101 ### This is default value

###########################################
    def  get_remain_money(self,currency):
        if CURRENCIES.BitCoin == currency:
            return float(self.get_btc_balance()) - float(self.__balance_information_container.btc_reserved)

        
    def get_owners_fee(self,currency):
        if CURRENCIES.BitCoin == currency:
            return self.__aux_info_container.owners_fee


    def inform_me(self,currency):

        remain_money = self.get_remain_money(currency)
        owners_fee = self.get_owners_fee(currency)
        
        return {"data":{"currency" : CURRENCIES.BitCoin, "remain_money": remain_money,"owners_fee":owners_fee},"response_errors": [] }
    
#############################
