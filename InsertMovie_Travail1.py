from tkinter import *
from tkinter import messagebox
import mysql.connector
import datetime

# Created by Lynix (Anthony Roy)
# Travail 1 CCNB

# Sends the Data to The Database
def sendToDB(title, description, release, length, ratingVariable, languageVariable):
    today = datetime.date.today()
    year = today.year

    # Title: Cannot be NULL
    if title == "": 
        messagebox.showerror("Error", "Content Error!\nTitle cannot be empty.")
        return

    # Description: Cannot be NULL
    if description == "": 
        messagebox.showerror("Error", "Content Error!\Description cannot be empty.")
        return

    # Release: Cannot be NULL
    if release == "": 
        messagebox.showerror("Error", "Content Error!\nRelease cannot be empty.")
        return
    
    # Length: Cannot be NULL
    if length == "": 
        messagebox.showerror("Error", "Content Error!\nLength cannot be empty.")
        return
    
    # Rating: Cannot be NULL
    if ratingVariable == "   Select   ": 
        messagebox.showerror("Error", "Content Error!\nRating must be selected.")
        return

    # Language: Cannot be NULL
    if languageVariable == "   Select   ": 
        messagebox.showerror("Error", "Content Error!\nLanguage must be selected.")
        return

    try: 
        int(release)
    except:
        messagebox.showerror("Error", "Content Error!\nRelease is not a valid whole number.")

    try: 
        int(length)
    except:
        messagebox.showerror("Error", "Content Error!\nRelease is not a valid whole number.")

    # Release: Cannot be more than 25 years in the future
    if int(release) > (year + 25):
        messagebox.showerror("Error", "Content Error!\nYou cannot create film more than 25 years in the future.")
        return  


    print("SQL STATUS: Sending Data to DB...")

    insert_cmd = (
        "INSERT INTO film (title, description, release_year, length, rating, language_id)"
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )

    try:
        cursor = connection.cursor()
        cursor.execute(insert_cmd, (title, description, release, length, ratingVariable, LANGUAGE_IDS[LANGUAGE_OPTIONS.index(languageVariable)]))
        connection.commit()
        messagebox.showinfo("Info", "Added Movie " + title + " to Database.")
        print("SQL STATUS: Sent!")

    except Exception as err:
        connection.rollback()
        messagebox.showerror("Error", "An error occured while sending data to Database.\n" + str(err))
        print("SQL ERROR: An error occured while sending data to Database.")
def connectToDB(host, username, password, database):

    if host == "" or username == "" or password == "" or database == "": 
        messagebox.showerror("Error", "Connection Error!\nSome connection settings is not filled out.")
        return


    # Connect to MySQL DB
    global connection
    try:
        connection = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database
        )
        print("CONNECTION STATUS: Connected.")
        con_window.destroy()
    except:
        messagebox.showerror("Error", "Connection Refused!\nMake sure your credentials are valid.")
        print("CONNECTION ERROR: Something went wrong!")

def prepareConnect():
    global con_window
    con_window = Tk()

    con_window.geometry("300x260")
    con_window.resizable(False, False)
    con_window.configure(background='#111827')
    con_window.attributes('-topmost',True)

    con_window.title("Database Credentials")

    program_lbl = Label(con_window, text = "Database Credentials", font='Helvetica 14 bold', background='#111827', foreground='#60a5fa')
    program_lbl.place(x = 20, y = 20)
    author_lbl = Label(con_window, text = "Enter the credentials to connect to your db", background='#111827', foreground='#f9fafb')
    author_lbl.place(x = 20, y = 50)


    # IP Address
    ip_lbl = Label(con_window, text = "IP Address", background='#111827', foreground='#f9fafb')
    ip_lbl.place(x = 20, y = 83)

    ip = Entry(con_window, width= 20, background='#374151', foreground='#f9fafb', border=0)
    ip.insert(0, "localhost")
    ip.place(x = 120, y = 85)

    # Username
    username_lbl = Label(con_window, text = "Username", background='#111827', foreground='#f9fafb')
    username_lbl.place(x = 20, y = 113)

    username = Entry(con_window, width= 20, background='#374151', foreground='#f9fafb', border=0, )
    username.place(x = 120, y = 115)

    # Password
    password_lbl = Label(con_window, text = "Password", background='#111827', foreground='#f9fafb')
    password_lbl.place(x = 20, y = 143)

    password = Entry(con_window, width= 20, background='#374151', foreground='#f9fafb', border=0, show="*")
    password.place(x = 120, y = 145)

    # DB
    db_lbl = Label(con_window, text = "DB Name", background='#111827', foreground='#f9fafb')
    db_lbl.place(x = 20, y = 173)

    db = Entry(con_window, width= 20, background='#374151', foreground='#f9fafb', border=0)
    db.insert(0, "sakila")
    db.place(x = 120, y = 175)

    # STODB Button
    submit_btn = Button(con_window, text='Connect', command=lambda:connectToDB(ip.get(), username.get(), password.get(), db.get()), width=20,bg='#2563eb',fg='#ffffff').place(x=20,y=215)

    con_window.mainloop()

# Gets Data for Rating & Language Dropdown
def getOptions():
    print("SQL STATUS: Fetching Options from DB...")

    # Fetch Languages
    get_languages_query = "SELECT language_id, name FROM sakila.language;"
    languages_cursor = connection.cursor()
    languages_cursor.execute(get_languages_query)
    lang_records = languages_cursor.fetchall()

    get_rating_query = "SELECT distinct rating FROM film"
    rating_cursor = connection.cursor()
    rating_cursor.execute(get_rating_query)
    rating_records = rating_cursor.fetchall()

    global RATING_OPTIONS
    global LANGUAGE_OPTIONS
    global LANGUAGE_IDS
    LANGUAGE_OPTIONS = []
    LANGUAGE_IDS = []
    RATING_OPTIONS = []

    for lang_record in lang_records:
        LANGUAGE_IDS.append(lang_record[0])
        LANGUAGE_OPTIONS.append(lang_record[1])

    for rating_record in rating_records:
        RATING_OPTIONS.append(rating_record[0])

    print("SQL STATUS: Fetched.")


def MainWindow(): 
    global window 
    window = Tk()   

    window.geometry("500x470")
    window.resizable(False, False)
    window.configure(background='#111827')

    window.title("Add Film to Sakila Database")

    program_lbl = Label(window, text = "Add Film to Sakila Database", font='Helvetica 14 bold', background='#111827', foreground='#60a5fa')
    program_lbl.place(x = 40, y = 20)
    author_lbl = Label(window, text = "Created by Lynix (Anthony Roy) All Rights Reserved. CCNB Python Project", background='#111827', foreground='#f9fafb')
    author_lbl.place(x = 40, y = 50)

    # Title
    title_lbl = Label(window, text = "Title", background='#111827', foreground='#f9fafb')
    title_lbl.place(x = 40, y = 90)

    title = Entry(window, width= 51, background='#374151', foreground='#f9fafb', border=0)
    title.place(x = 140, y = 90)

    # Description

    description_lbl = Label(window, text = "Description", background='#111827', foreground='#f9fafb')
    description_lbl.place(x = 40, y = 130)

    description = Text(window, width=38, height=5, background='#374151', foreground='#f9fafb', border=0)
    description.place(x = 140, y = 130)

    # Release Year

    release_lbl = Label(window, text = "Release Year", background='#111827', foreground='#f9fafb')
    release_lbl.place(x = 40, y = 235)

    release = Entry(window, width= 12, background='#374151', foreground='#f9fafb', border=0)
    release.place(x = 140, y = 235)

    # Length

    length_lbl = Label(window, text = "Length", background='#111827', foreground='#f9fafb')
    length_lbl.place(x = 40, y = 265)

    length = Entry(window, width= 12, background='#374151', foreground='#f9fafb', border=0)
    length.place(x = 140, y = 265)

    # Load Rating & Language from DB
    getOptions()

    # Rating
    rating_lbl = Label(window, text = "Rating", background='#111827', foreground='#f9fafb')
    rating_lbl.place(x = 40, y = 300)

    ratingVariable = StringVar(window)
    ratingVariable.set("   Select   ") # This is the default value
    rating = OptionMenu(window, ratingVariable, *RATING_OPTIONS)
    rating.config(background='#374151', foreground='#f9fafb', border=0)
    rating["highlightthickness"]=0
    rating.pack()
    rating.place(x=139,y=305)

    # Language
    language_lbl = Label(window, text = "Language", background='#111827', foreground='#f9fafb')
    language_lbl.place(x = 40, y = 345)

    languageVariable = StringVar(window)
    languageVariable.set("   Select   ") # This is the default value
    language = OptionMenu(window, languageVariable, *LANGUAGE_OPTIONS)
    language.config(background='#374151', foreground='#f9fafb', border=0)
    language["highlightthickness"]=0
    language.pack()
    language.place(x=139,y=340)

    # Connection Status
    if 'connection' in globals():
        if connection.is_connected():
            connection_lbl = Label(window, text = "Connected", background='#111827', foreground='#22c55e')
            connection_lbl.place(x = 40, y = 375)
        else:
            connection_lbl = Label(window, text = "Disconnected", background='#111827', foreground='#dc2626')
            connection_lbl.place(x = 40, y = 375)
    else:
        connection_lbl = Label(window, text = "Critical Error Occured / Disconnected", background='#111827', foreground='#dc2626')
        connection_lbl.place(x = 40, y = 375)
    # STODB Button
    submit_btn = Button(window, text='Send to DB', command=lambda:sendToDB(
        title.get(),
        description.get("1.0",'end-1c'),
        release.get(),
        length.get(),
        ratingVariable.get(),
        languageVariable.get()
    ), width=20,bg='#2563eb',fg='#ffffff').place(x=40,y=410)

    window.mainloop()

prepareConnect()
MainWindow()