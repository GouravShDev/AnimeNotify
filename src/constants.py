# global variables
from os import getcwd, name

PATH=""
API = "https://api.jikan.moe/v3" 
ICON_NAME="/resource/icon/icon" # just name no extension
SCHEDULE_SCRIPT=""
RELATED="/resource/data/related.anime"
DATE="/resource/data/lastruntime.time"

def correctPath(stri):
        return(stri.replace("/", "\\"))
    
def init():
    global PATH
    global ICON_NAME
    global SCHEDULE_SCRIPT
    global RELATED
    global DATE
    PATH=getcwd()
    ICON_NAME=PATH+"/"+ICON_NAME
    SCHEDULE_SCRIPT=PATH+"/"+SCHEDULE_SCRIPT
    RELATED=PATH+"/"+RELATED
    DATE=PATH+"/"+DATE
    if (name=="nt"):
        PATH=correctPath(PATH)
        ICON_NAME=correctPath(ICON_NAME)
        SCHEDULE_SCRIPT=correctPath(SCHEDULE_SCRIPT)
        RELATED=correctPath(RELATED)
        DATE=correctPath(DATE)