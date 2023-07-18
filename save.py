#! /usr/bin/python3
from cryptography.fernet import Fernet
from key import load_key


def save():
    """collect account name and password and push them to a txt file"""
    name = input('Account Name: ')
    pwd = input("Password: ")
    key = load_key()
    fer = Fernet(key)
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
