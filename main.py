"""
    En este modulo se hace la invocacion a los metodos de clase que permiten elegir 
    entre las opciones disponibles del MENU
    
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
