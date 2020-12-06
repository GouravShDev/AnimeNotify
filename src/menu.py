import userInput
import subscription
import userInput
from sys import exit
from os import name, system

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
            anime_name=(userInput.read("Name")).lower()
            subscription.subscribe(api_path, anime_name)
        elif (choice == 2):
            subscription.rmSubscribe()
        elif(choice == 99):
            exit()
        else:
            print("Invalid Choice")