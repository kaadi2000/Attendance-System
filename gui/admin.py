from tkinter.font import BOLD
from gui import loginscreen
from gui import loginscreen
from tkinter import*
from functools import partial
import sys

def login():
    loginscreen.login_admin()

def admin(mode, user, pswd, detail):
    if mode:
        admin_window = Tk()
        admin_window.title("Admin")
        icon = PhotoImage(file = "logo.png")
        copyright_symbol = u"\u00A9"

        def logout():
            admin_window.destroy()
            import main

        def new_appartment():
            destroy()
            global l1_nd, dept_name_l, dept_name_e
            var_dept_name = StringVar()
            l1_nd = Label(admin_window, text = "Add New Department", font = ("Cambria", 20, UNDERLINE))
            l1_nd.grid(row = 4, column = 0, columnspan = 7)
            dept_name_l = Label(admin_window, text = "Enter Department Name:", font = ("Lucida Fax", 13))
            dept_name_l.grid(row = 5, column = 1, columnspan = 2, sticky = "e")
            dept_name_e = Entry(admin_window, textvariable = var_dept_name, width = 30)
            dept_name_e.grid(row = 5, column = 3, columnspan = 2, sticky = "w")
        
        def new_employ():
            destroy()
            global l1_ne
            l1_ne = Label(text = "New Employ", font = ("Cambria", 20, UNDERLINE))
            l1_ne.grid(row = 4, column = 0, columnspan = 7)

        def view_department():
            destroy()
            global l1_d
            l1_d = Label(text = "Departments", font = ("Cambria", 20, UNDERLINE))
            l1_d.grid(row = 4, column = 0, columnspan = 7)
        
        def view_attendance():
            destroy()
            global l1_va
            l1_va = Label(text = "View Attendance", font = ("Cambria", 20, UNDERLINE))
            l1_va.grid(row = 4, column = 0, columnspan = 7)

        def search():
            destroy()
            global l1_s, dept_name_l, dept_name_e
            l1_s = Label(text = "Search", font = ("Cambria", 20, UNDERLINE))
            l1_s.grid(row = 4, column = 0, columnspan = 7)
            

        def destroy():
            try:
                l1_nd.grid_remove()
                dept_name_e.grid_remove()
                dept_name_l.grid_remove()
            except:
                pass

            try:
                l1_ne.grid_remove()
            except:
                pass

            try:
                l1_d.grid_remove()
            except:
                pass

            try:
                l1_va.grid_remove()
            except:
                pass

            try:
                l1_s.grid_remove()
            except:
                pass

        Label(admin_window, text = detail[0], font = ("Arial Round MT", 60, BOLD)).grid(row = 0, columnspan = 7)
        Label(admin_window, text = detail[1], font = ("Candara", 24)).grid(row = 1, columnspan = 7)
        Button(admin_window, text = "+New Department", bg = "green", font = ("Comic Sans MS", 12), command = new_appartment).grid(row = 3, column = 0)
        Button(admin_window, text = "+New Employ", bg = "green", font = ("Comic Sans MS", 12), command = new_employ).grid(row = 3, column = 1)
        Button(admin_window, text = "View Departments", bg = "green", font = ("Comic Sans MS", 12), command = view_department).grid(row = 3, column = 2)
        Button(admin_window, text = "View Attendance", bg = "green", font = ("Comic Sans MS", 12), command = view_attendance).grid(row = 3, column = 3)
        Button(admin_window, text = "Search", bg = "green", font = ("Comic Sans MS", 12), command = search).grid(row = 3, column = 4)
        Button(admin_window, text = "Log Out", bg = "black", font = ("Comic Sans MS", 12), fg = "white", command = logout).grid(row = 3, column = 5)
        Button(admin_window, text = "Exit", bg = "red", font = ("Comic Sans MS", 12), fg = "white", command = partial(sys.exit)).grid(row = 3, column = 6)

        Label(admin_window, text= copyright_symbol+"Kumar Aditya").grid(row = 2, column = 5, columnspan = 2)
        
        admin_window.minsize(False,900)
        admin_window.iconphoto(False, icon)
        admin_window.resizable(False, False)
        admin_window.mainloop()
    else:
        pass