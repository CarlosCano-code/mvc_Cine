DROP DATABASE IF EXISTS citasM_db;
CREATE DATABASE IF NOT EXISTS citasM_db;
use citasM_db;

CREATE TABLE IF NOT EXISTS paciente(
	pacienteID INT NOT NULL AUTO_INCREMENT,
    nombre_p VARCHAR(30),
    primerA_p VARCHAR(20),
    segundoA_p VARCHAR(20),
    descr VARCHAR(150),
    primary key(pacienteID)
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS medico(
	medicoID INT NOT NULL AUTO_INCREMENT,
	nombre_m VARCHAR(30),
	primerA_m VARCHAR(20),
    segundoA_m VARCHAR(20),
	departamento VARCHAR(20),
    primary key(medicoID)
)ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS consultorio(
	consultorioID INT NOT NULL AUTO_INCREMENT,
    medicoID INT,
    tipoConsultorio VARCHAR(20),
    primary key (consultorioID),
    CONSTRAINT fkmedicoID_c FOREIGN KEY (medicoID)
    REFERENCES medico(medicoID)
    ON DELETE SET NULL
    ON UPDATE CASCADE
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS citas(
	citaID INT NOT NULL AUTO_INCREMENT,
    consultorioID INT,
    pacienteID INT,
    fecha date,
    hora VARCHAR(15),
    descrCita VARCHAR(250),
    primary key (citaID),
    CONSTRAINT fkconsultorio_ci FOREIGN KEY (consultorioID)
    REFERENCES consultorio(consultorioID)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
    CONSTRAINT fkpaciente_ci FOREIGN KEY (pacienteID)
    REFERENCES paciente(pacienteID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=INNODB;

