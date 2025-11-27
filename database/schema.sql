CREATE DATABASE ufc;
USE ufc;

-- tabla de luchadores
CREATE TABLE fighters (
	fighter_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR (50),
    nickname VARCHAR (50),
    gender ENUM('Male', 'Female'),
    weight_class VARCHAR (30),
    country VARCHAR (50)
);

-- tablas de divisiones
CREATE TABLE weight_classes(
	weight_class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(50),
    gender ENUM ('Male', 'Female') NOT NULL
);

-- tabla de eventos
CREATE TABLE events(
	event_id INT AUTO_INCREMENT PRIMARY KEY,
    edition_number INT,
    event_name VARCHAR(120) NOT NULL,
    event_date DATE,
    location_name VARCHAR (200)
);

-- tabla de peleas
CREATE TABLE fights (
	fight_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    fighter_red INT NOT NULL,
    winner INT NULL,
    method VARCHAR(80),
    round_number INT,
    notes TEXT,
    CONSTRAINT fk_fights_event FOREIGN KEY (event_id) REFERENCES events(events_id),
    CONSTRAINT fk_fights_red FOREIGN KEY (fighter_red) REFERENCES fighters(fighter_id),
    CONSTRAINT fk_fights_blue FOREIGN KEY (fighter_blue) REFERENCES fighters(fighter_id),
    CONSTRAINT fk_fights_winner FOREIGN KEY (winner) REFERENCES fighters(fighter_id)
);



