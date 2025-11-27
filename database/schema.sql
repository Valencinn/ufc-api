CREATE DATABASE ufc;
USE ufc;

CREATE TABLE fighters (
	fighter_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR (50),
    nickname VARCHAR (50),
    gender ENUM('Male', 'Female'),
    weight_class VARCHAR (30),
    country VARCHAR (50)
)



