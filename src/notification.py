from os import system, name
import subprocess
import constants
from win10toast import ToastNotifier
import webbrowser
# show notification

def openBrowser(url):
    webbrowser.open(url)

def genNotificationWindows(title, descr, icon, link):
    # cmd = """$hdrText = New-BTText -Content '{title}'
    # $subText = New-BTText -Content '{descr}'
    # $icon = New-BTImage -Source '{icon}' -AppLogoOverride
    # $aBinding = New-BTBinding -Children $hdrText, $subText -AppLogoOverride $icon
    # $aVisual = New-BTVisual -BindingGeneric $aBinding
    # $aContent = New-BTContent -Visual $aVisual -Launch {link} -ActivationType Protocol
    # Submit-BTNotification -Content $aContent""".format(title = title,descr =descr,icon = icon,link = link)

    # subprocess.call('powershell.exe -windowstyle hidden -nologo -noninteractive '+cmd)
    toast = ToastNotifier()
    toast.show_toast( title=title, msg=descr,
                    icon_path=icon, duration=5, threaded=False, callback_on_click=lambda : openBrowser(link))

def genNotificationLinux(title, descr, icon, link):
    s="notify-send \'"+title+"\' \'"+descr+"...\n <a href=\""+link+"\">read more</a>\'"+" --icon=\""+icon+".png"+"\""
    
    system(s)

def genNotification(title, descr, icon, link):
    if (name=='nt'):
        genNotificationWindows(title, descr, icon, link)
    else:
        genNotificationLinux(title, descr, icon, link)

# TEST
# constants.init()
# genNotification("AnimeNewstitle", "descr...", constants.ICON_NAME, "https://www.google.com")