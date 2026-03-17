import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox

# Janela principal
root = tk.Tk()
root.geometry("900x600")
root.title("Aplicativo de Anotações - Situação Problema")

# PanedWindow principal (divide a tela em dois painéis ajustáveis)
paned = tk.PanedWindow(root, orient="horizontal")
paned.pack(fill="both", expand=True)

# Painel esquerdo (menu de navegação)
left_frame = tk.Frame(paned, bg="lightblue", width=200)
paned.add(left_frame)

tk.Label(left_frame, text="Menu de Navegação", bg="lightblue", font=("Arial", 12, "bold")).pack(pady=10)

# Painel direito (conteúdo principal com Notebook)
right_frame = tk.Frame(paned, bg="white")
paned.add(right_frame)

notebook = ttk.Notebook(right_frame)
notebook.pack(fill="both", expand=True)

# Aba 1 - Anotações
tab1 = tk.Frame(notebook, bg="white")
text_area = tk.Text(tab1, wrap="word")
text_area.pack(fill="both", expand=True)
notebook.add(tab1, text="Anotações")

# Aba 2 - Tarefas
tab2 = tk.Frame(notebook, bg="white")
task_list = tk.Listbox(tab2)
task_list.pack(fill="both", expand=True)

notebook.add(tab2, text="Tarefas")

# Aba 3 - Configurações
tab3 = tk.Frame(notebook, bg="white")

def limpar_anotacoes():
    text_area.delete("1.0", tk.END)

def mudar_cor():
    tab1.config(bg="lightyellow")
    text_area.config(bg="lightyellow")

tk.Button(tab3, text="Limpar Anotações", command=limpar_anotacoes).pack(pady=10)
tk.Button(tab3, text="Mudar Cor de Fundo", command=mudar_cor).pack(pady=10)

notebook.add(tab3, text="Configurações")

# --- Funções do Menu ---
def nova_nota():
    # Limpa área de texto e muda para aba de Anotações
    text_area.delete("1.0", tk.END)
    notebook.select(tab1)
    messagebox.showinfo("Nova Nota", "Área de anotações limpa para nova nota.")

def adicionar_tarefa():
    # Solicita ao usuário uma nova tarefa
    tarefa = simpledialog.askstring("Adicionar Tarefa", "Digite a nova tarefa:")
    if tarefa:
        task_list.insert(tk.END, tarefa)
        notebook.select(tab2)

def abrir_configuracoes():
    # Vai para aba de Configurações
    notebook.select(tab3)

# Botões do painel esquerdo conectados às funções
tk.Button(left_frame, text="Nova Nota", command=nova_nota).pack(pady=5, fill="x")
tk.Button(left_frame, text="Adicionar Tarefa", command=adicionar_tarefa).pack(pady=5, fill="x")
tk.Button(left_frame, text="Configurações", command=abrir_configuracoes).pack(pady=5, fill="x")

# Loop principal
root.mainloop()