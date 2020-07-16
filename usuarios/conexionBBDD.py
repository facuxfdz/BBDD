import mysql.connector

def connect():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "python_project",
        port = "3308"
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]
