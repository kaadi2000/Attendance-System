import mysql.connector

def check(detail, username, pswd):
    db = mysql.connector.connect(host = detail[-1], user = username, password = pswd)
    mycursor = db.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS attendance_system")

    db.close()

    db = mysql.connector.connect(host = detail[-1], user = username, password = pswd, database = "attendance_system")
    mycursor = db.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS department(DEPARTMENT_NAME CHAR(20))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS employ_details(DEPARTMENT_NAME CHAR(20),EMPLOY_ID INT, NAME CHAR(30), PHONE INT, EMAIL CHAR(30), ADDRESS CHAR(50))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS attendance(DEPARTMENT_NAME CHAR(20), EMPLOY_ID INT, NAME CHAR(30),DATE DATETIME, IN_TIME DATETIME, OUT_TIME DATETIME, REMARKS CHAR(10))")
    
    db.commit()
    db.close()