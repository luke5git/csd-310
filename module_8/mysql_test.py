#Luke Wilkins 07-23-2023 
#Professor Haas
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
