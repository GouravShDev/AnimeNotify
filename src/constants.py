# global variables
from os import getcwd, name

PATH=""
API = "https://api.jikan.moe/v3" 
ICON_NAME="/resource/icon/icon" # just name no extension
SCHEDULE_SCRIPT="/scheduledscript.pyw"
RELATED="/resource/data/related.anime"
DATE="/resource/data/lastruntime.time"
SUBSCRIBED="/resource/data/subscribed.scb"
BASH_SCRIPT="/resource/data/script.sh"
LOG="/resource/logs/log.txt"
TMP="/resource/temp/tmpfile.txt"

def correctPath(stri):
        return(stri.replace("/", "\\"))
    
def init():
    global PATH
    global ICON_NAME
    global SCHEDULE_SCRIPT
    global RELATED
    global DATE
    global SUBSCRIBED
    global BASH_SCRIPT
    global LOG
    global TMP
    PATH=getcwd()
    LOG=PATH+LOG
    BASH_SCRIPT=PATH+BASH_SCRIPT
    SUBSCRIBED=PATH+SUBSCRIBED
    ICON_NAME=PATH+ICON_NAME
    SCHEDULE_SCRIPT=PATH+SCHEDULE_SCRIPT
    RELATED=PATH+RELATED
    DATE=PATH+DATE
    TMP=PATH+TMP
    if (name=="nt"):
        PATH=correctPath(PATH)
        ICON_NAME=correctPath(ICON_NAME) + '.ico'
        SCHEDULE_SCRIPT=correctPath(SCHEDULE_SCRIPT)
        RELATED=correctPath(RELATED)
        DATE=correctPath(DATE)
        SUBSCRIBED=correctPath(SUBSCRIBED)
        BASH_SCRIPT=correctPath(BASH_SCRIPT)
        LOG=correctPath(LOG)
        TMP=correctPath(TMP)