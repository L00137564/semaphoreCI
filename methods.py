# Author: Owen Lyons    # Date: 21/07/17      # Program: methods.py
###########################################################################################
# List of methods that can be used with Assignment 1
###########################################################################################
import datetime
import os

#####################################################
def print_menu(dict): # Loops through the dict and prints the keys and values beside each other
    for key, value in dict.items():
        print(key, value)

#######################################################
def nice_print(str1, dict1): # prints the results in a tidy manner
    print("||" + str1 ,  " "*12, "||")
    print("||", "¬"*40, " "*23, "||")
    for k, v in dict1.items():
        print("||  ", k, ': ', v, " " * (57 - (len(str(k)) + len(str(v)))), "||")
    print("||" + " " * 65, "||")

######################################################
def menu_header(str1): # prints the menu headers
    print("")
    print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
    print(str1)
    print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
    print("")

######################################################
def date_time(): # prints current date and time
    project_init_date = datetime.datetime.now()

    date = str(project_init_date)[:-15] # splices date for use in the string below
    time = str(project_init_date)[11:19] # splices time for use in the string below

    date_time = "Date: " + date + " | Time: "+ time # more aesthetic that printing 'datetime()'

    return date_time

#######################################################

# Function that displays a menu, accepts the users input as an option
# and writes the chosen value to a dictionary (to be printed at the end)
def menu_option(menu_dict, str, empty_dict, str1):
    try:
        print_menu(menu_dict)
        option = user_int(str)

        for key, value in menu_dict.items():
            if int(option) == key:
                empty_dict[str1] = value
    except ValueError:
        print("ERROR - Invalid Option")

###########################################################

# If input is not a number - Handle Error
def user_int(question):
    try:
        return int(input(question))
    except ValueError:
        return user_int("ERROR - Invalid Input")



###########################################################