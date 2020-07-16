import usuarios.user as modelo
import notas.acciones
import re
import getpass

class actions:

    def registro(self):
        print("\nVamos a registrarte!\n")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")
        
        usuario = modelo.User(nombre, apellidos, email, password)
        registro_bd = usuario.to_reg()

        if registro_bd[0] >= 1:
            print(f"Perfecto {registro_bd[1].nombre} te has registrado con el email {registro_bd[1].email}")
        else:
            print("\nYa existe un registro con ese mismo email")

    def login(self):
        print("\nVamos a loguearte!\n")

        try:
            email = input("Introduce tu email: ")
            password = getpass.getpass("Introduce tu password: ")

        
            usuario = modelo.User('', '', email, password)
            login = usuario.identificar()
            mujer = False
            hombre = False
            name = r".*a$"
            match = re.match(name,login[1])
            if match:
                mujer = True
            else:
                hombre = True
            
            if email == login[3] and mujer:
                print(f"Bienvenida {login[1]} te has logueado el {login[5]}")
                self.proximasAcciones(login)
            elif email == login[3] and hombre:
                print(f"Bienvenido {login[1]} te has logueado el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
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
        do = notas.acciones.Acciones()        
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
            print(f"Ok {usuario[1]}! Hasta la proxima :D")
            exit()