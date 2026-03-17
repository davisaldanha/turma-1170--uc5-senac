'''Exemplo de um pequeno sistema HelpDesk com uso do ComboBox e Enum'''
import tkinter as tk
from tkinter import ttk, messagebox as mg
from enum import Enum
from datetime import datetime as dt

class CategoriaChamado(Enum):
    HARDWARE = "Hardware"
    SOFTWARE = "Software"
    REDE = "Rede"
    SISTEMA = "Sistema"

class Prioridade(Enum):
    BAIXA = "Baixa"
    MEDIA = "Média"
    ALTA = "Alta"
    CRITICA = "Crítica"

class Tecnico(Enum):
    LUCIANO = "Luciano - Infraestrutura"
    JEAN = "Jean - Suporte"
    ALLANDER = "Allander - Sistemas"
    KARLA = "Karla - Redes"


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Chamados - HelpDesk SENAC")
        self.root.geometry('500x300')
        self.root.configure(bg='#1e1e1e')

        self.criar_estilo()

        container = ttk.Frame(root, padding=20)
        container.pack(fill='both', expand=True)

        titulo = ttk.Label(container, text='Abrir Chamado Técnico', style='Titulo.TLabel')
        titulo.pack(pady=(0, 20))

        #Categoria 
        ttk.Label(container, text="Categoria do Problema: ").pack(anchor="w")

        self.combo_categoria = ttk.Combobox(
            container,
            values = [c.value for c in CategoriaChamado],
            state='readonly'
        )
        self.combo_categoria.pack(fill='x', pady=5)
        self.combo_categoria.bind("<<ComboboxSelected>>", self.atualizar_descricao)

        #Prioridade
        ttk.Label(container, text="Prioridade: ").pack(anchor="w")

        self.combo_prioridade = ttk.Combobox(
            container,
            values = [p.value for p in Prioridade],
            state='readonly'
        )
        self.combo_prioridade.pack(fill='x', pady=5)

        #Técnico
        ttk.Label(container, text="Técnico: ").pack(anchor="w")

        self.combo_tecnico = ttk.Combobox(
            container,
            values = [t.value for t in Tecnico],
            state='readonly'
        )
        self.combo_tecnico.pack(fill='x', pady=5)

        #Descrição

        ttk.Label(container, text="Descrição: ").pack(anchor='w')

        self.descricao = tk.Text(
            container,
            height=4,
            bg='#252526',
            fg='white'
        )
        self.descricao.pack(fill="x", pady=5)

        #Botão
        ttk.Button(
            container,
            text="Registrar Chamado",
            command=self.registrar
            
        ).pack(pady=15)


    def criar_estilo(self):
        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            'TFrame',
            background="#1e1e1e"
        )

        style.configure(
            'TLabel',
            background='#1e1e1e',
            foreground="white",
            font=("Segoe UI", 12)
        )

        style.configure(
            'Titulo.TLabel',
            font=('Segoe UI', 16, 'bold'),
            padding=6
        )

        style.configure(
            'TButton',
            font=('Segoe UI', 12),
            padding=6
        )

        style.configure(
            'TCombobox',
            font=('Segoe UI', 10),
            padding=5
        )

    # Funções de Evento - Bind
    def atualizar_descricao(self, event):

        categoria = self.combo_categoria.get()

        mensagens = {
            "Hardware": "Problema relacionado a componentes físicos do computador",
            "Software": "Erro ou falha em programas instalados",
            "Rede": "Problema de conectividade ou acesso à rede.",
            "Sistema": "Erro no sistema operacional ou serviços."
        }

        self.descricao.delete('1.0', tk.END)

        if categoria in mensagens:
            self.descricao.insert(tk.END, mensagens[categoria])

    def registrar(self):
        categoria = self.combo_categoria.get()
        prioridade = self.combo_prioridade.get()
        tecnico = self.combo_tecnico.get()

        msg = f'''
Informações Chamado
Categoria: {categoria}
Prioridade: {prioridade}
Técnico: {tecnico}

Data e Hora : {dt.today().strftime('%d/%m/%Y - %H:%m')}
'''

        mg.showinfo('Chamado Registrado', msg)



root = tk.Tk()
App(root)
root.mainloop()
