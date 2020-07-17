import notas.acciones_user_qr as modelo

"""
    En este modulo se desarrollan las acciones dentro del login, CREAR(), MOSTRAR(), BORRAR() y SALIR().
    En estas se instancia la clase Nota(), que recopila los datos necesarios para realizar las consultas SQL.

"""

exitoso, nombre_usuario = (0,1)
id_nota, titulo_nota, contenido_nota = (0,2,3)

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[nombre_usuario]}! Vamos a crear una nueva nota:  ")
        titulo = input("\nIntroduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")

        nota = modelo.Nota(usuario[id_nota],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"La nota '{nota.Titulo}'ha sido guardada exitosamente!")
        else:
            print("Error al intentar guardar la nota ;(")

    def mostrar(self, usuario):
        print(f"\nOk {usuario[nombre_usuario]} estas son tus notas:\n")

        nota = modelo.Nota(usuario[id_nota])
        notas = nota.listar()

        for nota in notas:
            print("*"*30)
            print(f"Titulo: {nota[titulo_nota]}")
            print(f"Contenido: {nota[contenido_nota]}")
            print("*"*30)

    
    def borrar(self, usuario):
        print(f"\n Ok {usuario[nombre_usuario]}! Vamos a borrar una nota")
        
        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[id_nota],titulo)
        eliminar = nota.eliminar()

        if eliminar[exitoso] >= 1:
            print(f"La nota '{nota.Titulo}' ha sido eliminada correctamente")
        else:
            print("No se pudo eliminar la nota ;(")
