from mysql.connector import MySQLConnection


class DataBaseConnector():

  def __init__(self,user = 'root',password = '',host =  '127.0.0.1',database = 'qr_0' , raise_on_warnings  =  True):
      self.set_configurations(user,password,host,database,raise_on_warnings)

  @property
  def config(self):
    return self.__config

  def set_configurations(self,*config):
      self.__config = {
        'user': config[0],
        'password': config[1],
        'host': config[2],
        'database': config[3],
        'raise_on_warnings': config[4],
      }

  def get_connector(self,config):
    conn = MySQLConnection(**config)
    return conn
