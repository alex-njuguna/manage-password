#! /usr/bin/python3
from save import save
from views import view


def main():
    # master_password = input("Enter master password: ")

    while True:
        mode = input("save new password(s)\nview passwords(v)\nquit(q)\n >>>> h")
        if mode == "s":
            save()
        elif mode == "v":
            view()
        elif mode == "q":
            exit()
        else:
            print("invalid option")
            continue

