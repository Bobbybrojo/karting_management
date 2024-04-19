create database GoKarting;
use GoKarting;

create table race(
	race_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    race_date DATE NOT NULL,
    UNIQUE (race_id)
);

create table racer(
	username VARCHAR(32) PRIMARY KEY NOT NULL,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32) NOT NULL,
    UNIQUE (username)
);

create table stint(
	stint_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    username VARCHAR(32) NOT NULL,
    race_id  INT NOT NULL,
    position INT NOT NULL,
    best_lap_time TIME NOT NULL,
    FOREIGN KEY (race_id) REFERENCES race(race_id)
		ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (username) REFERENCES racer(username)
		ON UPDATE CASCADE ON DELETE CASCADE
    
);

create table employee(
	employee_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32) NOT NULL
);

create table energy_drink(
	color ENUM("RED", "BLUE", "YELLOW", "GREEN") PRIMARY KEY NOT NULL,
    quantity INT NOT NULL,
    UNIQUE (color)
);

-- PROCEDURE TO ENTER A NEW RACER
DROP PROCEDURE create_racer;
DELIMITER $$
CREATE PROCEDURE create_racer(username_g VARCHAR(32), first_name_g VARCHAR(32), last_name_g VARCHAR(32))
	BEGIN
        INSERT INTO racer VALUES(username_g, first_name_g, last_name_g);
    END $$
DELIMITER ;

CALL create_racer ('maxvstap', 'max', 'verstappen');
CALL create_racer ('Hammy', 'lewis', 'hamilton');
CALL create_racer ('sperez', 'sergio', 'perez');

SELECT * from racer;
DELETE FROM RACER WHERE username = "";

-- PROCEDURE TO ENTER A NEW RACE
DROP PROCEDURE create_race;
DELIMITER $$
CREATE PROCEDURE create_race(race_id_g INT, date_g DATE)
	BEGIN
        INSERT INTO race VALUES(race_id_g, date_g);
    END $$
DELIMITER ;

-- PROCEDUREs TO GET Racing Stints
DROP PROCEDURE get_stints;
DELIMITER $$
CREATE PROCEDURE get_stints()
	BEGIN
        SELECT race.race_date, stint.username, stint.race_id, stint.position, stint.best_lap_time FROM stint 
        JOIN race ON race.race_id = stint.race_id
        ORDER BY race.race_date;
    END $$
DELIMITER ;
CALL get_sint();

DROP PROCEDURE get_stints_by_racer;
DELIMITER $$
CREATE PROCEDURE get_stints_by_racer(username_given VARCHAR(32))
	BEGIN
        SELECT race.race_date, stint.username, stint.race_id, stint.position, stint.best_lap_time FROM stint
        JOIN race ON race.race_id = stint.race_id
        WHERE username = username_given ORDER BY race.race_date DESC;
    END $$
DELIMITER ;

DROP PROCEDURE get_stints_by_race_id;
DELIMITER $$
CREATE PROCEDURE get_stints_by_race_id(race_id_given int)
	BEGIN
        SELECT race.race_date, stint.username, stint.race_id, stint.position, stint.best_lap_time FROM stint 
        JOIN race ON race.race_id = stint.race_id
        WHERE stint.race_id = race_id_given ORDER BY position;
    END $$
DELIMITER ;


DELETE FROM race WHERE 1=1;
-- INSERT Races into race
INSERT INTO race VALUES (1, '2024-01-01');
INSERT INTO race VALUES (2, '2024-01-02');
INSERT INTO race VALUES (3, '2024-01-03');
INSERT INTO race VALUES (4, '2024-01-04');
INSERT INTO race VALUES (5, '2024-01-05');
INSERT INTO race VALUES (6, '2024-01-05');
INSERT INTO race VALUES (7, '2024-01-06');
INSERT INTO race VALUES (8, '2024-01-07');
INSERT INTO race VALUES (9, '2024-01-08');
INSERT INTO race VALUES (10, '2024-01-09');
INSERT INTO race VALUES (11, '2024-01-10');
INSERT INTO race VALUES (12, '2024-01-10');

SELECT * FROM race;


-- Insert Stints
DELETE FROM stint WHERE 1=1;
-- Stintid, Username, Raceid, position, time
INSERT INTO stint VALUES (0, 'Hammy', 1, 1, "00:01:25");
INSERT INTO stint VALUES (0, 'sperez', 1, 2, "00:01:27");
INSERT INTO stint VALUES (0, 'maxvstap', 1, 3, "00:01:28");

INSERT INTO stint VALUES (0, 'Hammy', 2, 1, "00:01:28");
INSERT INTO stint VALUES (0, 'sperez', 2, 2, "00:01:30");
INSERT INTO stint VALUES (0, 'maxvstap', 2, 3, "00:01:31");

INSERT INTO stint VALUES (0,'Hammy', 3, 3, "00:01:30");
INSERT INTO stint VALUES (0, 'sperez', 3, 1, "00:01:25");
INSERT INTO stint VALUES (0, 'maxvstap', 3, 2, "00:01:27");

-- Insert energy drinks into energy_drink
DELETE FROM energy_drink WHERE 1=1;
INSERT INTO energy_drink VALUES ("RED", 10);
INSERT INTO energy_drink VALUES ("BLUE", 10);
INSERT INTO energy_drink VALUES ("YELLOW", 10);
INSERT INTO energy_drink VALUES ("GREEN", 10);

-- Insert Employees
DELETE FROM employee WHERE 1=1;
INSERT INTO employee VALUES (0, "Bobby", "Rojo");
INSERT INTO employee VALUES (0, "John", "Smith");
INSERT INTO employee VALUES (0, "Lazy", "Susan");























