-- divisiones primero
INSERT INTO divisions (class_name, gender)
VALUES 
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
INSERT INTO fighters 
(first_name, last_name, nickname, gender, weight_class_id, country)
VALUES
('Conor', 'McGregor', 'The Notorious', 'Male', 4, 'Ireland'),
('Amanda', 'Nunes', 'The Lioness', 'Female', 11, 'Brazil'),
('Jon', 'Jones', 'Bones', 'Male', 7, 'USA');

-- eventos
INSERT INTO events (edition_number, event_name, event_date, location_name)
VALUES
(295, 'UFC 295: Prochazka vs Pereira', '2023-11-11', 'Madison Square Garden, New York'),
(296, 'UFC 296: Edwards vs Covington', '2023-12-16', 'Las Vegas, Nevada');

-- peleas 
INSERT INTO fights
(event_id, fighter_red, fighter_blue, winner, method, round_number, notes)
VALUES
(1, 3, 1, 3, 'Submission', 2, 'Rear-naked choke'),
(1, 2, 1, NULL, 'KO', 1, 'Example: no winner yet (future fight)');