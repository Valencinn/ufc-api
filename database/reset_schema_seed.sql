-- =====================================================
-- FULL RESET
-- =====================================================

DROP TABLE IF EXISTS fights;
DROP TABLE IF EXISTS fighters;
DROP TABLE IF EXISTS divisions;
DROP TABLE IF EXISTS events;

-- If working inside a specific DB:
-- USE ufc;

-- =====================================================
-- SCHEMA
-- =====================================================

-- divisiones
CREATE TABLE divisions (
    weight_class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(50),
    gender ENUM('Male', 'Female') NOT NULL
);

-- peleadores
CREATE TABLE fighters (
    fighter_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    nickname VARCHAR(50),
    gender ENUM('Male', 'Female'),
    weight_class_id INT,
    country VARCHAR(50),
    CONSTRAINT fk_fighter_division 
        FOREIGN KEY (weight_class_id) REFERENCES divisions(weight_class_id)
);

-- eventos
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    edition_number INT,
    event_name VARCHAR(120) NOT NULL,
    event_date DATE,
    location_name VARCHAR(200)
);

-- peleas
CREATE TABLE fights (
    fight_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    fighter_red INT NOT NULL,
    fighter_blue INT NOT NULL,
    winner INT NULL,
    method VARCHAR(80),
    round_number INT,
    notes TEXT,
    CONSTRAINT fk_fights_event FOREIGN KEY (event_id) REFERENCES events(event_id),
    CONSTRAINT fk_fights_red FOREIGN KEY (fighter_red) REFERENCES fighters(fighter_id),
    CONSTRAINT fk_fights_blue FOREIGN KEY (fighter_blue) REFERENCES fighters(fighter_id),
    CONSTRAINT fk_fights_winner FOREIGN KEY (winner) REFERENCES fighters(fighter_id)
);

-- =====================================================
-- SEED DATA
-- =====================================================

-- divisiones
INSERT INTO divisions (class_name, gender) VALUES
('Flyweight', 'Male'),
('Bantamweight', 'Male'),
('Featherweight', 'Male'),
('Lightweight', 'Male'),
('Welterweight', 'Male'),
('Middleweight', 'Male'),
('Light Heavyweight', 'Male'),
('Heavyweight', 'Male'),
('Strawweight', 'Female'),
('Flyweight', 'Female'),
('Bantamweight', 'Female'),
('Featherweight', 'Female');

-- peleadores
INSERT INTO fighters (first_name, last_name, nickname, gender, weight_class_id, country) VALUES
('Conor', 'McGregor', 'The Notorious', 'Male', 4, 'Ireland'),
('Khabib', 'Nurmagomedov', 'The Eagle', 'Male', 4, 'Russia'),
('Amanda', 'Nunes', 'The Lioness', 'Female', 11, 'Brazil'),
('Jon', 'Jones', 'Bones', 'Male', 7, 'USA'),
('Valentina', 'Shevchenko', 'Bullet', 'Female', 10, 'Kyrgyzstan');

-- eventos
INSERT INTO events (edition_number, event_name, event_date, location_name) VALUES
(295, 'UFC 295: Prochazka vs Pereira', '2023-11-11', 'Madison Square Garden, New York'),
(296, 'UFC 296: Edwards vs Covington', '2023-12-16', 'Las Vegas, Nevada');

-- peleas
INSERT INTO fights (event_id, fighter_red, fighter_blue, winner, method, round_number, notes) VALUES
(1, 1, 2, 2, 'Submission', 4, 'Rear-naked choke'),
(1, 3, 5, 3, 'Decision', 5, 'Split decision'),
(2, 4, 1, 4, 'KO', 1, 'Head kick'),
(2, 2, 1, NULL, 'Scheduled', NULL, 'Fight has not occurred yet');
