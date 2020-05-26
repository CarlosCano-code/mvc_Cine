DROP DATABASE IF EXISTS cine_db;
CREATE DATABASE IF NOT EXISTS cine_db;
use cine_db;



CREATE TABLE IF NOT EXISTS idioma(
	idiomaID INT NOT NULL AUTO_INCREMENT ,
    descr	VARCHAR(20),
    PRIMARY KEY(idiomaID)
)ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS asientos(
	asientoID INT NOT NULL auto_increment,
    asientos_x INT NOT NULL,
    asientos_y INT NOT NULL,
    PRIMARY KEY(asientoID)
)ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS fecha(
	fechaID INT NOT NULL AUTO_INCREMENT,
    fecha date,
    PRIMARY KEY(fechaID)
)ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS userx(
	userxID INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(20) NOT NULL,
    apellido1 VARCHAR(20) NOT NULL,
    apellido2 VARCHAR(20) NOT NULL,
    PRIMARY KEY(userxID)
)ENGINE=INNODB;


    
    
CREATE TABLE IF NOT EXISTS pelicula(
	peliculaID INT NOT NULL AUTO_INCREMENT,
    idiomaID INT NOT NULL,
    nombrePelicula VARCHAR(30) NOT NULL,
    clasificacion VARCHAR(10) NOT NULL,
    sipnosis VARCHAR(250),
    duracion VARCHAR(20),
    PRIMARY KEY(peliculaId),
    CONSTRAINT fkidiomaID_pelicula FOREIGN KEY(idiomaID)
		REFERENCES idioma(idiomaID)
        ON UPDATE CASCADE
)ENGINE=INNODB;
    
    
CREATE TABLE IF NOT EXISTS sala(
	salaID INT NOT NULL AUTO_INCREMENT,
    asientoID INT NOT NULL,
    tipo VARCHAR(20),
	PRIMARY KEY(salaID,asientoID),
    CONSTRAINT fkasientoID_sala FOREIGN KEY(asientoID)
		REFERENCES asientos(asientoID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE=INNODB;




CREATE TABLE IF NOT EXISTS funcion(
	funcionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    peliculaID INT NOT NULL,
    salaID INT NOT NULL,
    fechaID INT NOT NULL,
    hora VARCHAR(10) NOT NULL,
    CONSTRAINT fkpel_fun FOREIGN KEY(peliculaID)
		REFERENCES pelicula(peliculaID)
        ON UPDATE CASCADE,
	CONSTRAINT fksala_fun FOREIGN KEY(salaID)
		REFERENCES sala(salaID)
        ON UPDATE CASCADE,
	CONSTRAINT fkfecha_fun FOREIGN KEY(fechaID)
		REFERENCES fecha(fechaID)
        ON UPDATE CASCADE  
)ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS boleto(
	boletoID INT NOT NULL AUTO_INCREMENT,
    funcionID INT NOT NULL,
    asiento VARCHAR(10) NOT NULL,
    PRIMARY KEY(boletoID),
    CONSTRAINT fkfuncionID FOREIGN KEY(funcionID)
		REFERENCES funcion(funcionID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
    ) ENGINE=INNODB;
    
    
    
CREATE TABLE IF NOT EXISTS boleto_usuario(
	boletoID INT NOT NULL,
    userxID INT NOT NULL,
    PRIMARY KEY (boletoID,userxID),
    FOREIGN KEY(boletoID)
		REFERENCES boleto(boletoID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
        FOREIGN KEY(userxID)
		REFERENCES userx(userxID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
)ENGINE=INNODB;
