UPDATE player
SET team_id = 2,
	first_name = 'Goron',
    last_name = 'Destroyer of Galaxies'
WHERE first_name = 'Goron';

DELETE FROM player
WHERE first_name = 'Goron';

INSERT INTO player (first_name, last_name, team_id)
	VALUES('Goron', 'Team Worm Hole', 1);

SHOW DATABASES;
USE pysports;
SELECT * FROM player;