create database automotriz;
USE automotriz;

CREATE TABLE clientes (
	id_cliente int auto_increment PRIMARY KEY,
    nombre varchar(150) NOT NULL,
    rut	 varchar(20) NOT NULL UNIQUE,
    telefono varchar(20),
    correo varchar(100)
);

CREATE TABLE vehiculos (
	id_auto int auto_increment PRIMARY KEY,
    patente varchar(150) NOT NULL UNIQUE,
    marca varchar(20) NOT NULL,
    modelo varchar(20)NOT NULL,
    año int,
    color varchar(30),
    id_cliente int, FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE presupuestos (
	id_presupuesto int auto_increment PRIMARY KEY,
    numero_presupuesto int NOT NULL UNIQUE,
    fecha date NOT NULL,
    total_neto int DEFAULT 0,
    id_auto int, FOREIGN KEY (id_auto) REFERENCES vehiculos(id_auto)
);


SELECT * FROM vehiculos;	
