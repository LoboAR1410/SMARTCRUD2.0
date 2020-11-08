from Usuarios import Connect as C

Conn = C.DBConn()
Db = Conn[0]
cursor = Conn[1]

class User:
    def __init__(self,name,user,password):
        self.name = name
        self.user = user
        self.password = password

    def CreateU(self):
        sql = "INSERT INTO usuario (name, user, password) VALUES (%s, %s, %s)"
        user = (self.name,self.user,self.password)
        cursor.execute(sql,user)
        return cursor.rowcount

    def Login(self):
        sql = 'SELECT * FROM usuario WHERE user = %s AND password = %s'
        data = (self.user,self.password)
        cursor.execute(sql,data)
        result = cursor.fetchone()
        return result
