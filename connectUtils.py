import mysql.connector
import sys

def createConn(data):
    """
Function to create a connection to mysql database.

structure of data(parameter) must be like
data = {
'host': 'ip or localhost',
'username': 'username',
'password': 'password',
'database': 'database name'
}
    """
    try:
        conn = mysql.connector.connect(
            host=data['host'],
            username=data['username'],
            password=data['password'],
            database=data['database']
            )
        print('Connection Sucessfull')
        cursor = conn.cursor()
        return (conn, cursor)
    
    except Exception as e:
        print('An error occured during+n : {}'.format(str(e)))
        sys.exit()