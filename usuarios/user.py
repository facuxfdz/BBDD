import datetime
import hashlib
import usuarios.conexionBBDD as cnx

connect = cnx.connect()
database = connect[0]
cursor = connect[1]

class User:

    def __init__(self, nombre, apellidos, email, paswd):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = paswd
    
    def to_reg(self):
        fecha = datetime.datetime.now()
        #Cifrando contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            return [cursor.rowcount, self]
        except:
            return [0,self]

    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        usuario = (self.email, cifrado.hexdigest()) #Creo una tupla para poder hacer el reemplazo del %s en la consulta sql

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result