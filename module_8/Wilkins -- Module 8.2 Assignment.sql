SHOW DATABASES;
USE pysports;

-- Create the team table
CREATE TABLE team (

team_id INT NOT NULL AUTO_INCREMENT,
team_name VARCHAR(75) NOT NULL,
mascot VARCHAR(75) NOT NULL,
PRIMARY KEY(team_id)
);
SELECT * FROM TEAM;
DESCRIBE TEAM;

-- Create the player table and set the foreign key
CREATE TABLE player (
player_id INT NOT NULL AUTO_INCREMENT,
first_name VARCHAR(75) NOT NULL,
last_name VARCHAR(75) NOT NULL,
team_id INT NOT NULL,
PRIMARY KEY(player_id),
CONSTRAINT fk_team
FOREIGN KEY(team_id)
REFERENCES team(team_id)
);
INSERT INTO team(team_name, mascot)
VALUES('Team Nebula', 'Black Hole');
SELECT team_name, mascot FROM TEAM
WHERE team_id = 2;