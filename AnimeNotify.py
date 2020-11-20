# Documentation of Api : https://jikan.docs.apiary.io/

from requests import get
# Library to make get Request
from json import loads
# Convert json String to python Object
from sys import exit


apiPath = "https://api.jikan.moe/v3" 

def loadJson(url):
    # Using request's get method to get data
    try:
        response = get(url)
    except Exception as e:
        print("Error: " + str(e))
        exit(1)
    if(response.status_code == 200):
        return loads(response.content)
    else:
        print("Error: " + str(response.status_code) + " : "+ response.reason)
        exit(1)


def searchAnime():
    # Ask User name of Anime
    # Prepare Url for searching Anime titles
    animeName = input("Enter Name of anime: ")
    subUrl = "/search/anime?q=%s/Zero&page=1"%animeName
    dict = loadJson(apiPath + subUrl)
    # TODO
    # Shivanshu
    #jsonParser(dict)

def getChoice():
    #Method to get user Input
    try:
        choice = int(input("Choice> "))
    except ValueError:
        print("Not a valid input")
        return getChoice()
    return choice


def menu():
    # Creates Menu which is shown to the user
    # And Taking input from user
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
    # calling menu function
    menu()

if __name__ == "__main__":
    # Call main when this python file is not imported 
    # to other python file
    main()