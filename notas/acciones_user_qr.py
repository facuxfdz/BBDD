import usuarios.conexionBBDD as cnx

"""
    En este modulo, que es el mas "profundo"(después del login), se desarrollan los modulos
    encargados de realizar las consultas SQL a la BBDD.

"""

connect = cnx.connect()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, Usuario_ID, Titulo="", Descripcion=""):
        self.Usuario_ID = Usuario_ID
        self.Titulo = Titulo
        self.Descripcion = Descripcion

    def guardar(self):
        sql = "INSERT INTO notas VALUES (null, %s, %s, %s, NOW())"
        nota = (self.Usuario_ID, self.Titulo, self.Descripcion)

        cursor.execute(sql,nota)
        database.commit()

        return [cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM notas WHERE Usuario_ID = {self.Usuario_ID}"
        
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def eliminar(self):
        sql = f"DELETE FROM notas WHERE Usuario_ID = {self.Usuario_ID} AND Titulo LIKE '%{self.Titulo}%'"

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]