import jsonparser
import collector
import filehandlers
import menu
from os import system, name
import constants
import schedule
from sys import exit

def subscribe(api_path, anime_name):
    # Prepare Url for searching Anime titles
    filehandlers.writeLastRunDate()
    i = collector.collectMalID(api_path, anime_name)
    filehandlers.writeRelatedMalID(collector.collectRelatedMalID(api_path, i))
    if (schedule.checkSubscribed()==0):
        schedule.schedule()

def rmSubscribe():
    menu.clear()
    choice=input("Remove all subscriptions (y/n): ")
    if (choice=='y'):
        if (name!='nt'):
            system("rm " + constants.RELATED)
            system("rm "+constants.DATE)
        else:
            system("del "+constants.RELATED)
            system("del "+constants.DATE)
        schedule.rmSchedule()
        exit(0)
    else:
        menu.clear()
        choice=input("Name to unsubscribe: ")
        filehandlers.rmSpecific(choice.lower())