#Luke Wilkins, 08-09-2023
#Professor Haas, CYBR410-T301
import mysql.connector
from mysql.connector import errorcode
#Displays list of books.
def show_books(my_cursor):
    print("Here is the list of your books")
    query = "select * from book;"
    my_cursor.execute(query)
    content = my_cursor.fetchall()

    for item in content:
        print(item)
#Displays book store location and store hours.
def show_locations(my_cursor):
    print("store locations")
    query = "select locale, city, hours from store"
    my_cursor.execute(query)
    content = my_cursor.fetchall()

    for item in content:
        print(item)
#checking if user ID is valid.
def validate_user(user_id):
    if isinstance(user_id, int) and 0 <= user_id < 4:
        return True
    else: return False
    
    # if user_id.isdigit() and (user_id > 3 or user_id < 0): 
    #     print("Sorry! This is not a valid user ID")
    #     return False
    # elif not user_id.isdigit():
    #     return False
    # else: return True
#Shows wishlist for users.
def show_wishlist(my_cursor, user_id):
    query = f"""SELECT user.user_id, first_name, last_name, book_name FROM user
    INNER JOIN wishlist ON user.user_id = wishlist.user_id
    INNER JOIN book ON book.book_id = wishlist.book_id
    WHERE user.user_id = {user_id};"""
    my_cursor.execute(query)
    for item in my_cursor.fetchall():
        print (item)
#Adds book to database
def show_books_to_add(my_cursor, user_id):
    query = f"""SELECT book_id, book_name FROM book
WHERE book_id NOT IN ( SELECT book_id FROM wishlist WHERE user_id
= {user_id});"""
    my_cursor.execute(query)
    for item in my_cursor.fetchall():
        print (item)
#Adds book to wishlist table
def add_book_to_wishlist(my_cursor, user_id, book_id):
    query = f"""INSERT INTO wishlist(user_id, book_id)
    VALUES ({user_id}, {book_id})"""
    my_cursor.execute(query)
#    my_cursor.commit()
#Displays account information for user.
def show_account_menu(my_cursor):

    print("Welcome to your account!")

    user_id = input("please input your user ID (Try 1, 2, or 3): ")
    if user_id.isdigit():
        user_id = int(user_id)
    else:
        print("Error. User ID should only be numerical. Try again.")
    while True:
        if (validate_user(user_id)):
            print(f"""

Welcome user ID {user_id} What would you like to do?
                                                  
1: Print your wishlist
2: Add a book
3: Back to the main menu""")
            user_input = input("Please select fron 1 to 3: ")
#        user_input = input("Please select fron 1 to 3: ")
            if user_input == "1":
                print("Here is your wishlist!")
                show_wishlist(my_cursor, user_id)
            if user_input == "2":
                print("The available books are:")
                show_books_to_add(my_cursor, user_id)
                user_select = input("Which book would you like to add to the wishlist?")
                add_book_to_wishlist(my_cursor, user_id, user_select)
            if user_input == "3":
                return
        else:
            print("Your ID is not valid. Please try again.")
            return


#This is the main function for printing the menu and connecting to the SQL database.
def show_menu():
    #Setting up the MySQL cofiguration.
    config = {
    "user": "root",
    "password": "Pr4iS3tH310rd!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
    }
    #Error handling.
    try:
        #Created a database and generated cursor.
        db = mysql.connector.connect(**config)
        cursor = db.cursor()    
        #================================================
        #Main part of the program.

        key = "none"
        while True:
            print("""
Welcome to WhatABook Program!
Main Menu:
Please select a key to get started!              

a: is for view books 
b: is for view store location 
c: view your account
q: is for quit
==========================================================                     
              """)
            key = input("Please select a key: ")
            if key == "a":
                show_books(cursor)
            if key == "b":
                show_locations(cursor)
            if key == "c":
                show_account_menu(cursor)
            if key == "q":
                print("Thank you for using the WhatABook Program!") 
                break
        db.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(" The supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(" The specified database does not exist")
        
        else:
            print(err)
    
    finally:
        db.close()

show_menu()
