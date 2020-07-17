import usuarios.user as modelo
import notas.acciones as Nota
import re
import getpass
import Enums
registro = Enums.registro()
campoUsuario = Enums.campoUsuario()

"""
    En este modulo se desarrollan las acciones principales REGISTRO, LOGIN y PROXIMAS ACCIONES como metodos de clase
    estos instancian la clase User() en donde se van a almacenar los datos ingresados por el usuario.
    Estas clases se utilizarán en otro módulo para que, a través de sus atributos de clase, se ejecuten las diferentes
    consultas SQL. 

"""


class AccionesPrincipales:

    def registro(self):
        print("\nVamos a registrarte!\n")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")
        
        usuario = modelo.User(nombre, apellidos, email, password)
        registro_qr = usuario.registrar()

        if registro_qr[registro.exitoso] >= 1:
            print(f"Perfecto {registro_qr[registro.usuario].nombre} te has registrado con el email {registro_qr[registro.usuario].email}")
        else:
            print("\nYa existe un registro con ese mismo email")

    def login(self):
        print("\nVamos a loguearte!\n")

        #Este bloque de codigo es susceptible a tener errores en la consulta SQL que valida los datos en la BBDD
        try:
            email = input("Introduce tu email: ")
            password = getpass.getpass("Introduce tu password: ")

            usuario = modelo.User('', '', email, password)
            login = usuario.identificar()
            
            mujer = False
            hombre = False
            regexName = r".*a$"
            match = re.match(regexName,login[1])
            if match:
                mujer = True
            else:
                hombre = True
            
            if email == login[campoUsuario.email] and mujer:
                print(f"Bienvenida {login[campoUsuario.nombre]} te has logueado el {login[campoUsuario.fecha]}")
                self.proximasAcciones(login)
            elif email == login[3] and hombre:
                print(f"Bienvenido {login[campoUsuario.nombre]} te has logueado el {login[campoUsuario.fecha]}")
                self.proximasAcciones(login)
        except Exception as e:
            print("\nERROR")
            print(type(e).__name__)
            print("Los datos ingresados no son correctos")

    def proximasAcciones(self, usuario):
        print("""
        Acciones:
        - Crear nota(c)
        - Mostrar notas(s)
        - Eliminar notas(d)
        - Salir(e)
        """)
        while True:
            accion = input("¿Que desea realizar?: ")
            if  accion != "c" and accion != "s" and accion != "d" and accion != "e":
                continue
            else:
                break

        do = Nota.Acciones()     

        if accion == "c":
            do.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "s":
            do.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "d":
            do.borrar(usuario)
            self.proximasAcciones(usuario)
        else:
            print(f"Ok {usuario[campoUsuario.nombre]}! Hasta la proxima :D")
            exit()