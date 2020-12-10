from os import name, system, getcwd, popen
import constants
from pickle import dump, load

def init():
    try:
        with open(constants.SUBSCRIBED, 'rb') as subscribed:
            pass
    except FileNotFoundError:
        with open(constants.SUBSCRIBED, 'wb') as subscribed:
            dump(0, subscribed)

def setSubscribed(i):
    with open(constants.SUBSCRIBED, 'wb') as subscribed:
        dump(i, subscribed)

def checkSubscribed():
    with open(constants.SUBSCRIBED, 'rb') as subscribed:
        return(load(subscribed))

def schedule():
    # param, name of script to schedule
    # check if winows or linux and call
    # corresponding func
    setSubscribed(1)
    if (name=='nt'):
        scheduleWindows()
    else:
        scheduleLinux(constants.SCHEDULE_SCRIPT)

def scheduleLinux(schedule_script):
    # takes name of script to schedule on linux
    # schedule a ps in linux using crontab
    # schedule script on every boot
    from subprocess import check_output
    try:
        usrname=check_output('whoami').decode('utf-8')[:-1]
        # cmd='@reboot '+ usrname + " cd " + pwd + ' && export DISPLAY=:0.0 && '
        cmd='@reboot '+ usrname + " sleep 600 && cd " + constants.PATH + ' && export DISPLAY=:0.0 && '
        python3_path=check_output(['which', 'python3']).decode('utf-8')[:-1] 
        cmd=cmd+(python3_path+" "+constants.SCHEDULE_SCRIPT+" >> " + constants.LOG + " 2>&1 ") 
        with open(constants.BASH_SCRIPT, 'w') as script:
            script.write("sudo echo \""+cmd+"\n\" >> /etc/crontab")
        system("sudo bash " + constants.BASH_SCRIPT)
    except Exception as err:
        print("Error: " + err)
        exit(1)

def rmSchedule():
    if (name=='nt'):
        rmScheduleWindows()
    else:
        rmScheduleLinux()

def rmScheduleLinux():
    # remove from task scheduler linux
    # remove from task scheduler linux
    from subprocess import check_output
    usrname=check_output('whoami').decode('utf-8')[:-1]
    # cmd='@reboot '+usrname+' export DISPLAY=:0.0 && '
    cmd='@reboot '+ usrname + " sleep 600 && cd " + constants.PATH + ' && export DISPLAY=:0.0 && '
    python3_path=check_output(['which', 'python3']).decode('utf-8')[:-1] 
    cmd=cmd+(python3_path+" "+constants.SCHEDULE_SCRIPT+" >> " + constants.LOG + " 2>&1 ") 
    with open(constants.BASH_SCRIPT, 'w') as script:
        script.write("sudo gr_scriptep -v \""+ cmd +"\" /etc/crontab > " + constants.TMP + " && sudo mv " + constants.TMP + " /etc/crontab")
    system("sudo bash " + constants.BASH_SCRIPT)
    system("sudo rm " + constants.SUBSCRIBED)
    system("sudo rm " + constants.BASH_SCRIPT)
    system("sudo rm " + constants.TMP)
    system("sudo rm " + constants.LOG)
    exit(0)

def rmScheduleWindows():
    # rm from task scheduler windows
    command = "schtasks -delete -tn AnimeNotify -f"
    try:
        system("del " + constants.SUBSCRIBED)
        system("del " + constants.BASH_SCRIPT)
        system("del " + constants.TMP)
    except Exception as e:
        print(e)
        input("Press any key to continue......")
    popen(command)

def scheduleWindows():
    cwd = getcwd()
    command = 'schtasks -create -tn "AnimeNotify" -tr "%s\schedulescript.pyw" -sc onlogon -v1' % cwd 
    system(command)