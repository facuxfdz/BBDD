import usuarios.acciones_principales_qr as modelo
import notas.acciones_user as Nota
import re
import getpass

exitoso, usuarioSelf = (0,1)
nombre_usuario, emailUsuario, fechaUsuario = (1,3,5)

"""
    En este modulo se desarrollan las acciones principales REGISTRO(), LOGIN() y PROXIMAS ACCIONES().
    En estas se instancia la clase User() que recopila los datos necesarios para realizar las consultas SQL.

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

        if registro_qr[exitoso] >= 1:
            print(f"Perfecto {registro_qr[usuarioSelf].nombre} te has registrado con el email {registro_qr[usuarioSelf].email}")
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
            match = re.match(regexName,login[nombre_usuario])
            if match:
                mujer = True
            else:
                hombre = True
            
            if email == login[emailUsuario] and mujer:
                print(f"Bienvenida {login[nombre_usuario]} te has logueado el {login[fechaUsuario]}")
                self.proximasAcciones(login)
            elif email == login[3] and hombre:
                print(f"Bienvenido {login[nombre_usuario]} te has logueado el {login[fechaUsuario]}")
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
            print(f"Ok {usuario[nombre_usuario]}! Hasta la proxima :D")
            exit()