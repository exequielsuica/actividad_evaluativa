CREATE TABLE Alumnos (
  id_alumno INT AUTO_INCREMENT NOT NULL,
  nombre VARCHAR(100)  DEFAULT NULL,
  apellido VARCHAR(50) DEFAULT NULL,
  dni VARCHAR(29) DEFAULT NULL,
  telefono VARCHAR(30) DEFAULT NULL,
  CONSTRAINT PK_users PRIMARY KEY (id_alumno)
);
