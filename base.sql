CREATE DATABASE jobfair
  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;

CREATE TABLE CV2015(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(100),
    surname VARCHAR(100),
    adress TEXT,
    zip VARCHAR(100),
    city VARCHAR(200),
    phone VARCHAR(100),
    email VARCHAR(300),
    web TEXT,
    birth DATE,
    education TEXT,
    experience TEXT,
    languages TEXT,
    computerskills TEXT,
    otherskills TEXT
);