from tkinter.font import BOLD
from gui import loginscreen
from gui import loginscreen
from tkinter import*
from functools import partial
import sys
from attendancesystem import database
from tkinter import messagebox, ttk
from authentication import traindata

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
            global l1_nd, dept_name_l, dept_name_e, dept_name_b, dept_name_c

            var_dept_name = StringVar()

            def add():
                database.add_dept(var_dept_name.get(), detail[-1], user, pswd)
                messagebox.showinfo("Add Department", "Department Successfully Added!!")
                destroy()

            l1_nd = Label(admin_window, text = "Add New Department", font = ("Cambria", 20, UNDERLINE))
            l1_nd.grid(row = 4, column = 0, columnspan = 7)

            dept_name_l = Label(admin_window, text = "Enter Department Name:", font = ("Lucida Fax", 14))
            dept_name_l.grid(row = 5, column = 1, columnspan = 2, sticky = "e")
            dept_name_e = Entry(admin_window, textvariable = var_dept_name, width = 22, font = ("", 13))
            dept_name_e.grid(row = 5, column = 3, columnspan = 2, sticky = "w")
            dept_name_b = Button(admin_window, text = "Add", command = add, bg = "green", fg = "white", font = ("", 10))
            dept_name_b.grid(row = 6, column = 1, columnspan = 2)
            dept_name_c = Button(admin_window, text = "Cancel", command = partial(destroy), bg = "black", fg = "white", font = ("", 10))
            dept_name_c.grid(row = 6, column = 3, columnspan = 2)
        
        def new_employ():
            destroy()
            global l1_ne, new_employ_name_l, new_employ_name_e, new_employ_name_i, new_employ_name_ie, new_employ_dept_l, new_employ_dept_c, new_employ_name_phe, new_employ_name_phl, new_employ_name_el, new_employ_name_ee,new_employ_address,new_employ_address_e, next_b, next_c

            name = StringVar()
            id = IntVar()
            dept_name = StringVar()
            phone_no = IntVar()
            email = StringVar()
            address = StringVar()

            l1_ne = Label(text = "New Employ", font = ("Cambria", 20, UNDERLINE))
            l1_ne.grid(row = 4, column = 0, columnspan = 7)

            def next():
                if len(name.get()) == 0:
                    messagebox.showerror("Name Error","Name cannot be left empty!!")
                else:
                    global train_l, train_folder, train_camera
                    values = [name.get(), id.get(), dept_name.get(), phone_no.get(), email.get(), address.get()]
                    destroy()

                    def folder():
                        traindata.selectfolder(values[1])
                        database.add_employ(detail[-1], user, pswd, values)
                        messagebox.showinfo("Train Data", "Successfull")

                    def camera():
                        traindata.camera(values[1])
                        database.add_employ(detail[-1], user, pswd, values)
                        messagebox.showinfo("Train Data", "Successfull")
                    
                    l1_ne = Label(text = "New Employ", font = ("Cambria", 20, UNDERLINE))
                    l1_ne.grid(row = 4, column = 0, columnspan = 7)
                    train_folder = Button(admin_window, text = "Train from Folder", command = folder, font = ("Cascadia Mono ExtraLight", 14))
                    train_folder.grid(row = 6, column = 1, columnspan = 2)
                    train_camera = Button(admin_window, text = "Train from Camera", command = camera, font = ("Cascadia Mono ExtraLight", 14))
                    train_camera.grid(row = 6, column = 3, columnspan = 3)

            new_employ_name_l = Label(admin_window, text = "Enter Employ Name: ", font = ("Lucida Fax", 14))
            new_employ_name_l.grid(row = 5, column = 1, columnspan = 2, sticky = "e")
            new_employ_name_e = Entry(admin_window, textvariable = name, width = 22, font = ("", 13))
            new_employ_name_e.grid(row = 5, column = 3, columnspan = 2, sticky = "w")
            new_employ_name_i = Label(admin_window, text = "Enter Employ Unique ID: ", font = ("Lucida Fax", 14))
            new_employ_name_i.grid(row = 6, column = 1, columnspan = 2, sticky = "e")
            new_employ_name_ie = Entry(admin_window, textvariable = id, width = 22, font = ("", 13))
            new_employ_name_ie.grid(row = 6, column = 3, columnspan = 2, sticky = "w")
            new_employ_dept_l = Label(admin_window, text = "Select Department: ", font = ("Lucida Fax", 14))
            new_employ_dept_l.grid(row = 7, column = 1, columnspan = 2, sticky = "e")
            new_employ_dept_c = ttk.Combobox(admin_window, textvariable = dept_name, values = database.get_dept(detail[-1], user, pswd))
            new_employ_dept_c.grid(row = 7, column = 3, columnspan = 2, sticky = "w")
            new_employ_name_phl = Label(admin_window, text = "Enter Employ Phone: ", font = ("Lucida Fax", 14))
            new_employ_name_phl.grid(row = 8, column = 1, columnspan = 2, sticky = "e")
            new_employ_name_phe = Entry(admin_window, textvariable = phone_no, width = 22, font = ("", 13))
            new_employ_name_phe.grid(row = 8, column = 3, columnspan = 2, sticky = "w")
            new_employ_name_el = Label(admin_window, text = "Enter Employ Email: ", font = ("Lucida Fax", 14))
            new_employ_name_el.grid(row = 9, column = 1, columnspan = 2, sticky = "e")
            new_employ_name_ee = Entry(admin_window, textvariable = email, width = 22, font = ("", 13))
            new_employ_name_ee.grid(row = 9, column = 3, columnspan = 2, sticky = "w")
            new_employ_address = Label(admin_window, text = "Enter Employ Address: ", font = ("Lucida Fax", 14))
            new_employ_address.grid(row = 10, column = 1, columnspan = 2)
            new_employ_address_e = Entry(admin_window, textvariable = address, width = 22, font = ("", 13))
            new_employ_address_e.grid(row = 10, column = 3, columnspan = 2)
            next_b = Button(admin_window, text = "Next", command = next, fg = "white", bg = "green", font = ("",12))
            next_b.grid(row = 11, column = 1, columnspan = 2)
            next_c = Button(admin_window, text = "Cancel", command = partial(destroy), fg = "white", bg = "black", font = ("", 12))
            next_c.grid(row = 11, column = 3, columnspan = 2)

        def view_department():
            destroy()
            global l1_d
            l1_d = Label(text = "Departments", font = ("Cambria", 20, UNDERLINE))
            l1_d.grid(row = 4, column = 0, columnspan = 7)
            depts = database.get_dept(detail[-1], user, pswd)
            

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
                dept_name_b.grid_remove()
                dept_name_c.grid_remove()
            except:
                pass

            try:
                l1_ne.grid_remove()
                new_employ_name_l.grid_remove()
                new_employ_name_e.grid_remove()
                new_employ_name_i.grid_remove()
                new_employ_name_ie.grid_remove()
                new_employ_dept_l.grid_remove()
                new_employ_dept_c.grid_remove()
                new_employ_name_phl.grid_remove()
                new_employ_name_phe.grid_remove()
                new_employ_name_ee.grid_remove()
                new_employ_name_el.grid_remove()
                new_employ_address_e.grid_remove()
                new_employ_address.grid_remove()
                next_b.grid_remove()
                next_c.grid_remove()
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

            try:
                train_folder.grid_remove()
                train_camera.grid_remove()
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
        
        menubar = Menu(admin_window)
        menu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Menu', menu = menu)
        menu.add_command(label ='Edit Holidays', command = None)
        menu.add_command(label ='View Holidays', command = None)
        menu.add_command(label ='Exit', command = partial(sys.exit))

        admin_window.config(menu = menubar)
        admin_window.minsize(False,900)
        admin_window.iconphoto(False, icon)
        admin_window.resizable(False, False)
        admin_window.mainloop()
    else:
        pass