import os, sys
from gui import registration, loginscreen

if not os.path.exists("register.txt"):
    registration.register()
    sys.exit()

loginscreen.login()
sys.exit()