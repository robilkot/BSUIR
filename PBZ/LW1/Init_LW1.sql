CREATE DEFINER=`root`@`localhost` PROCEDURE `Init_LW1`()
BEGIN

drop table if exists Lecturers;
drop table if exists Subjects;
drop table if exists StudentGroups;
drop table if exists LSG;

drop table if exists SPP;
drop table if exists Suppliers;
drop table if exists Parts;
drop table if exists Projects;

CREATE TABLE Lecturers(
id int UNIQUE PRIMARY KEY,
lastName varchar(255),
position varchar(255),
department varchar(255),
speciality varchar(255),
homePhone int
);

CREATE TABLE Subjects(
id int UNIQUE PRIMARY KEY,
name varchar(255),
hours int,
speciality varchar(255),
semester int
);

CREATE TABLE StudentGroups(
id int UNIQUE PRIMARY KEY,
name varchar(255),
students int,
speciality varchar(255),
head int
);

CREATE TABLE LSG (
    GroupId INT,
    SubjectId INT,
    LecturerId INT,
    Auditory INT NOT NULL,
    FOREIGN KEY (GroupId)
        REFERENCES StudentGroups (id)
        ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (SubjectId)
        REFERENCES Subjects (id)
        ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (LecturerId)
        REFERENCES Lecturers (id)
        ON DELETE SET NULL ON UPDATE CASCADE
);


CREATE TABLE Suppliers (
    id INT NOT NULL AUTO_INCREMENT,
    lastName VARCHAR(255) NOT NULL,
    status INT,
    city VARCHAR(100),
    PRIMARY KEY (id)
);

CREATE TABLE Parts (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    color VARCHAR(100),
    size INT,
    city VARCHAR(100),
    PRIMARY KEY (id)
);

CREATE TABLE Projects (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE SPP (
    SupplierId INT,
    PartId INT,
    ProjectId INT,
    Quantity INT NOT NULL,
    FOREIGN KEY (PartId)
        REFERENCES Parts (id)
        ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (ProjectId)
        REFERENCES Projects (id)
        ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (SupplierId)
        REFERENCES Suppliers (id)
        ON DELETE SET NULL ON UPDATE CASCADE
);

insert into Suppliers(lastName, status, city) values 
("Петров", 20, "Москва"),
("Синицын", 10, "Таллинн"),
("Фёдоров", 30, "Таллинн"),
("Чаянов", 20, "Минск"),
("Крюков", 30, "Киев");

insert into Parts(name, color, size, city) values 
("Болт", "Красный", 12, "Москва"),
("Гайка", "Зелёная", 17, "Минск"),
("Диск", "Чёрный", 17, "Вильнюс"),
("Диск", "Чёрный", 14, "Москва"),
("Корпус", "Красный", 12, "Минск"),
("Крышки", "Красный", 19, "Москва");

insert into Parts(name, color, size, city) values 
("Болт", "Красный", 12, "Москва"),
("Гайка", "Зелёная", 17, "Минск"),
("Диск", "Чёрный", 17, "Вильнюс"),
("Диск", "Чёрный", 14, "Москва"),
("Корпус", "Красный", 12, "Минск"),
("Крышки", "Красный", 19, "Москва");

insert into Projects(name, city) values
("ИПР1", "Минск"),
("ИПР2", "Таллинн"),
("ИПР3", "Псков"),
("ИПР4", "Псков"),
("ИПР5", "Москва"),
("ИПР6", "Саратов"),
("ИПР7", "Москва");

insert into SPP(SupplierId, PartId, ProjectId, Quantity) values
(1, 1, 1, 200),
(1, 1, 2, 700),
(2, 3, 1, 400),
(2, 2, 2, 200),
(2, 3, 3, 200),
(2, 3, 4, 500),
(2, 3, 5, 600),
(2, 3, 6, 400),
(2, 3, 7, 800),
(2, 5, 2, 100),
(3, 3, 1, 200),
(3, 4, 2, 500),
(4, 6, 3, 300),
(4, 6, 7, 300),
(5, 2, 2, 200),
(5, 2, 4, 100),
(5, 5, 5, 500),
(5, 5, 7, 100),
(5, 6, 2, 200),
(5, 1, 2, 100),
(5, 3, 4, 200),
(5, 4, 4, 800),
(5, 5, 4, 400),
(5, 6, 4, 500);

END