'''Classe representativa de uma tela de Login'''
import tkinter as tk
from tkinter import messagebox as mg

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tela de Login")
        self.master.geometry("300x200")
        self.master.option_add('*Font', "Helvetica 12")
        self.master.configure(bg="#444444")

        #Image
        self.image = tk.PhotoImage(file="login.png", format='png')
        self.image = self.image.subsample(2)

        #Label Image
        self.label_image = tk.Label(master, image=self.image, bg="#444444")
        self.label_image.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

        #Form Login
        self.label_user = tk.Label(master, text="Usuário:", fg="#FFFFFF", bg="#444444")
        self.label_user.grid(row=1, column=0, pady=5, padx=5)

        self.input_user = tk.Entry(master)
        self.input_user.grid(row=1, column=1, pady=5, padx=5)

        self.label_pass = tk.Label(master, text="Senha:", fg="#FFFFFF", bg="#444444")
        self.label_pass.grid(row=2, column=0, pady=5, padx=5)

        self.input_pass = tk.Entry(master, show='*')
        self.input_pass.grid(row=2, column=1, pady=5, padx=5)

        self.check_login = tk.IntVar()
        self.checkbutton_login = tk.Checkbutton(master, text="Manter-me Conectado", 
                                                variable=self.check_login, bg="#444444", fg='#FFFFFF')
        self.checkbutton_login.grid(row=3, column=0, columnspan=2, pady=5, padx=5, sticky='w')

        self.btn_login = tk.Button(master, text="Login", command=self.validation_login)
        self.btn_login.grid(row=4, column=0, columnspan=2, pady=10)

    
    def validation_login(self):
        user = self.input_user.get()
        password = self.input_pass.get()

        if user == 'admin' and password == 'admin':
            mg.showinfo('Login Bem-Sucedido', 'Bem-vindo, admin!')
        else:
            mg.showerror("Erro de Login", "Usuário ou senha incorretos.")

if __name__ == "__main__":
    root = tk.Tk()
    LoginApp(root)
    root.mainloop()
