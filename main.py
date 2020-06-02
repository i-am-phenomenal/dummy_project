import mysql.connector as mycon
import utils as utils
from os import system
import time

def handle_book_lend_cases(choice, member_id): 
    if choice == 1: 
        book_names = utils.display_book_names() 
        print("These are the list of available books. Enter one of the above names (Case sensitive) ")
        book_name = input()
        if book_name in book_names: 
            utils.lend_book(book_name, member_id)
            utils.display_book_lending_options()
            handle_book_lend_cases(int(input()), member_id)

        else: 
            print("The book name you entered is not correct. Please try again")
            time.sleep(3)
            handle_book_lend_cases(1, member_id)

    elif choice == 2: 
        system('cls')
        print("Enter the name of the book you want to return !!")
        book_name = input()
        if utils.check_book_validations(book_name, member_id):
            utils.return_book(book_name)
            utils.display_book_lending_options()
            handle_book_lend_cases(int(input()), member_id)

        else: 
            print("The book name you entered either doesnt exist or does not need to be entered !")
            time.sleep(2)
            handle_book_lend_cases(2, member_id)

    # elif choice == 3: 
        

    else: 
        print("Invalid Input")
        return 

def render_cases(choice):
    if choice == 1: 
        try:
            utils.create_database()
            utils.create_table()

        except Exception as e:
            print(e)
            print("UNABLE TO CREATE TABLE !!")

        finally: 
            utils.input_and_save_user()
            print("Your membership has been created !! ")
            print("Have a nice day !")
            utils.display_main_menu()
            render_cases(int(input()))

    elif choice == 2:
        member_uuid = utils.login_member()
        if member_uuid: 
        # We need to write a function to check whether this user has been lended any books
            utils.display_book_lending_options()
            handle_book_lend_cases(int(input()), member_uuid)

        else: 
            print("User not found ! Please try again ")


    elif choice == 3: 
        exit(0)

    else: 
        print("Invalid Input !!")



utils.display_main_menu()
render_cases(int(input()))
