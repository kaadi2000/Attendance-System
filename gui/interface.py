from tkinter import *
from tkinter.font import BOLD
import mysql.connector

def interface(detail, username, pswd):
    db = mysql.connector.connect(host = detail[-1], user = username, password = pswd)
    mycursor = db.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS attendance_system")

    db.close()

    db = mysql.connector.connect(host = detail[-1], user = username, password = pswd, database = "attendance_system")
    mycursor = db.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS department(DEPARTMENT_NAME CHAR(20))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS employ_details(DEPARTMENT_NAME CHAR(20),EMPLOY_ID INT, NAME CHAR(30), PHONE INT, EMAIL CHAR(30), ADDRESS CHAR(50))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS attendance(DEPARTMENT_NAME CHAR(20), EMPLOY_ID INT, NAME CHAR(30),DATE CHAR(20), IN_TIME CHAR(30), OUT_TIME CHAR(30), REMARKS CHAR(10))")
    

    window = Tk()
    window.title("Attendance System")
    
    db.commit()
    window.resizable(False, False)
    window.mainloop()

def mode(detail, username, pswd):
    window = Tk()
    window.title("Select Mode")

    def admin():
        window.destroy()
        interface(detail, username, pswd)
        
    def attendance():
        pass

    button_1 = Button(text = "ADMIN LOGIN", font = ("",50, BOLD), command = admin).grid()
    button_2 = Button(text = "ATTENDANCE", font = ("",50, BOLD), command = attendance).grid()

    button_list = [button_1, button_2]

    Grid.columnconfigure(window, 0 , weight = 1)
    row_number = 0
    for button in button_list:
        Grid.rowconfigure(window, row_number, weight = 1)
        row_number += 1

    window.mainloop()
