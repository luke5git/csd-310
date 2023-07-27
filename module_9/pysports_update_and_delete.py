#Luke Wilkins 07-23-2023 
#Python Code for SQL connector errorcode

#import libararies for mysql
import mysql.connector
from mysql.connector import errorcode
#from mypassword import password
#import mypassword
#setting up congfig required by mysql
config = {
    "user": "root",
    "password": "Pr4iS3tH310rd!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#Trying to connect with mysql. If any errors are made, point them out.
try: 
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()
    print("--DISPLAYING TEAM RECORDS--")
    #================================================== Question 2 answered.  
    
    query = '''
    INSERT INTO player(first_name, last_name, team_id)
        VALUES('Cosmo', 'Holder of Starlight', 1)'''
    
    cursor.execute(query)  

    query = '''
    
    SELECT player_id, first_name, last_name, team_name
    FROM player
    INNER JOIN team
	ON player.team_id = team.team_id
    order by player_id;'''
    cursor.execute(query)
    teams = cursor.fetchall()
    print("--DISPLAYING PLAYERS AFTER INSERT--")
    for team in teams:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(team[0],team[1],team[2],team[3]))
    print()
#===================================================================================================================== Question 3 answered. 
    query = '''
    UPDATE player
    SET team_id = 2
    WHERE first_name = 'Cosmo' and last_name = 'Holder of Starlight';'''
    cursor.execute(query)  

    query = '''
    
    SELECT player_id, first_name, last_name, team_name
    FROM player
    INNER JOIN team
	ON player.team_id = team.team_id
                   order by player_id;'''
    cursor.execute(query)
    teams = cursor.fetchall()
    print("--DISPLAYING PLAYERS AFTER UPDATE--")
    for team in teams:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(team[0],team[1],team[2],team[3]))
    print()
#====================================================================================================================== Question 4 Answered
    query = '''
    DELETE FROM player
    WHERE first_name = 'Cosmo' and last_name = 'Holder of Starlight';'''
    cursor.execute(query)  

    query = '''
    
    SELECT player_id, first_name, last_name, team_name
    FROM player
    INNER JOIN team
	ON player.team_id = team.team_id
                   order by player_id;'''
    cursor.execute(query)
    teams = cursor.fetchall()
    print("--DISPLAYING PLAYERS AFTER DELETE--")
    for team in teams:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(team[0],team[1],team[2],team[3]))
    print()
    '''
    cursor = db.cursor()
    print("--DISPLAYING PLAYER RECORDS--")
    cursor.execute("SELECT * FROM PLAYER")
    
    players = cursor.fetchall()
    
    for player in players: 
        print("Player ID {}\nFirst Name:{}\nLast Name: {}\nTeam ID: {}\n".format(player[0],player[1],player[2],player[3]))
'''
                   




    input("\n\n Press any key to continue...\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplies username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    
    else:
        print(err)
    
finally:
    db.close()