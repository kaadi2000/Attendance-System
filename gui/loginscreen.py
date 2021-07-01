from authentication import facerecognition
import sys, os
from tkinter import *
from tkinter.font import BOLD
from gui import interface, admin
from authentication import verify
from tkinter import messagebox
from attendancesystem import database

def login_admin():
    loginscreen = Tk()
    loginscreen.title("Login-Admin")
    detail = open("register.txt").read().split("\n")

    icon = PhotoImage(file = "logo.png")
    
    def auth():
        if verify.verify_login(user.get(), pswd.get(), detail):
            loginscreen.destroy()
            database.check(detail, user.get(), pswd.get())
            facerecognition.facerecognition()
        else:
            Label(loginscreen, text = "Invalid Login!!", fg = "red").grid(column = 0, columnspan=2)

    def reset():
        if os.path.exists("register.txt"):
            os.remove("register.txt")
        messagebox.showinfo("Login", "Program reset!! Kindly re-register to use!!")
        sys.exit()
    
    user = StringVar()
    pswd = StringVar()

    copyright_symbol = u"\u00A9"

    menubar = Menu(loginscreen)
    option = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Options', menu = option)
    option.add_command(label ='Reset', command = reset)
    loginscreen.config(menu=menubar)

    Label(loginscreen, text = detail[0], font = ("Castellar",22, UNDERLINE, BOLD)).grid(row = 0, column = 0, sticky = "sw", columnspan = 2)
    Label(loginscreen, text = detail[1], font = ("Bradley Hand ITC",16 , UNDERLINE, BOLD)).grid(row = 1, column = 0, columnspan = 2, sticky = "sw")
    Label(loginscreen, text = "Username:", font =("", 15)).grid(row = 2, column = 0, sticky = "e")
    Entry(loginscreen, font =("", 15), textvariable=user).grid(row = 2, column = 1)
    Label(loginscreen, text = "Password:", font =("", 15)).grid(row = 3, column = 0, sticky = "e")
    Entry(loginscreen, font =("", 15), show = "*", textvariable = pswd).grid(row = 3, column = 1)
    Button(loginscreen, text = "Login", command = auth,font = ("Berlin Sans FB Demi Bold", 16), bg = "green", fg = "white").grid(row = 4, column = 0, columnspan=2)
    Label(loginscreen, text= copyright_symbol+"Kumar Aditya").grid(sticky = "w")

    loginscreen.iconphoto(False, icon)
    loginscreen.resizable(False, False)
    loginscreen.mainloop()

def login_attendance():
    loginscreen = Tk()
    loginscreen.title("Login-Attendance")
    detail = open("register.txt").read().split("\n")

    icon = PhotoImage(file = "logo.png")
    
    def auth():
        if verify.verify_login(user.get(), pswd.get(), detail):
            loginscreen.destroy()
            database.check(detail, user.get(), pswd.get())
            facerecognition
        else:
            Label(loginscreen, text = "Invalid Login!!", fg = "red").grid(column = 0, columnspan=2)

    
    user = StringVar()
    pswd = StringVar()

    copyright_symbol = u"\u00A9"

    Label(loginscreen, text = detail[0], font = ("Castellar",22, UNDERLINE, BOLD)).grid(row = 0, column = 0, sticky = "sw", columnspan = 2)
    Label(loginscreen, text = detail[1], font = ("Bradley Hand ITC",16 , UNDERLINE, BOLD)).grid(row = 1, column = 0, columnspan = 2, sticky = "sw")
    Label(loginscreen, text = "Username:", font =("", 15)).grid(row = 2, column = 0, sticky = "e")
    Entry(loginscreen, font =("", 15), textvariable=user).grid(row = 2, column = 1)
    Label(loginscreen, text = "Password:", font =("", 15)).grid(row = 3, column = 0, sticky = "e")
    Entry(loginscreen, font =("", 15), show = "*", textvariable = pswd).grid(row = 3, column = 1)
    Button(loginscreen, text = "Login", command = auth,font = ("Berlin Sans FB Demi Bold", 16), bg = "green", fg = "white").grid(row = 4, column = 0, columnspan=2)
    Label(loginscreen, text= copyright_symbol+"Kumar Aditya").grid(sticky = "w")

    loginscreen.iconphoto(False, icon)
    loginscreen.resizable(False, False)
    loginscreen.mainloop()