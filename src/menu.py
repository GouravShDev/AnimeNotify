import userInput
import subscription
import userInput
from sys import exit


def createMenu(api_path, icon_name, schedule_script):
    # Creates Menu which is shown to the user
    # And Taking input from user
    while(True):
        print("*******AnimeNotify************")
        print("1. Subscribe Anime ")
        print("2. Remove Subscription")
        print("99. Quit")
        choice = int(input("Choice> "))
        if(choice == 1):
            anime_name=userInput.read("Anime")
            subscription.subscribeAnime(api_path, anime_name)
        elif (choice == 2):
            subscription.rmSubscribe()
        elif(choice == 99):
            exit()
        else:
            print("Invalid Choice")