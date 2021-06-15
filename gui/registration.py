import tkinter, sys
from tkinter import *
from tkinter import filedialog, messagebox

def register():
    def choose_file():
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select logo",filetypes = [('JPG files', '*.jpg'),('PNG files', '*.png')])

    register_window = Tk()
    register_window.title("New Registration")

    name_var = StringVar()
    vision_var = StringVar()
    sql_ip = StringVar()
    sql_port = StringVar()

    def submit():
        saveas(name_var.get(),vision_var.get(),sql_ip.get(),sql_port.get())
        messagebox.showinfo("New Registration", "Registration Successful")
        sys.exit()
        
    m_font = ("Courier New Bold", 16)
    t_font = ("Copperplate Gothic Light",14)

    name_label  = Label(register_window, text = "Name of Organization:", font = m_font).grid(row = 0, column = 0)
    name_entry = Entry(register_window, width = 28, font = t_font, textvariable = name_var).grid(row = 0, column = 1)

    logo_label = Label(register_window, text = "Logo:", font = m_font).grid(row = 1, column = 0)
    logo_button = Button(register_window, text = "Choose File", command = choose_file, font = m_font).grid(row = 1, column = 1)

    vision_label = Label(register_window, text = "Vision:", font = m_font).grid(row = 2, column = 0)
    vision_entry = Entry(register_window, width = 28, font = t_font, textvariable = vision_var).grid(row = 2, column = 1)

    sql_ip_label = Label(register_window, text = "Enter SQL server IP:", font = m_font).grid(row = 3, column = 0)
    sql_ip_entry = Entry(register_window, width = 28, font = t_font, textvariable = sql_ip).grid(row = 3, column = 1)

    sql_port_label = Label(register_window, text = "Enter SQL server Port:", font = m_font).grid(row = 4, column = 0)
    sql_port_entry = Entry(register_window, width = 28, font = t_font, textvariable = sql_port).grid(row = 4, column = 1)

    submit_button = Button(register_window, text = "Submit", command = submit, font = m_font).grid(columnspan=2)

    register_window.resizable(False, False)
    register_window.minsize(600, 250)
    register_window.mainloop()

def saveas(name, vision, sqlip, sqlport):
    with open("register.txt", "w") as file:
        file.write(name + "\n" + vision + "\n" + sqlip + "\n" + sqlport)
    file.close()