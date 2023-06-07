import customtkinter as ctk
import tkinter as tk
import modules.creating_screen as m_screen
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Users (Email TEXT, Login TEXT, Password TEXT)')
conn.commit()

def reg_bt_cmd():
    login_bt.place_forget()
    reg_bt.place_forget()
    login_label.place_forget()
    entry_4.place_forget()
    entry_5.place_forget()
    entry_6.place_forget()
    label_4.place_forget()
    label_5.place_forget()
    label_6.place_forget()
    login_bt2.place_forget()
    entry_1.place(x = 350, y = 150)
    entry_2.place(x = 350, y = 200)
    entry_3.place(x = 350, y = 250)
    label_1.place(x = 260, y = 150)
    label_2.place(x = 260, y = 200)
    label_3.place(x = 260, y = 250)
    submit_bt.place(x = 338, y = 300)
    reg_label.place(x = 350, y = 70)

def login_bt_cmd():
    login_bt.place_forget()
    reg_bt.place_forget()
    reg_label.place_forget()
    entry_1.place_forget()
    entry_2.place_forget()
    entry_3.place_forget()
    label_1.place_forget()
    label_2.place_forget()
    label_3.place_forget()
    submit_bt.place_forget()
    entry_4.place(x = 350, y = 150)
    entry_5.place(x = 350, y = 200)
    entry_6.place(x = 350, y = 250)
    label_4.place(x = 260, y = 150)
    label_5.place(x = 260, y = 200)
    label_6.place(x = 260, y = 250)
    login_bt2.place(x = 338, y = 300)
    login_label.place(x = 350, y = 70)

def reg():
    email = entry_1.get()
    login = entry_2.get()
    password = entry_3.get()
    cursor.execute(f"SELECT Email, Login, Password FROM Users WHERE Email = '{email}' AND Login = '{login}' AND Password = '{password}'")

    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO Users (Email, Login, Password) VALUES(?,?,?)", (email, login, password))
        conn.commit()
        login_bt_cmd()
        entry_1.delete(0, "end")
        entry_2.delete(0, "end")
        entry_3.delete(0, "end")
    else:
        messagebox.showinfo(title = "😠", message= "This account already exists!11!!1!")
        entry_1.delete(0, "end")
        entry_2.delete(0, "end")
        entry_3.delete(0, "end")
                                                                                                                                                                                  
def login():
    email = entry_4.get()
    login = entry_5.get()
    password = entry_6.get()
    cursor.execute(f"SELECT Email, Login, Password FROM Users WHERE Email = '{email}' AND Login = '{login}' AND Password = '{password}'")
    conn.commit()

    if not cursor.fetchone():
        messagebox.showinfo(title="😠", message= "this account doesn't exist!!!11!1!")
        entry_4.delete(0, "end")
        entry_5.delete(0, "end")
        entry_6.delete(0, "end")
        reg_bt_cmd()
    else:
        messagebox.showinfo(title = "😁", message = "Welcum!")


reg_bt = tk.Button(m_screen.app, text = 'Registration', font = "arial 12 bold", foreground= "white", cursor= "hand2", command = reg_bt_cmd)
reg_bt.place(x = 350, y = 350)

login_bt = tk.Button(m_screen.app, text = 'Login', font = "arial 12 bold", foreground= "white", cursor= "hand2", command = login_bt_cmd)
login_bt.place(x = 500, y = 350)

submit_bt = tk.Button(m_screen.app, text = 'Submit', width = 20, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command = reg)
login_bt2 = tk.Button(m_screen.app, text = 'Login', width = 20, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command= login)

reg_label = tk.Label(m_screen.app, text = "Registration", font = "arial 23 bold", fg = "white", bg = "black")
login_label = tk.Label(m_screen.app, text = "Login", font = "arial 23 bold", fg = "white", bg = "black")

label_1 = tk.Label(m_screen.app, text = "Email", font = "arial 12 bold", fg = "white", bg = "black")
label_2 = tk.Label(m_screen.app, text = "Login", font = "arial 12 bold", fg = "white", bg = "black")
label_3 = tk.Label(m_screen.app, text = "Password", font = "arial 12 bold", fg = "white", bg = "black")

entry_1 = tk.Entry(m_screen.app, font = "arial 12 bold", cursor= "xterm")
entry_2 = tk.Entry(m_screen.app, font = "arial 12 bold", cursor= "xterm")
entry_3 = tk.Entry(m_screen.app, font = "arial 12 bold", cursor= "xterm")

label_4 = tk.Label(m_screen.app, text = "Email", font = "arial 12 bold", fg = "white", bg = "black")
label_5 = tk.Label(m_screen.app, text = "Login", font = "arial 12 bold", fg = "white", bg = "black")
label_6 = tk.Label(m_screen.app, text = "Password", font = "arial 12 bold", fg = "white", bg = "black")

entry_4 = tk.Entry(m_screen.app, font = "arial 12 bold", cursor= "xterm")
entry_5 = tk.Entry(m_screen.app, font = "arial 12 bold", cursor= "xterm")
entry_6 = tk.Entry(m_screen.app, font = "arial 12 bold", cursor= "xterm")

