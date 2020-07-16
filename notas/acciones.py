import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1]}! Vamos a crear una nueva nota:  ")
        titulo = input("\nIntroduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"La nota '{nota.Titulo}'ha sido guardada exitosamente!")
        else:
            print("Error al intentar guardar la nota ;(")

    def mostrar(self, usuario):
        print(f"\nOk {usuario[1]} estas son tus notas:\n")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("*"*30)
            print(f"Titulo: {nota[2]}")
            print(f"Contenido: {nota[3]}")
            print("*"*30)

    
    def borrar(self, usuario):
        print(f"\n Ok {usuario[1]}! Vamos a borrar una nota")
        
        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0],titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"La nota '{nota.Titulo}' ha sido eliminada correctamente")
        else:
            print("No se pudo eliminar la nota ;(")
