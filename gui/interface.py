from tkinter import *
from tkinter.font import BOLD
import mysql.connector
from authentication import facerecognition, fingerprint

def interface(detail, username, pswd):
    db = mysql.connector.connect(host = detail[-1], user = username, password = pswd)
    mycursor = db.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS attendance_system")

    icon = PhotoImage(file = "logo.png")

    db.close()

    db = mysql.connector.connect(host = detail[-1], user = username, password = pswd, database = "attendance_system")
    mycursor = db.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS department(DEPARTMENT_NAME CHAR(20))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS employ_details(DEPARTMENT_NAME CHAR(20),EMPLOY_ID INT, NAME CHAR(30), PHONE INT, EMAIL CHAR(30), ADDRESS CHAR(50))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS attendance(DEPARTMENT_NAME CHAR(20), EMPLOY_ID INT, NAME CHAR(30),DATE DATETIME, IN_TIME DATETIME, OUT_TIME DATETIME, REMARKS CHAR(10))")
    

    window = Tk()
    window.title("Attendance System")
    
    db.commit()

    window.iconphoto(False, icon)
    window.resizable(False, False)
    window.mainloop()

def mode(detail, username, pswd):
    window = Tk()
    window.title("Select Mode")

    icon = PhotoImage(file = "icon.png")
    
    def admin():
        window.destroy()
        interface(detail, username, pswd)
        
    def attendance():
        pass

    Button(text = "ADMIN LOGIN", font = ("",50, BOLD), command = admin).grid()
    Button(text = "ATTENDANCE", font = ("",50, BOLD), command = attendance).grid()

    window.iconphoto(False, icon)
    window.resizable(False, False)
    window.mainloop()
