# global variables
from os import getcwd, name

PATH=""
API = "https://api.jikan.moe/v3" 
ICON_NAME="/resource/icon/icon" # just name no extension
SCHEDULE_SCRIPT=""

def init():
    if (name=="nt"):
        ch="//"
    else:
        ch="/"
    global PATH
    global ICON_NAME
    global SCHEDULE_SCRIPT
    PATH=getcwd()
    ICON_NAME=PATH+ch+ICON_NAME
    SCHEDULE_SCRIPT=PATH+ch+SCHEDULE_SCRIPT