
class DataBaseTransactor:

    def __init__(self, db_connector):

        self.__db_connector = db_connector

    def result_of_withdraw(self,key):
        query = "SELECT q.title from qr q WHERE q.qr_key = {};".format(key)
        cur = self.__db_connector.cursor()
        cur.execute(query)
        response = cur.fetchall()
        if not response:
            return ""

        return response[0][0]
