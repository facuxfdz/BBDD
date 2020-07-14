"""
    Proyecto Python y MySql:
    -Abrir asistente
    -Login o registro
    -Registro: Creará un usuario en la bbdd
    -Login: Identifica al usuario y preguntará
    -Crear nota, mostrar nota, borrar nota
"""
from usuarios import actions

print("""
MENU:
    -Registro(r)
    -Login(l)
""")
do = actions.actions()

while True:
    accion = input("Tipee la accion que desea realizar: ")
    if accion == "r":
        do.reg()
        break
    elif accion == "l":
        do.login()
        break
    else:
        continue
