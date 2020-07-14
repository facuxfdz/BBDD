import usuarios.user as modelo

class actions:

    def reg(self):
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
            print("No se ha podido registrar de manera exitosa :(")


    def login(self):
        print("\nVamos a loguearte!\n")

        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")
