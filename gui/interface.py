from tkinter import *
from tkinter.font import BOLD
from gui import admin
from authentication import facerecognition

def mode():
    window = Tk()
    window.title("Select Mode")

    icon = PhotoImage(file = "logo.png")
    
    def admin_():
        window.destroy()
        admin.login()

    def attendance():
        window.destroy()
        facerecognition.login()

    Button(text = "ADMIN LOGIN", font = ("",50, BOLD), command = admin_).grid()
    Button(text = "ATTENDANCE", font = ("",50, BOLD), command = attendance).grid()

    window.iconphoto(False, icon)
    window.resizable(False, False)
    window.mainloop()
