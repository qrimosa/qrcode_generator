import customtkinter as ctk
import tkinter as tk
import modules.creating_screen as m_screen
import sqlite3
from tkinter import messagebox
import modules.myqrcode as qrcd
from PIL import Image, ImageTk
import os

conn = sqlite3.connect("media\\database.db")
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
    main_label.place_forget()
    meme_frame.place_forget()
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
    main_label.place_forget()
    meme_frame.place_forget()
    entry_4.place(x = 350, y = 150)
    entry_5.place(x = 350, y = 200)
    entry_6.place(x = 350, y = 250)
    label_4.place(x = 260, y = 150)
    label_5.place(x = 260, y = 200)
    label_6.place(x = 260, y = 250)
    login_bt2.place(x = 338, y = 300)
    login_label.place(x = 385, y = 70)
    

def reg():
    if entry_1.get().endswith("@gmail.com"):
        email = entry_1.get()    
    login = entry_2.get()
    password = entry_3.get()
    try:
        cursor.execute(f"SELECT Email, Login, Password FROM Users WHERE Email = '{email}' AND Login = '{login}' AND Password = '{password}'")
    except:
        messagebox.showinfo(title = '!', message= "invalid email")
        entry_1.delete(0, 'end')
        entry_2.delete(0, 'end')
        entry_3.delete(0, 'end')
    
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO Users(Email, Login, Password) VALUES(?,?,?)', (email, login, password))
        conn.commit()
        login_bt_cmd()
        entry_1.delete(0, 'end')
        entry_2.delete(0, 'end')
        entry_3.delete(0, 'end')
    else:
        messagebox.showinfo(title = "!", message = "This account already exists!")
        entry_1.delete(0, 'end')
        entry_2.delete(0, 'end')
        entry_3.delete(0, 'end')
        login_bt_cmd()

def login():
    email = entry_4.get()
    login = entry_5.get()
    password = entry_6.get()
    cursor.execute(f"SELECT Email, Login, Password FROM Users WHERE Email = '{email}' AND Login = '{login}' AND Password ='{password}'")
    conn.commit()
    if not cursor.fetchone():
        messagebox.showinfo(title= "!", message= "This account doesn't exist!")
        entry_4.delete(0, 'end')
        entry_5.delete(0, 'end')
        entry_6.delete(0, 'end')
        reg_bt_cmd()
    else:
        messagebox.showinfo(title= "😁", message= f"Welcome {entry_5.get()}!")
        entry_1.place_forget()
        entry_2.place_forget()
        entry_3.place_forget()
        entry_4.place_forget()
        entry_5.place_forget()
        entry_6.place_forget()
        label_1.place_forget()
        label_2.place_forget()
        label_3.place_forget()
        label_4.place_forget()
        label_5.place_forget()
        label_6.place_forget()
        submit_bt.place_forget()
        reg_label.place_forget()
        login_label.place_forget()
        login_bt2.place_forget()
        main_label.place_forget()
        qrcd.qrdata.place(x = 100, y = 150)
        qrcd.make_qr_bt.place(x = 665, y = 545)
        qrcd.add_logo_bt.place(x = 100, y = 250)
        qrcd.save_bt.place(x = 715, y = 595)
        qrcd.fgcolor.place(x = 100, y = 350)
        qrcd.bgcolor.place(x = 100, y = 450)
        qrcd.entry_label.place(x = 100, y = 120)
        qrcd.drawer_patterns.place(x = 100, y = 550)
        qrcd.apply_drawer_bt.place(x = 100, y = 600)
        qrcd.colormask_patterns.place(x = 250, y = 550)
        qrcd.apply_colormask_bt.place(x = 300, y = 600)
        qrcd.qrcode_frame.place(x = 500, y = 150)
        qrcd.svg_bt.place(x = 615, y = 550)
        user_bt.place(x = 800, y = 40)
        user_bt.config(text=entry_5.get())
        directory = entry_5.get()
        parent_dir = "C:\\marat\\python\\qrcode\\users"
        path = os.path.join(parent_dir, directory)
        isExist = os.path.exists(path)
        if not isExist:
            os.mkdir(path)


def logout():
    qrcd.qrdata.place_forget()
    qrcd.make_qr_bt.place_forget()
    qrcd.add_logo_bt.place_forget()
    qrcd.save_bt.place_forget()
    qrcd.fgcolor.place_forget()
    qrcd.bgcolor.place_forget()
    qrcd.entry_label.place_forget()
    qrcd.qrcode_frame.place_forget()
    qrcd.drawer_patterns.place_forget()
    qrcd.apply_drawer_bt.place_forget()
    qrcd.colormask_patterns.place_forget()
    qrcd.apply_colormask_bt.place_forget()
    qrcd.account_bt.place_forget()
    qrcd.image_label.configure(image = None)
    qrcd.listbox.delete(0, 'end')
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    entry_4.delete(0, 'end')
    entry_5.delete(0, 'end')
    entry_6.delete(0, 'end')
    qrcd.svg_bt.place_forget()
    user_bt.place_forget()
    logout_bt.place_forget()
    

    reg_bt_cmd()

def user_bt_cmd():
    list_path = os.listdir(f"C:\\marat\\python\\qrcode\\users\\{entry_5.get()}")
    path = f"C:\\marat\\python\\qrcode\\users\\{entry_5.get()}" 
    logout_bt.place(x = 800, y = 110)
    qrcd.account_bt.place( x = 650, y = 110)
    for image in list_path:
        if image.endswith(".png") or image.endswith('.jpg'):
            image_path = os.path.join(path, image)
            qrcd.listbox.insert('end', image_path)

user_icon = Image.open('media\\12345.png')
user_icon = user_icon.resize((25, 25), Image.LANCZOS)
user_icon = ImageTk.PhotoImage(user_icon)

meme_image = Image.open('media\\banana.jpg')
meme_image = meme_image.resize((440, 320), Image.LANCZOS)
meme_image = ImageTk.PhotoImage(meme_image)

reg_bt = tk.Button(m_screen.app, background="red", width = 20, text = 'Registration', font = "arial 15 bold", foreground= "white", cursor= "hand2", command = reg_bt_cmd)
reg_bt.place(x = 900 / 2 - 250, y = 500)

login_bt = tk.Button(m_screen.app, text = 'Login', width = 20, background="red", font = "arial 15 bold", foreground= "white", cursor= "hand2", command = login_bt_cmd)
login_bt.place(x = 900 / 2 , y = 500)

main_label = tk.Label(m_screen.app, text = "QRCode Generator", font = "impact 40 bold", fg = "white", bg = "black")
main_label.place(x = 240, y = 50)

submit_bt = tk.Button(m_screen.app, text = 'Submit', width = 20, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command = reg)
login_bt2 = tk.Button(m_screen.app, text = 'Login', width = 20, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command = login)

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

user_bt = tk.Button(m_screen.app, image = user_icon, compound= "left", text = "", font= "arial 9 bold", fg = "white", bg = "black", bd = 0, command = user_bt_cmd)
 
logout_bt = tk.Button(m_screen.app, text = 'Log Out', background= "red", font = "arial 11 bold", foreground= "white", cursor= "hand2", command = logout)

meme_frame = ctk.CTkFrame(m_screen.app, bg_color= "#1b1b1b", width = 450, height = 325)
meme_frame.place(x = 450 - 225, y = 150)

meme_label =  ctk.CTkLabel(meme_frame, image = meme_image, text = "")
meme_label.pack()

