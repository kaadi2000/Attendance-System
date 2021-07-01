from gui import loginscreen
from gui import loginscreen
from tkinter import*

def login():
    loginscreen.login_admin()

def admin(mode):
    admin_window = Tk()
    admin_window.title("Admin")
    
    admin_window.mainloop()