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
        print("2. Subscribe Manga")
        print("3. Subscribe Person")
        print("4. Subscribe Studio")
        print("5. Remove Subscription")
        print("99. Quit")
        choice = int(input("Choice> "))
        if(choice == 1):
            anime_name=userInput.read("Anime")
            subscription.subscribeAnime(api_path, anime_name)
        elif (choice == 2):
            manga_name=userInput.read("Manga")
            subscription.subscribeManga(api_path, manga_name)
        elif (choice == 3):
            person_name=userInput.read("Person")
            subscription.subscribePerson(api_path, person_name)
        elif (choice == 4):
            studio_name=userInput.read("Studio")
            subscription.subscribeStudio(api_path, studio_name)
        elif (choice == 5):
            subscription.rmSubscribe()
        elif(choice == 99):
            exit()
        else:
            print("Invalid Choice")