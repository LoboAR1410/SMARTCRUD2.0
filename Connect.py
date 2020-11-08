import mysql.connector

def DBConn():
    DataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='consola',
        port=3308
    )
    Query = DataBase.cursor(buffered=True)

    return [DataBase,Query]

