import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Seja Bem Vindo ao SmartSystem")
        self.geometry("420x500")

        ctk.set_appearance_mode('system') # system(default), light, dark
        ctk.set_default_color_theme('green') #blue(default), dark-blue, green

        self.current_frame = TelaLogin(self)
        self.current_frame.pack(pady=10, padx=10, fill='both', expand=True)