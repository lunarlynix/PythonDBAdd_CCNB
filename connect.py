from tkinter import *

window = Tk()   

window.geometry("300x260")
window.resizable(False, False)
window.configure(background='#111827')

window.title("Database Credentials")

program_lbl = Label(window, text = "Database Credentials", font='Helvetica 14 bold', background='#111827', foreground='#60a5fa')
program_lbl.place(x = 20, y = 20)
author_lbl = Label(window, text = "Enter the credentials to connect to your db", background='#111827', foreground='#f9fafb')
author_lbl.place(x = 20, y = 50)


# IP Address
ip_lbl = Label(window, text = "IP Address", background='#111827', foreground='#f9fafb')
ip_lbl.place(x = 20, y = 83)

ip = Entry(window, width= 20, background='#374151', foreground='#f9fafb', border=0)
ip.insert(0, "localhost")
ip.place(x = 120, y = 85)

# Username
port_lbl = Label(window, text = "Username", background='#111827', foreground='#f9fafb')
port_lbl.place(x = 20, y = 113)

port = Entry(window, width= 20, background='#374151', foreground='#f9fafb', border=0, )
port.place(x = 120, y = 115)

# Password
password_lbl = Label(window, text = "Password", background='#111827', foreground='#f9fafb')
password_lbl.place(x = 20, y = 143)

password = Entry(window, width= 20, background='#374151', foreground='#f9fafb', border=0, show="*")
password.place(x = 120, y = 145)

# DB
ip_lbl = Label(window, text = "DB Name", background='#111827', foreground='#f9fafb')
ip_lbl.place(x = 20, y = 173)

ip = Entry(window, width= 20, background='#374151', foreground='#f9fafb', border=0)
ip.insert(0, "sakila")
ip.place(x = 120, y = 175)

# STODB Button
submit_btn = Button(window, text='Connect', width=20,bg='#2563eb',fg='#ffffff').place(x=20,y=215)

window.mainloop()