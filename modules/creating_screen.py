import customtkinter as ctk 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.APP_WIDTH = 900
        self.APP_HEIGHT = 700
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        self.resizable(False, False)
        self.title("QRCode Creator")
        self.wm_iconbitmap("media\\5.ico")
        self.config(bg = "black")

app = App()