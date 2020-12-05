from os import system, name
import constants
# show notification

def genNotificationWindows(title, descr, icon):
    pass

def genNotificationLinux(title, descr, icon):
    # notify-send 'Hello World!' 'This is a custom notification! <a href="https://www.google.com">https://www.google.com</a>'
    system("notify-send \""+title+"\" "+descr+" --icon=\""+icon+".png"+"\"")

def genNotification(title, descr, icon):
    if (name=='nt'):
        genNotificationWindows(title, descr, icon)
    else:
        genNotificationLinux(title, descr, icon)
constants.init()
genNotification("Anime", "descr..", constants.ICON_NAME)