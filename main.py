import os, sys,gc
from gui import registration, interface

if not os.path.exists("register.txt"):
    registration.register()
    sys.exit()
    
gc.enable()
interface.mode()
sys.exit()