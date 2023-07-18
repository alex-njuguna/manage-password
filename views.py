#! /usr/bin/python3
from cryptography.fernet import Fernet
from key import load_key


def view():
    key = load_key()
    fer = Fernet(key)

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())
