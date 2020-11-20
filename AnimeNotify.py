# Documentation of Api : https://jikan.docs.apiary.io/

from requests import get
# Library to make get Request
from json import loads
# Convert json String to python Object
from sys import exit
# exit with a exit code
from pynotifier import Notification
# create notification
from os import name, getcwd, system
# get name of os, execute shell, get cwd
from crontab import CronTab
# schedule script

API = "https://api.jikan.moe/v3" 
ICON_NAME="" # just name no extension
SCHEDULE_SCRIPT=""

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

def jsonParser(dic):
    # takes dict as param
    # dic has json data
    for result in dic["results"]:
        print(result["title"])

def subscribeAnime(api_path):
    # Ask User name of Anime
    # Prepare Url for searching Anime titles
    anime_name = input("Enter Name of anime: ")
    sub_url = "/search/anime?q=%s/Zero&page=1"%anime_name
    dic = loadJson(api_path + sub_url)
    jsonParser(dic)
    print(jsonParser(dic))

def subscribeManga(api_path):
    pass

def subscribePerson(api_path):
    pass

def subscribeStudio(api_path):
    pass

def rmSubscribe():
    pass

def schedule(schedule_script):
    # param, name of script to schedule
    # check if winows or linux and call
    # corresponding func
    if (name=='nt'):
        scheduleWindows(schedule_script)
    else:
        scheduleLinux(schedule_script)

def scheduleLinux(schedule_script):
    # takes name of script to schedule on linux
    # schedule a ps in linux using crontab
    # schedule script on every boot
    cron=CronTab()
    cmd='export DISPLAY=:0.0 && '
    python3_path=system('which python3')
    cmd+=(python3_path+" "+getcwd()+"/"+schedule_script) 
    schedule=cron.new(command=cmd, comment='Anime News Notification')
    schedule.every_reboot()
    cron.write()

def rmScheduleLinux():
    # remove from task scheduler linux
    cron=CronTab()
    jobs=cron.find_comment("Anime News Notification")
    for job in jobs:
        cron.remove(job)

def rmScheduleWindows():
    pass

def scheduleWindows():
    pass

def menu(api_path, icon_name, schedule_script):
    # Creates Menu which is shown to the user
    # And Taking input from user
    while(True):
        print("*******AnimeNotify************")
        print("1. Subscribe Anime ")
        print("2. Subscribe Manga")
        print("3. Subscribe Person")
        print("4. Subscribe Studio")
        print("Remove Subscription")
        print("99. Quit")

        choice = int(input("Choice> "))

        if(choice == 1):
            subscribeAnime(api_path)
        elif (choice == 2):
            subscribeManga(api_path)
        elif (choice == 3):
            subscribePerson(api_path)
        elif (choice == 4):
            subscribeStudio(api_path)
        elif (choice == 5):
            rmSubscribe()
        elif(choice == 99):
            exit()
        else:
            print("Invalid Choice")
            
def main():
    # calling menu function
    menu(API, ICON_NAME, SCHEDULE_SCRIPT)

if __name__ == "__main__":
    # Call main when this python file is not imported 
    # to other python file
    main()