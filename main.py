import os, sys
from gui import registration, interface

if not os.path.exists("register.txt"):
    registration.register()
    sys.exit()

interface.mode()
sys.exit()