import customtkinter as ctk
from tkinter import messagebox as msg


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x300")
        self.title("Janela CTK - 17/03")
        self.label = ctk.CTkLabel(self, 
                                  text='Página Inicial', 
                                  fg_color="transparent",
                                  text_color=('black','white'),
                                  font=('Berlin Sans FB', 16))
        self.label.pack(padx=10, pady=10)

        self.button = ctk.CTkButton(self, text='Clique-me!', fg_color='crimson', hover_color='dark red')
        self.button.pack(padx=10, pady=10)

        #Demais componentes serão adicionados no construtor
    
    #Métodos serão adicionados para criar comportamentos ligados a janela

app = MainWindow()
app.mainloop()
