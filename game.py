import getpass
import os
from pathlib import Path
import platform
import random

import sys
import time
import gtn
import ttt


global login_user
global users_folder
users_folder = Path("users")
users_folder.mkdir(exist_ok=True)
login_user = ""
admin = False
def Mac():    
    print("WARNING: Mac user detected.")
    time.sleep(1)
    print("This game does not allow Mac users.")
    time.sleep(1)
    print("BANNING IN 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Goodbye. 👋🍏💥")
    file_name = f"{login_user}.mgtgterminalgameuser"
    file_path = users_folder / file_name
    
    with open(file_path, "r") as file:
        lines = file.readlines()
        lines[1] = "Ban\n"
    with open(file_path, "w") as file:
        file.writelines(lines)
    sys.exit()
def DisplayTitle():
    print("Terminal Game \n [1] Signup \n [2] Login \n [3] Exit \n")
    number = input("Which one? ")
    if (number == "1"):
        # Ask the user for their name
        username = input("Enter your username: ")
        passwd = getpass.getpass("Enter your password: ")

# Build the file name using their input
        file_name = f"{username}.mgtgterminalgameuser"

# Set the path to the users folder
        users_folder = Path("users")
        users_folder.mkdir(exist_ok=True)

# Create the full path
        file_path = users_folder / file_name

# Write to the file
        with open(file_path, "w") as file:
            file.write(f"{passwd}\n")
            file.write("Peasant")

        print(f"File created at: {file_path}")
        number = ""
        DisplayTitle()
        
    if (number == "2"):
        #old coming soon line
        global login_user
        login_user = input("user: ")
        login_pwd = getpass.getpass("pwd: ")
        file_name = f"{login_user}.mgtgterminalgameuser"

# Set the path to the users folder
        users_folder = Path("users")
        users_folder.mkdir(exist_ok=True)
        file_path = users_folder / file_name
        with open(file_path, "r") as file:
            true_password = file.readline().strip()
            login_status = file.readline().strip()
        if (login_pwd == true_password and not login_status == "Ban" and not platform.system() == "Darwin"):
            print("You have been logged in")
            DisplayLoggedInTitle()
        elif(login_pwd !=true_password):
            print("you are a hacker :(")
            sys.exit()
            DisplayTitle()
        elif(login_status == "Ban"):
            print("By the way, if you did not know, your account is banned")
            sys.exit()
        elif platform.system == "Darwin":
            Mac()
        
        number = ""
        DisplayTitle()
    if (number == "3"):
        sys.exit()

    number = ""
    DisplayTitle()

def DisplayLoggedInTitle():
    global admin
    print("Terminal Game \n [1] Signup \n [2] Exit \n [3] Games \n [4] Leaderboards \n [5] Admin \n")
    number = input("Which one? ")
    if (number == "1"):
        # Ask the user for their name
        username = input("Enter your username: ")
        passwd = getpass.getpass("Enter your password: ")

# Build the file name using their input
        file_name = f"{username}.mgtgterminalgameuser"

# Set the path to the users folder
        users_folder = Path("users")
        users_folder.mkdir(exist_ok=True)

# Create the full path
        file_path = users_folder / file_name

# Write to the file
        with open(file_path, "w") as file:
            file.write(f"{passwd}\n")
            file.write("Peasant")

        print(f"File created at: {file_path}")
        number = ""
        DisplayLoggedInTitle()
        
    
    if (number == "2"):
        sys.exit()
    if (number == "3"):
        print("Coming Soon! \n \n \n \n \n \n \n \n \n \n \n \n")
        print("[1] Tic Tac Toe \n[2] Guess The Number \n")
        number_for_games = input("game: ")
        if (number_for_games == "1"):            
            ttt.PlayTicTacToeTimed(login_user)
            
        if (number_for_games == "2"):
            gtn.CreateNum()
            gtn.Guess()
    if (number == "4"):
        print("Leaderboards \n [1] Tic-Tac-Toe \n [2] Guess The Number \n")
        number_for_leaderboards = input("which one? ")
        if (number_for_leaderboards == "1"):
            leaderboard_name = "ttt_highscore.mgtgterminalgamehighscoreleaderboard"
            leaderboards_folder = Path("leaderboards")
            leaderboard_path = leaderboards_folder / leaderboard_name
            with open(leaderboard_path, "r") as file:
                leaderboard_data = file.read()
                print(leaderboard_data)
        if (number_for_leaderboards == "2"):
            leaderboard_name = "gtn_highscore.mgtgterminalgamehighscoreleaderboard"
            leaderboards_folder = Path("leaderboards")
            leaderboard_path = leaderboards_folder / leaderboard_name
            with open(leaderboard_path, "r") as file:
                leaderboard_data = file.read()
                print(leaderboard_data)
    if (number == "5"):
        print("Checking if admin...")
        file_name = f"{login_user}.mgtgterminalgameuser"

# Set the path to the users folder
        users_folder = Path("users")
        users_folder.mkdir(exist_ok=True)
        file_path = users_folder / file_name
        with open(file_path, "r") as file:
            admin_check_l1 = file.readline().strip()
            admin_check_l2 = file.readline().strip()
        if (admin_check_l2 == "admin"):
            admin = True
        else:
            admin = False
        time.sleep(2.5)
        if(admin == True):
            file_name = f"{login_user}.mgtgterminalgameuser"

# Set the path to the users folder
            users_folder = Path("users")
            users_folder.mkdir(exist_ok=True)

# Create the full path
            file_path = users_folder / file_name
            print("Admin Stuff \n [1] Ban Panel \n [2] Adminify \n [3] De-admin")
            number_for_admin = getpass.getpass("admin number (note: number = hidden): ")
            if (number_for_admin == "1"):
                to_ban = getpass.getpass("person to ban (note: person = hidden): ")
                file_name = f"{to_ban}.mgtgterminalgameuser"
                file_path = users_folder / file_name
                with open(file_path, "r") as file:
                    lines = file.readlines()
                lines[1] = "Ban\n"
                with open(file_path, "w") as file:
                    file.writelines(lines)
            if (number_for_admin == "2"):
                to_adminify = getpass.getpass("person to adminify (note: person = hidden): ")
                file_name = f"{to_adminify}.mgtgterminalgameuser"
                file_path = users_folder / file_name
                with open(file_path, "r") as file:
                    lines = file.readlines()
                lines[1] = "admin\n"
                with open(file_path, "w") as file:
                    file.writelines(lines)
            if (number_for_admin == "3"):
                to_deadminify = getpass.getpass("person to de-admin (note: person = hidden): ")
                file_name = f"{to_deadminify}.mgtgterminalgameuser"
                file_path = users_folder / file_name
                with open(file_path, "r") as file:
                    lines = file.readlines()
                lines[1] = "Peasant\n"
                with open(file_path, "w") as file:
                    file.writelines(lines)
        else:
            file_name = f"{login_user}.mgtgterminalgameuser"

# Set the path to the users folder
            users_folder = Path("users")
            users_folder.mkdir(exist_ok=True)

# Create the full path
            file_path = users_folder / file_name
            print("admin_hack = True")
            with open(file_path, "r") as file:
                pwd = file.readline().strip()
                non_admin_status = file.readline().strip()
            if(non_admin_status == "Warning"):
                with open(file_path, "r") as file:
                    lines = file.readlines()
                lines[1] = "Ban\n"
                with open(file_path, "w") as file:
                    file.writelines(lines)
            elif(non_admin_status == "Peasant"):
                with open(file_path, "r") as file:
                    lines = file.readlines()
                lines[1] = "Warning\n"
                with open(file_path, "w") as file:
                    file.writelines(lines)
                print("HACKER DETECTED! INITIATING COUNTERATTACK...")

# Funny prank: Spam random letters on the screen
                for _ in range(50):
                    random_letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=50))
                    print(random_letters)
                    time.sleep(0.05)

                # Then clear the screen (optional)
                os.system('cls' if os.name == 'nt' else 'clear')

                print("You have been banned. Goodbye. 😎")
                time.sleep(2)
            sys.exit()
            quit()



            



    number = ""
    DisplayLoggedInTitle()

DisplayTitle()