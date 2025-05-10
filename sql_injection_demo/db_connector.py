import mysql.connector as con
import os

class Connector:
    def __init__(self, host, port, user, password) :        
        # Connect to server
        self.cnx = con.connect(
            host=host,
            port=port,
            user=user,
            password=password, auth_plugin='mysql_native_password',database='test')

        # Get a cursor
        self.cur = self.cnx.cursor()

    def execute_query(self,query):
        try:
            self.cur.execute(query)
            return 0
        except:
            return -1
        
    def terminate_cnx(self):
        self.cnx.close()
        
