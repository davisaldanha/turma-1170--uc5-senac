'''Tela de Cadastro Simples'''

from CTkMessagebox import CTkMessagebox as mg
import customtkinter as ctk

class TelaCadastro(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        #Título
        self.label_titulo = ctk.CTkLabel(self, 
                                         text="Criar Conta", 
                                         font=('High Tower Text', 40, 'bold'))
        self.label_titulo.pack(pady=10)

        #Campos de Inserção
        self.entry_nome = ctk.CTkEntry(self, 
                                       placeholder_text="Nome", 
                                       height=40, 
                                       font=('High Tower Text', 20))
        self.entry_nome.pack(pady=6, padx=10, fill='x')

        self.entry_email = ctk.CTkEntry(self, 
                                       placeholder_text="Email", 
                                       height=40, 
                                       font=('High Tower Text', 20))
        self.entry_email.pack(pady=6, padx=10, fill='x')

        self.entry_senha = ctk.CTkEntry(self, 
                                       placeholder_text="Senha", 
                                       height=40, 
                                       font=('High Tower Text', 20),
                                       show='*')
        self.entry_senha.pack(pady=6, padx=10, fill='x')

        self.entry_conf_senha = ctk.CTkEntry(self, 
                                       placeholder_text="Confirmar Senha", 
                                       height=40, 
                                       font=('High Tower Text', 20),
                                       show="*")
        self.entry_conf_senha.pack(pady=6, padx=10, fill='x')

        #Botões
        self.btn_enviar = ctk.CTkButton(self, text="Enviar", height=40, font=('High Tower Text', 20),
                                        command=self.cadastrar)
        self.btn_enviar.pack(pady=6, padx=10, fill='x')

        self.btn_visualizar_senhas = ctk.CTkButton(self, 
                                                   text="Mostrar Senhas", 
                                                   height=40, 
                                                   font=('High Tower Text', 20),
                                                   command=self.visualizar_senhas)
        self.btn_visualizar_senhas.pack(pady=6, padx=10, fill='x')


    #Métodos
    def cadastrar(self):
        senha = self.entry_senha.get()
        conf_senha = self.entry_conf_senha.get()

        if senha == conf_senha and senha != "":
            mg(title='Cadastro Confirmado', 
               message=f"Usuário {self.entry_nome.get()} foi cadastrado com sucesso!",
               icon='check', option_1='Confirmar',
               font=('High Tower Text', 20))
        else:
            mg(title='Erro ao Cadastrar!',
               message='As senhas não conferem!',
               icon='cancel',
               font=('High Tower Text', 20))
    
    def visualizar_senhas(self):
        if self.entry_senha.cget('show') == '*':
            self.entry_senha.configure(show="")
            self.entry_conf_senha.configure(show="")
            self.btn_visualizar_senhas.configure(text="Ocultar Senhas")
        else:
            self.entry_senha.configure(show="*")
            self.entry_conf_senha.configure(show="*")
            self.btn_visualizar_senhas.configure(text="Mostrar Senhas")

if __name__ == '__main__':
    app = TelaCadastro()
    app.mainloop()

    '13:00'.split(':') # ['13', '00']
    

