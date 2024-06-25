-- Active: 1719357881135@@127.0.0.1@3307@ejemplo_db
create table alumnos (id_alumno int not null AUTO_INCREMENT PRIMARY KEY, nombre varchar(255), apellido varchar(255),dni int);

insert into alumnos (nombre,apellido,dni) values ("lionel","messi",12345),
("julian","alvarez",6789);

delete from alumnos where apellido = "alvarez";

update alumnos set apellido = "martinez" where apellido = "messi";

create table ejemplo (id_ejemplo int AUTO_INCREMENT not NULL AUTO_INCREMENT PRIMARY KEY, nombre varchar(255));

drop table ejemplo;