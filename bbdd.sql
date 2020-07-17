"""CREATE DATABASE IF NOT EXISTS python_project;
use python_project;

CREATE TABLE Usuarios(
    ID        INT(25) auto_increment not null,
    Nombre          VARCHAR(100),
    Apellidos       VARCHAR(255),
    Email           VARCHAR(255) not null,
    Password        VARCHAR(255) not null,
    Fecha           DATE not null,
    CONSTRAINT pk_Usuarios PRIMARY KEY(ID),
    CONSTRAINT uq_email UNIQUE(Email)
)ENGINE = InnoDB;

CREATE TABLE Notas(
    ID              INT(25) auto_increment not null,
    Usuario_ID      INT(25) not null,
    Titulo          VARCHAR(255) not null,
    Descripcion     MEDIUMTEXT,
    Fecha           DATE not null,
    CONSTRAINT pk_Notas PRIMARY KEY(ID),
    CONSTRAINT fk_Nota_Usuario FOREIGN KEY(Usuario_ID) REFERENCES Usuarios(ID)
)ENGINE = InnoDB;"""