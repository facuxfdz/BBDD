import mysql.connector
import datetime

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "python_project",
    port = "3308"
)

cursor = database.cursor(buffered=True)

class User:

    def __init__(self, nombre, apellidos, email, paswd):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = paswd
    
    def to_reg(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, self.password, fecha)

        cursor.execute(sql, usuario)
        database.commit()
        
        return [cursor.rowcount, self]

    def identity(self):
        return  "bye"
