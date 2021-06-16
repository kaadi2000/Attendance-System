import mysql.connector

def verify_login(username, password, detail):
    try:
        mysql.connector.connect(host=detail[-1],user=username,password=password)
    except:
        return False
    else:
        return True