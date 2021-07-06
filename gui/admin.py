from tkinter.font import BOLD
from gui import loginscreen
from gui import loginscreen
from tkinter import*
from functools import partial

def login():
    loginscreen.login_admin()

def admin(mode, user, pswd, detail):
    if mode:
        admin_window = Tk()
        admin_window.title("Admin")
        icon = PhotoImage(file = "logo.png")
        copyright_symbol = u"\u00A9"

        Label(admin_window, text = detail[0], font = ("Arial Round MT", 60, BOLD)).grid(row = 0, columnspan = 7)
        Label(admin_window, text = detail[1], font = ("Candara", 24)).grid(row = 1, columnspan = 7)
        Button(admin_window, text = "+New Department", bg = "green", font = ("Comic Sans MS", 12)).grid(row = 2, column = 0)
        Button(admin_window, text = "+New Employ", bg = "green", font = ("Comic Sans MS", 12)).grid(row = 2, column = 1)
        Button(admin_window, text = "View Departments", bg = "green", font = ("Comic Sans MS", 12)).grid(row = 2, column = 2)
        Button(admin_window, text = "View Attendance", bg = "green", font = ("Comic Sans MS", 12)).grid(row = 2, column = 3)
        Button(admin_window, text = "Search", bg = "green", font = ("Comic Sans MS", 12)).grid(row = 2, column = 4)
        Button(admin_window, text = "Log Out", bg = "black", font = ("Comic Sans MS", 12), fg = "white").grid(row = 2, column = 5)
        Button(admin_window, text = "Exit", bg = "red", font = ("Comic Sans MS", 12), fg = "white").grid(row = 2, column = 6)
        Label(admin_window, text= copyright_symbol+"Kumar Aditya").grid(sticky = "w")

        admin_window.iconphoto(False, icon)
        admin_window.resizable(False, False)
        admin_window.mainloop()
    else:
        pass