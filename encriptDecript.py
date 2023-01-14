from cryptography.fernet import Fernet


global key, fernet

key = Fernet.generate_key()
fernet = Fernet(key)


def encrypt(Msg):
    encMsg = fernet.encrypt(Msg.encode())
    return encMsg


def decrypt(Msg, key):
    Msg = bytes(Msg, 'utf-8')
    decMsg = Fernet(key).decrypt(Msg).decode()
    return decMsg


def menu():
    x = 0
    while x < 3 and x > -1:
        print("_____Menu_____")
        print("1. Encriptar")
        print("2. Desencriptar")
        print("3. Salir")
        x = int(input("Opción: "))
        if x == 1:
            mensaje = encrypt(
                input("Ingrese el mensaje que desea encriptar: "))
            print(mensaje)
            print(key)
        elif x == 2:
            mensaje = decrypt(
                input("Ingrese el mensaje que desea desencriptar: "), input("Ingrese la llave: "))
            print(mensaje)
