import tkinter as tk
import customtkinter as ctk
import qrcode
import pyqrcode
import png
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageTk
import modules.creating_screen as m_screen

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10, 
    border = 1 
)



qrdata = tk.Entry(m_screen.app, font = "arial 12 bold", cursor = "xterm")

def make_qr():
    if len(qrdata.get()) != 0:
        qr.add_data(qrdata.get())
        qr.make(fit= True)
        global imgqr
        imgqr = qr.make_image(back_color = (bg_color[1]), fill_color = (fg_color[1])).convert('RGB')
        # get_image = ImageTk.PhotoImage(Image.open("1.png"))
        # image_label.config(image= get_image)
        qrdata.delete(0, 'end')

def add_logo():
    file_object = filedialog.askopenfile(title = "Choose a logo you want to be added on QRCode", filetypes=(('jpg', '*.jpg'), ('png', '*.png')))
    if file_object:
        logo = Image.open(file_object.name)
        basewidth = 100
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.LANCZOS)
        pos = ((imgqr.size[0] - logo.size[0]) // 2, (imgqr.size[1] - logo.size[1]) // 2)
        imgqr.paste(logo, pos)

def bgcolor_cmd():
    global bg_color
    bg_color = colorchooser.askcolor(initialcolor= "white")
    return bg_color

def fgcolor_cmd():
    global fg_color
    fg_color = colorchooser.askcolor(initialcolor= "black")
    return fg_color

def save():
    # path = "C:\\marat\\screenshots\\1.png"
    # imgqr.save(path,"PNG")
    imgqr.save("1.png")
    # qr.clear()

make_qr_bt = tk.Button(m_screen.app, text = 'Create QRCode', width = 15, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command = make_qr)

add_logo_bt = tk.Button(m_screen.app, text = 'Add Logo', width = 10, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command = add_logo)

save_bt = tk.Button(m_screen.app, text = 'Save', width = 10, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command = save)

image_label = tk.Label(m_screen.app, text = "")

bgcolor = tk.Button(m_screen.app, text = 'Choose Background Color', width = 20, bg = "red", font = "arial 10 bold", foreground= "white", cursor= "hand2", command = bgcolor_cmd)

fgcolor = tk.Button(m_screen.app, text = 'Choose Key Color', width = 20, bg = "red", font = "arial 10 bold", foreground= "white", cursor= "hand2", command = fgcolor_cmd)
