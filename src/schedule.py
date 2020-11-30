from os import name

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
    pass

def rmScheduleLinux():
    # remove from task scheduler linux
    pass

def rmScheduleWindows():
    pass

def scheduleWindows(x):
    pass
