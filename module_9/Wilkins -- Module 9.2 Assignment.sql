SELECT player_id, first_name, last_name, team_name
FROM player
INNER JOIN team
	ON player.team_id = team.team_id;

SELECT player_id, first_name, last_name, team_name
FROM player
LEFT OUTER JOIN team
	ON player.team_id = team.team_id;

SELECT player_id, first_name, last_name, team_name
FROM player
RIGHT OUTER JOIN team
	ON player.team_id = team.team_id;
    
SELECT first_name, last_name
FROM player
WHERE player_id = 3;