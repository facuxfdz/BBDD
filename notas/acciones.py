import notas.nota as modelo
import Enums

campoUsuario = Enums.campoUsuario()
campoNota = Enums.campoNota()
registro = Enums.registro()

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[campoUsuario.nombre]}! Vamos a crear una nueva nota:  ")
        titulo = input("\nIntroduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")

        nota = modelo.Nota(usuario[campoNota.ID],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"La nota '{nota.Titulo}'ha sido guardada exitosamente!")
        else:
            print("Error al intentar guardar la nota ;(")

    def mostrar(self, usuario):
        print(f"\nOk {usuario[campoUsuario.nombre]} estas son tus notas:\n")

        nota = modelo.Nota(usuario[campoNota.ID])
        notas = nota.listar()

        for nota in notas:
            print("*"*30)
            print(f"Titulo: {nota[campoNota.titulo]}")
            print(f"Contenido: {nota[campoNota.contenido]}")
            print("*"*30)

    
    def borrar(self, usuario):
        print(f"\n Ok {usuario[campoUsuario.nombre]}! Vamos a borrar una nota")
        
        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[campoNota.ID],titulo)
        eliminar = nota.eliminar()

        if eliminar[registro.exitoso] >= 1:
            print(f"La nota '{nota.Titulo}' ha sido eliminada correctamente")
        else:
            print("No se pudo eliminar la nota ;(")
