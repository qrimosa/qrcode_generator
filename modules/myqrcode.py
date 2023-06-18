import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import qrcode
# import pyqrcode
# import png
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageTk
import modules.creating_screen as m_screen
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.moduledrawers.pil import SquareModuleDrawer
from qrcode.image.styles.moduledrawers.pil import GappedSquareModuleDrawer
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer
from qrcode.image.styles.moduledrawers.pil import VerticalBarsDrawer
from qrcode.image.styles.moduledrawers.pil import HorizontalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.colormasks import SquareGradiantColorMask
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask
from qrcode.image.styles.colormasks import VerticalGradiantColorMask
import qrcode.image.svg
import modules.registration as mreg
import os 


path_to_logo = None
svg_factory = None
count = 0
list_path = []

def svg_cmd():
    add_logo_bt.configure(state = "disabled")
    bgcolor.configure(state = "disabled")
    fgcolor.configure(state = "disabled")
    apply_colormask_bt.configure(state = "disabled")
    apply_drawer_bt.configure(state = "disabled")
    method = "basic"
    if method == "basic":
        global svg_factory
        svg_factory = qrcode.image.svg.SvgImage


def add_logo():
    file_object = filedialog.askopenfile(title = "Choose a logo you want to be added on QRCode", filetypes=(('jpg', '*.jpg'), ('png', '*.png')))
    if file_object:
        global path_to_logo
        path_to_logo = file_object.name
    else:
        path_to_logo = None

def make_qr():
    global count
    global imgqr
    count += 1
    if len(qrdata.get()) != 0:
        if path_to_logo == None and svg_factory == None:
            qr = qrcode.QRCode(version = 1,
                                error_correction = qrcode.constants.ERROR_CORRECT_H,
                                box_size = 50, 
                                border = 1) 
            qr.add_data(qrdata.get())
            qr.make(fit= True)
            
            imgqr = qr.make_image(back_color = (bg_color[1]), fill_color = (fg_color[1]), image_factory= StyledPilImage, 
                              module_drawer = abc, color_mask = a)
            imgqr = imgqr.resize((315, 315))
            imagetk = ImageTk.PhotoImage(imgqr)
            qrcode_label = ctk.CTkLabel(qrcode_frame, image = imagetk, text = "")
            qrcode_label.place(x = 5, y = 5)
            imgqr.save(f"C:\\marat\\python\\qrcode\\users\\{mreg.entry_5.get()}\\qrcode{count}.png")
            
        elif path_to_logo != None:
            qr = qrcode.QRCode(version = 1,
                                error_correction = qrcode.constants.ERROR_CORRECT_H,
                                box_size = 50, 
                                border = 1) 
            qr.add_data(qrdata.get())
            qr.make(fit= True)
            imgqr = qr.make_image(back_color = (bg_color[1]), fill_color = (fg_color[1]), image_factory= StyledPilImage, 
                              module_drawer = abc, color_mask = a, embeded_image_path = path_to_logo)
            imgqr = imgqr.resize((315, 315))
            imagetk = ImageTk.PhotoImage(imgqr)
            qrcode_label = ctk.CTkLabel(qrcode_frame, image = imagetk, text = "")
            qrcode_label.place(x = 5, y = 5)
            imgqr.save(f"C:\\marat\\python\\qrcode\\users\\{mreg.entry_5.get()}\\qrcode{count}.png") 
        
        elif svg_factory != None:
            qr = qrcode.QRCode(version = 1,
                                error_correction = qrcode.constants.ERROR_CORRECT_H,
                                box_size = 50, 
                                border = 1) 
            qr.add_data(qrdata.get())
            qr.make(fit= True)            
            global svg_imgqr
            svg_imgqr = qr.make_image(image_factory= svg_factory)
            imgqr = qr.make_image()
            imgqr = imgqr.resize((315, 315))
            imagetk = ImageTk.PhotoImage(imgqr)
            qrcode_label = ctk.CTkLabel(qrcode_frame, image = imagetk, text = "")
            qrcode_label.place(x = 5, y = 5)
            imgqr.save(f"C:\\marat\\python\\qrcode\\users\\{mreg.entry_5.get()}\\qrcode{count}.png") 
    
        qrdata.delete(0, 'end')
        listbox.delete(0, 'end')
        qr.clear()
    else:
       print("you didn't provide neither link nor text")


def bgcolor_cmd():
    global bg_color
    bg_color = colorchooser.askcolor(initialcolor= "white")
    return bg_color

def fgcolor_cmd():
    global fg_color
    fg_color = colorchooser.askcolor(initialcolor= "black")
    return fg_color

def save():
    input_path_object = filedialog.asksaveasfile(defaultextension=".png")
    if input_path_object:
        input_path = input_path_object.name
        if input_path.endswith(".svg"):
            svg_imgqr.save(input_path)
        imgqr.save(input_path)
    
        
def display_image(event): #big thanks to Uliana!!!!
    cur_index = listbox.curselection()
    if cur_index:
        image_path = listbox.get(cur_index)
        image = Image.open(image_path)
        # image = image.resize((320, 320))
        tk_image = ImageTk.PhotoImage(image)
        label_image = ctk.CTkLabel(qrcode_frame, image = tk_image, text = "")
        label_image.place(x = 5, y = 5)


def apply_drawer():
    global abc 
    if drawer_patterns.get() == drawer_list[0]:
        abc = CircleModuleDrawer()
    elif drawer_patterns.get() == drawer_list[1]:
        abc = HorizontalBarsDrawer()
    elif drawer_patterns.get() == drawer_list[2]:
        abc = SquareModuleDrawer()
    elif drawer_patterns.get() == drawer_list[3]:
        abc = GappedSquareModuleDrawer()
    elif drawer_patterns.get() == drawer_list[4]:
        abc = RoundedModuleDrawer()
    elif drawer_patterns.get() == drawer_list[5]:
        abc = VerticalBarsDrawer()
    return abc

def apply_colormask():
    global a 
    if colormask_patterns.get() == colormask_list[0]:
        a = SolidFillColorMask(front_color= fg_color[0], back_color= bg_color[0])
    elif colormask_patterns.get() == colormask_list[1]:
        a = SquareGradiantColorMask(center_color= fg_color[0], back_color= bg_color[0])
    elif colormask_patterns.get() == colormask_list[2]:
        a = RadialGradiantColorMask(center_color = fg_color[0], back_color= bg_color[0])
    elif colormask_patterns.get() == colormask_list[3]:
        a = HorizontalGradiantColorMask(left_color = fg_color[0], back_color= bg_color[0])
    elif colormask_patterns.get() == colormask_list[4]:
        a = VerticalGradiantColorMask(top_color= fg_color[0], back_color= bg_color[0])

def account_cmd():
    qrdata.place_forget()
    make_qr_bt.place_forget()
    add_logo_bt.place_forget()
    save_bt.place_forget()
    fgcolor.place_forget()
    bgcolor.place_forget()
    entry_label.place_forget()
    drawer_patterns.place_forget()
    apply_drawer_bt.place_forget()
    colormask_patterns.place_forget()
    apply_colormask_bt.place_forget()
    svg_bt.place_forget()
    account_bt.place_forget()
    mreg.entry_1.delete(0, 'end')
    mreg.entry_2.delete(0, 'end')
    mreg.entry_3.delete(0, 'end')
    mreg.entry_4.delete(0, 'end')
    mreg.entry_6.delete(0, 'end')
    mreg.user_bt.place_forget()
    mreg.logout_bt.place_forget()
    listbox.place(x = 200, y = 200)
    back_bt.place(x = 50, y = 600)

def back():
    qrdata.place(x = 100, y = 150)
    make_qr_bt.place(x = 665, y = 545)
    add_logo_bt.place(x = 100, y = 250)
    save_bt.place(x = 715, y = 595)
    fgcolor.place(x = 100, y = 350)
    bgcolor.place(x = 100, y = 450)
    entry_label.place(x = 100, y = 120)
    drawer_patterns.place(x = 100, y = 550)
    apply_drawer_bt.place(x = 100, y = 600)
    colormask_patterns.place(x = 250, y = 550)
    apply_colormask_bt.place(x = 300, y = 600)
    qrcode_frame.place(x = 500, y = 150)
    svg_bt.place(x = 615, y = 550)
    mreg.user_bt.place(x = 800, y = 40)
    mreg.user_bt.config(text = mreg.entry_5.get())
    back_bt.place_forget()
    listbox.place_forget()

drawer_list = ["Circle", "Horizontal Lines", "Square", "Gapped Square", "Rounded", "Vertical Lines"]
colormask_list = ["Solid", "Square Gradient", "Radial Gradient", "Horizontal Gradient", "Vertical Gradient"]

qrdata = tk.Entry(m_screen.app, font = "arial 12 bold", cursor = "xterm")

make_qr_bt = tk.Button(m_screen.app, text = 'Create QRCode', width = 15, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command = make_qr)

add_logo_bt = tk.Button(m_screen.app, text = 'Add Logo', width = 22, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command = add_logo)

save_bt = tk.Button(m_screen.app, text = 'Save', width = 10, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command = save)

image_label = tk.Label(m_screen.app, text = "", bg = "black")

drawer_patterns = ttk.Combobox(m_screen.app, values = drawer_list)
drawer_patterns.set("Pick a Key Pattern")
apply_drawer_bt = tk.Button(m_screen.app, text = 'Apply', width = 10, bg = "red", font = "arial 10 bold", foreground= "white", cursor= "hand2", command = apply_drawer)

colormask_patterns = ttk.Combobox(m_screen.app, values = colormask_list)
colormask_patterns.set("Pick a Gradient Pattern")
apply_colormask_bt = tk.Button(m_screen.app, text = 'Apply', width = 10, bg = "red", font = "arial 10 bold", foreground= "white", cursor= "hand2", command = apply_colormask)

bgcolor = tk.Button(m_screen.app, text = 'Choose BG Color', width = 22, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command = bgcolor_cmd)

fgcolor = tk.Button(m_screen.app, text = 'Choose Key Color', width = 22, bg = "red", font = "arial 12 bold", foreground= "white", cursor= "hand2", command = fgcolor_cmd)

entry_label = tk.Label(m_screen.app, text = "enter text or link", bg = "black", fg = "white", font = "arial 10 italic")

qrcode_frame = ctk.CTkFrame(m_screen.app, bg_color= "#1b1b1b", width = 325, height = 325)

svg_bt = tk.Button(m_screen.app, text = 'SVG', bg = "black", font = "arial 12 bold", bd = 0, foreground= "white", cursor= "hand2", command = svg_cmd)

listbox = tk.Listbox(m_screen.app, font = 'arial 10 bold ', width = 30, height = 10, background= "#1b1b1b", foreground= "white")

account_bt = tk.Button(m_screen.app, text = 'your account', background= "red", font = "arial 11 bold", foreground= "white", cursor= "hand2", command = account_cmd)

listbox.bind("<<ListboxSelect>>", display_image)

back_bt = tk.Button(m_screen.app, text = '<- back', background= "red", font = "arial 11 bold", foreground= "white", cursor= "hand2", command = back)