'''import subprocess

# command to run
#cmd = 'dism /online /add-capability /capabilityname:Rsat.ServerManager.Tools~~~~0.0.1.0'
cmd = 'notepad.exe'
# run the command as an administrator
subprocess.run('start cmd /c "echo off & {}"'.format(cmd), shell=True)


import subprocess
from subprocess import PIPE, STARTUPINFO, STARTF_USESHOWWINDOW

startupinfo = STARTUPINFO()
startupinfo.dwFlags |= STARTF_USESHOWWINDOW
startupinfo.wShowWindow = 0

cmd = 'calc.exe'

subprocess.Popen(cmd, startupinfo=startupinfo, stdin=PIPE,
                 stdout=PIPE, stderr=PIPE, shell=True)

import ctypes
messageBox = ctypes.windll.user32.MessageBoxW
for i in range(10):
    messageBox(None, "Your message here",
               "Message Box Title", 0x40 | 0x1)

import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

for i in range(10):
    message_box = QMessageBox()
    message_box.setText("This is an infinite message box")
    message_box.setModal(True)
    message_box.show()
'''

import time

print(time.time())
