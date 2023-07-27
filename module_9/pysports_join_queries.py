#Luke Wilkins 07-27-2023 
#Professor Haas CYBR410-T301
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
#getting information from SQL database
    cursor = db.cursor()
    print("--DISPLAYING TEAM RECORDS--")
    cursor.execute("""SELECT player_id, first_name, last_name, team_name
    FROM player
    RIGHT OUTER JOIN team
	ON player.team_id = team.team_id
                   order by player_id;""")

    teams = cursor.fetchall()

    for team in teams:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(team[0],team[1],team[2],team[3]))
    '''
    cursor = db.cursor()
    print("--DISPLAYING PLAYER RECORDS--")
    cursor.execute("SELECT * FROM PLAYER")
    
    players = cursor.fetchall()
    
    for player in players: 
        print("Player ID {}\nFirst Name:{}\nLast Name: {}\nTeam ID: {}\n".format(player[0],player[1],player[2],player[3]))
'''
                   




    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplies username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    
    else:
        print(err)
    
finally:
    db.close()