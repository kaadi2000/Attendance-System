from tkinter import *
from gui import interface

def login():
    loginscreen = Tk()
    loginscreen.title("Login")
    detail = open("register.txt").read().split("\n")
    
    Label(loginscreen, text = detail[0], font = ("Clarendon Lt BT Light",22)).grid(row = 0, column = 1)

    loginscreen.minsize(400,300)
    loginscreen.resizable(False, False)
    loginscreen.mainloop()