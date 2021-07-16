from tkinter.messagebox import RETRY
import mysql.connector

def check(host, username, pswd):
    db = mysql.connector.connect(host = host, user = username, password = pswd)
    mycursor = db.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS attendance_system")

    db.close()

    db = mysql.connector.connect(host = host, user = username, password = pswd, database = "attendance_system")
    mycursor = db.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS department(DEPARTMENT_NAME CHAR(20))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS employ_details(EMPLOY_ID INT, DEPARTMENT_NAME CHAR(20), NAME CHAR(30), PHONE INT, EMAIL CHAR(30), ADDRESS CHAR(50))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS attendance(EMPLOY_ID INT, DATE DATETIME, IN_TIME DATETIME, OUT_TIME DATETIME, REMARKS CHAR(10))")
    
    db.commit()
    db.close()

def add_dept(dept_name,host, username, pswd):
    db = mysql.connector.connect(host = host, user = username, password = pswd, database = "attendance_system")
    mycursor = db.cursor()

    mycursor.execute("INSERT INTO department (DEPARTMENT_NAME) VALUES (%s)", (dept_name,))

    db.commit()
    db.close()

def add_employ(host, username, pswd, *values):
    db = mysql.connector.connect(host = host, user = username, password = pswd, database = "attendance_system")
    mycursor = db.cursor()

    mycursor.execute()

    db.commit()
    db.close()


def view_dept(host, username, pswd):
    db = mysql.connector.connect(host = host, user = username, password = pswd, database = "attendance_system")
    mycursor = db.cursor()

    mycursor.execute()

    db.commit()
    db.close()

def view_attendnce(host, username, pswd):
    db = mysql.connector.connect(host = host, user = username, password = pswd, database = "attendance_system")
    mycursor = db.cursor()

    mycursor.execute()

    db.commit()
    db.close()


def search(host, username, pswd):
    db = mysql.connector.connect(host = host, user = username, password = pswd, database = "attendance_system")
    mycursor = db.cursor()

    mycursor.execute()

    db.commit()
    db.close()


def get_dept(host, username, pswd):
    db = mysql.connector.connect(host = host, user = username, password = pswd, database = "attendance_system")
    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM department")
    result = [i[0] for i in mycursor.fetchall()]

    db.commit()
    db.close()

    return result
