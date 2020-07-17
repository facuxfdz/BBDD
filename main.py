"""
    Proyecto Python y MySql:
    -Abrir asistente
    -Login o registro
    -Registro: Creará un usuario en la bbdd
    -Login: Identifica al usuario y preguntará
    -Crear nota, mostrar nota, borrar nota
"""
from usuarios import acciones_principales as acciones

print("""
MENU:
    -Registro(r)
    -Login(l)
""")
do = acciones.AccionesPrincipales()

while True:
    accion = input("Tipee la accion que desea realizar: ")
    if accion == "r":
        do.registro()
        break
    elif accion == "l":
        do.login()
        break
    else:
        continue
