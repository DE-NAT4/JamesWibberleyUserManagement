import os
from pathlib import Path

def menu():
    print("1 = ADD USER")
    print("2 = VIEW USERS ACTIVE/DISABLED")
    print("3 = ENABLE / DISABLE USERS")
    print("4 = LOGIN")
    print("0 = EXIT APP")

    choice = input(": ")

    if (int(choice) < 5):
        return (int(choice))
    else:
        print("Invalid choice")


def adduser(userlist):
    username = input("Enter username: ")
    userpass = input("Enter password: ")
    userstatus = "enabled"

    userlist[username] = {
        "password": userpass,
        "status": userstatus
    }

def listusers(userlist):
    
    print("********")

    for username, useritem in userlist.items():
        if (useritem['status'] == "enabled"):
            print(f"Username: {username}")
            print(f"Password: {useritem['password']}")
            print(f"Status: {useritem['status']}")

    print("********")

    for username, useritem in userlist.items():
        if (useritem['status'] == "disabled"):
            print(f"Username: {username}")
            print(f"Password: {useritem['password']}")
            print(f"Status: {useritem['status']}")

def enabledisableusers(userlist):
    print("enabledisableusers")

    listusers(userlist)
    userchoice = input("Enable or disable? ")

    if (userchoice == "enable"):
        name = input("Enter the username to enable: ")
        userlist[name]["status"] = "enabled"
    elif (userchoice =="disable"):
        name = input("Enter the username to disable: ")
        userlist[name]["status"] = "disabled"
        
users = {
}

def userlogin(userlist):
    username = input("Enter username: ")

    if username in userlist:
        userpass = input("Enter password: ")
        if (userlist[username]["password"] == userpass):
            print("login successful!")
        else:
            print("login failed :(")

def loadusers(filename):
    print("loadusers")
    
    userlist = {}

    try:
        with open(filename, "r") as f:
            userlist = eval(f.read())
            return(userlist)
    except FileNotFoundError as fnfe:
        print(f"File not found {fnfe}")
        return {}
    
def saveusers(filename, userlist):
    print("saveusers")
    print(str(userlist))

    try:

        with open(filename, "w") as f:
            f.write(str(userlist))
    except FileNotFoundError as fnfe:
        print(f"file not found {fnfe}")

#Main part of the program starts here

#file_path = Path(__file__).resolve().parent.parent / "data" / "users.txt"
file_path = "../data/users.txt"

menuchoice = 0

keep_running = True

users = loadusers(file_path)

while keep_running:
    menuchoice = menu()

    if (menuchoice == 0):
        keep_running = False

    match menuchoice:
        case 1:
            adduser(users)
        case 2:
            listusers(users)
        case 3:
            enabledisableusers(users)
        case 4:
            userlogin(users)

saveusers(file_path, users)