# Documentation of Api : https://jikan.docs.apiary.io/

from requests import get
# Library to make get Request
from json import loads
# Convert json String to python Object
from sys import exit


apiPath = "https://api.jikan.moe/v3" 


def searchAnime():
    animeName = input("Enter Name of anime: ")
    subUrl = "/search/anime?q=%s/Zero&page=1" % animeName
    print(apiPath + subUrl)


def getChoice():
    #Method to get user Input
    try:
        choice = int(input("Choice> "))
    except ValueError:
        print("Not a valid input")
        return getChoice()
    return choice


def menu():
    while(True):
        print("*******AnimeNotify************")
        print("1. Search Anime ")
        print("2. Quit")

        choice = getChoice()

        if(choice == 1):
            searchAnime()
        elif(choice == 2):
            exit()
            

def main():
    menu()

if __name__ == "__main__":
    main()