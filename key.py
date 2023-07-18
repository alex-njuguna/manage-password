#! /usr/bin/python3
from cryptography.fernet import Fernet


def write_key():
    """generate a key"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
    """load a key"""
    f = open("key.key", "rb")
    key = f.read()
    f.close()
    return key