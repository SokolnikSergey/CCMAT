from datetime import datetime
from Server.DataBaseConnector import DataBaseConnector

class DataBaseTransactor:

    def __init__(self, db_connector):

        self.__db_connector = db_connector

    def result_of_withdraw(self,wallet_owner,wallet_reciever ,imei_bankomat,location,crypto_type,amount_crypto,amount_real):
        
        data_time = datetime.now()
        transaction_id = 0
        query = "insert into transactions values (NULL,NULL,{amount_of_crypto},{amount_of_real},'{date_time}','{type_crypto}');"\
             .format(amount_of_crypto = amount_crypto,amount_of_real = amount_real,date_time = data_time, type_crypto = crypto_type)
        cur = self.__db_connector.cursor()
        cur.execute(query)
        self.__db_connector.commit()
        
        try:
            query = "select id_transaction from transactions where amount_of_crypto={amount_of_crypto}" \
                    "  and amount_of_real={amount_of_real};".format(amount_of_crypto = amount_crypto,
                                    amount_of_real = amount_real,date_time =data_time)
            cur = self.__db_connector.cursor()
            cur.execute(query)
            transaction_id = cur.fetchall()[-1][0]
        except Exception as ex:
            transaction_id = 0
        
    
        query = "select id_bankomat from bankomats where imei_bankomat='{imei_bankomat}' and location='{location}' ".format(imei_bankomat=imei_bankomat, location=location)
        cur.execute(query)
        bankomat_id_s = cur.fetchall()
        if bankomat_id_s:
            bankomat_id = bankomat_id_s[-1][0]
        else:
            query = "insert into bankomats values (NULL,'{location}','{imei_bankomat}');".format(imei_bankomat = imei_bankomat, location  = location)
            cur.execute(query)
            self.__db_connector.commit()
            query = "select id_bankomat from bankomats where location='{location}' and imei_bankomat='{imei_bankomat}';".format(imei_bankomat=imei_bankomat, location=location)
            cur.execute(query)

            bankomat_id_s = cur.fetchall()
            if bankomat_id_s:
                bankomat_id = bankomat_id_s[-1][0]

        query = "insert into operations values (NULL,'{client_wallet}','{server_wallet}',{id_bankomat},{id_transaction});" \
            .format(client_wallet = wallet_reciever,server_wallet = wallet_owner,id_bankomat = bankomat_id,id_transaction = transaction_id)
        cur = self.__db_connector.cursor()
        cur.execute(query)
        self.__db_connector.commit()


connector = DataBaseConnector(database="bankomat")
conn = connector.get_connector(connector.config)
transactor = DataBaseTransactor(conn)
transactor.result_of_withdraw("1","2","imei_bankomat123","BEL Minsk","BTC",2.65,32121.2)