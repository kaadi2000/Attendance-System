import os, sys
from gui import registration, loginscreen

os.chdir(os.environ['USERPROFILE'])

if not os.path.exists("Attendance System"):
    os.mkdir("Attendance System")
if not os.path.exists("Attendance System/data"):
    os.mkdir("Attendance System/data")

os.chdir("Attendance System/data")

if not os.path.exists("register.txt"):
    registration.register()
    sys.exit()

loginscreen.login()
sys.exit()