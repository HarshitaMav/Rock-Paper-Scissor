import tkinter as tk
import datetime
import pymysql
import os

connection = pymysql.connect(host="localhost", database="pytest", user="root", password="root")
cursor = connection.cursor()
# Sidenote: your database does not have a PRIMARY KEY
# I made u_id the PRIMARY KEY
cursor.execute(
    'CREATE TABLE IF NOT EXISTS account( username TEXT, password TEXT, classy TEXT,subject TEXT, forename TEXT, surname TEXT)')

root = tk.Tk()
l1 = tk.Label(text="Username")
l2 = tk.Label(text="password")
l3 = tk.Label(text="Class")
l4 = tk.Label(text="Subject")
l5 = tk.Label(text="Designation")
l6 = tk.Label(text="Surname")
username_entry = tk.Entry(root)
password_entry = tk.Entry(root)
classy_entry = tk.Entry(root)
subject_entry = tk.Entry(root)
forename_entry = tk.Entry(root)
surname_entry = tk.Entry(root)


def play():
    os.system("python tkrps.py")


def insert_user():
    username = username_entry.get()
    password = password_entry.get()
    classy = classy_entry.get()
    subject = subject_entry.get()
    forename = forename_entry.get()
    surname = surname_entry.get()
    insert_command = "INSERT INTO account(username,password, classy, subject, forename, surname) VALUES('{0}','{1}','{2}','{3}','{4}','{5}');".format(
        username, password, classy, subject, forename, surname)
    cursor.execute(insert_command)
    connection.commit()



insert_button = tk.Button(root, text="Insert my account", command=insert_user)
play = tk.Button(root, text="Play the game", command=play)


l1.pack()
username_entry.pack()
l2.pack()
password_entry.pack()
l3.pack()
classy_entry.pack()
l4.pack()
subject_entry.pack()
l5.pack()
forename_entry.pack()
l6.pack()
surname_entry.pack()
insert_button.pack()
play.pack()

root.mainloop()
