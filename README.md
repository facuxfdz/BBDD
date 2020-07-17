# BBDD
Proyecto de login y registro con Python y MySql

Este proyecto trata de implementar y acoplar los principales conceptos de POO y BBDD.
Se trata de un sistema de registro y logueo de usuarios en el cual, una vez logueado, el usuario podrá realizar diferentes acciones, consultarlas y editarlas 
(en un primer momento, notas).
En los modulos cuyo nombre termina en "_qr", se desarrollan los métodos de clase encargados de ejecutar las consultas a la BBDD.
En los modulos con nombre "acciones" se instancian las clases desarrolladas en los módulos "_qr" y ejecutan sus métodos.
En el módulo restante "main.py" se hace la invocación a los métodos de clase desarrollados en "acciones_principales.py" para elegir dentro del MENU.
En el módulo "conexionBBDD" se realiza, como bien expresa su nombre, la conexion a la base de datos MySql.
Los modulos referentes a las primeras acciones (las que estan disponibles en el MENU) se encuentran dentro de la carpeta "usuarios" y los que son referentes
a la creación de notas, en otra.

En un principio el proyecto solo crea notas, pero lo iré editando para que haga mas cosas, la idea viene del curso en Udemy de Victor Robles los cuales iré subiendo a distintos
repositorios y agregaré siempre funcionalidades propias de mi imaginación y gusto.

See you later!!
