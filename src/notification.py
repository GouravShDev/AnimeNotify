from os import system, name
import constants
# show notification

def genNotificationWindows(title, descr, icon, link):
    pass

def genNotificationLinux(title, descr, icon, link):
    s="notify-send \'"+title+"\' \'"+descr+"\n <a href=\""+link+"\">read more</a>\'"+" --icon=\""+icon+".png"+"\""
    system(s)

def genNotification(title, descr, icon, link):
    if (name=='nt'):
        genNotificationWindows(title, descr, icon, link)
    else:
        genNotificationLinux(title, descr, icon, link)
#constants.init()
#genNotification("Anime", "descr..", constants.ICON_NAME, "https://www.google.com")