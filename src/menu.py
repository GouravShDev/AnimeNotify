import userInput
import subscription, sys
import userInput, ctypes
from sys import exit
from os import name, system

def is_admin():
    # Check for windows if admin access is available
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def clear():
    # Clear terminal showing previous outputs
    system('cls' if name == 'nt' else 'clear')

def createMenu(api_path, icon_name, schedule_script):
    # Creates Menu which is shown to the user
    # And Taking input from user
    while(True):
        clear()
        print("*******AnimeNotify************")
        print("1. Subscribe")
        print("2. Remove Subscription")
        print("99. Quit")
        try:
            choice = int(input("Choice> "))
        except ValueError:
            print("Invalid Choice")
            continue
        if(choice == 1):
            if (is_admin() or name != 'nt'):
                anime_name=(userInput.read("Name")).lower()
                subscription.subscribe(api_path, anime_name)
            else:
                # Re-run the program with admin rights
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        elif (choice == 2):
            if (is_admin() or name != 'nt'):
                subscription.rmSubscribe()
            else:
                # Re-run the program with admin rights
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        elif(choice == 99):
            exit()
        else:
            print("Invalid Choice")