# Author: Owen Lyons
# Date: 25/07/17
# Program: github_menu.py
###################################################################################################
###################################################################################################

from github import Github
from methods import *

quest_dict = {1: "Yes", 2: "No"}

menu_dict = {1: "List Repositories", 2: "Create a Repository", 3: "Choose Repository",
             4: "Display current Repository", 5: "Delete Repo", 0: "Exit"}

#######################################################################
#######################################################################

def print_menu(dict):
    for key, value in dict.items():
        print(key, value)

##############################################
def github_menu():
    # user_name = input("Enter username: ")
    # pass_word = input("Enter password: ")
    # g = Github(user_name, pass_word)

    g = Github("06891da0a4b2306b0f882b92835b0c3d12cc35f3")
    repo_name = None
    repo_dict = {}

    option = None
    while option != 0:

        menu_header("GitHub Menu")
        print_menu(menu_dict)
        print("")
        option = input("Choose: ")
        print("")
        #####################################################
        if int(option) == 1:
            repo_dict = {}
            i = 1
            for repo in g.get_user().get_repos():
                repo_dict[i] = str(repo.name)
                i = i + 1

            print("")

            print_menu(repo_dict)
        ####################################################
        elif int(option) == 2:
            repo_name = input("Enter new repository name: ")
            user = g.get_user()
            user.create_repo(repo_name)

        ####################################################
        elif int(option) == 3:

            i = 1
            for repo in g.get_user().get_repos():
                repo_dict[i] = str(repo.name)
                i = i + 1

            print("")
            for k, v in repo_dict.items():
                print(k, v)

            option = input("Choose Repository: ")
            for k, v in repo_dict.items():
                if int(option) == k:
                    repo_name = v

                    print("")
                    print(repo_name)

        ####################################################
        elif int(option) == 4:
            print(repo_name)

        ####################################################

        elif int(option) == 5:
            flag = False
            i = 1
            for repo in g.get_user().get_repos():
                repo_dict[i] = str(repo.name)
                i = i + 1

            print("")
            for k, v in repo_dict.items():
                print(k, v)

            option = input("Choose Repository to delete: ")
            for k, v in repo_dict.items():
                if int(option) == k:
                    repo_name = v
                    repo_path = 'L00137564/' + str(repo_name)
                    #print(repo_path)

                    print_menu(quest_dict)
                    print("Are you sure you want to delete: " + str(repo_path) + " ?")
                    option = input()
                    answer = quest_dict[int(option)]

                    if answer == "Yes":
                        flag = True
                        repo = g.get_repo(repo_path)
                        repo.delete()
                    else:
                        break

            if flag == True:
                del repo_dict[int(option)]

        ######################################################

        elif int(option) == 0:
            break

    return repo_name

#######################################################################################

github_menu()









