import tkinter as tk
from tkinter import messagebox
import re, json

PATH_JSON = 'dados.json'

# ==============================
# Funções
# ==============================

def validar_usuario(email):
    data_json = None

    with open(PATH_JSON, 'r', encoding='utf-8') as f:
        data_json = json.load(f)

    for user in data_json:
        if user['email'] == email:
            return True
    return False

def validar_email(email):
    PADRAO = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.fullmatch(PADRAO, email):
        return True
    
    return False

def salvar_json(path, data):
    data_json = None

    # Ler o conteúdo do json
    with open(path, 'r', encoding='utf-8') as f:
        data_json = json.load(f) #desserializando

    # Adicionar o novo user(dict) na lista
    data_json.append(data)

    # Escrever os dados no json
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data_json, f, ensure_ascii=False, indent=4)

def salvar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if nome == "" or email == "" or telefone == "":
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return
    
    if not validar_email(email):
        messagebox.showerror('Error', 'E-mail Inválido!')
        
    
    if validar_usuario(email):
        messagebox.showerror('Error', 'Usuário já cadastrado!')
        return

    dict_user = {
        'nome': nome,
        'email': email,
        'telefone': telefone
    }

    try:
        salvar_json(PATH_JSON, dict_user)
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

        limpar()
    except Exception as e:
        print(e)
        messagebox.showerror('Error', 'Erro ao cadastrar o usuário!')

def limpar():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)


# ==============================
# Janela principal
# ==============================

root = tk.Tk()
root.title("Mini Sistema de Cadastro")
root.geometry("700x400")

# ==============================
# Frame Lateral (Menu)
# ==============================

frame_lateral = tk.Frame(root, bg="#2c3e50", width=150)
frame_lateral.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(frame_lateral, text="MENU", bg="#2c3e50", fg="white",
         font=("Arial", 14, "bold")).pack(pady=20)

tk.Button(frame_lateral, text="Cadastro").pack(fill=tk.X, padx=10, pady=5)
tk.Button(frame_lateral, text="Relatórios").pack(fill=tk.X, padx=10, pady=5)
tk.Button(frame_lateral, text="Configurações").pack(fill=tk.X, padx=10, pady=5)

# ==============================
# Frame Principal
# ==============================

frame_principal = tk.Frame(root, bg="#ecf0f1")
frame_principal.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# ---- Frame Título ----
frame_titulo = tk.Frame(frame_principal, bg="#bdc3c7", height=60)
frame_titulo.pack(fill=tk.X)

tk.Label(frame_titulo, text="Cadastro de Usuário",
         bg="#bdc3c7", font=("Arial", 16, "bold")).pack(pady=15)

# ---- Frame Formulário ----
frame_form = tk.Frame(frame_principal, bg="#ecf0f1")
frame_form.pack(pady=30)

# Usando GRID dentro do frame_form
tk.Label(frame_form, text="Nome:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", padx=10, pady=10)
entry_nome = tk.Entry(frame_form, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_form, text="Email:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", padx=10, pady=10)
entry_email = tk.Entry(frame_form, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame_form, text="Telefone:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", padx=10, pady=10)
entry_telefone = tk.Entry(frame_form, width=30)
entry_telefone.grid(row=2, column=1, padx=10, pady=10)

# Botões
btn_salvar = tk.Button(frame_form, text="Salvar", width=12, command=salvar)
btn_salvar.grid(row=3, column=0, pady=20)

btn_limpar = tk.Button(frame_form, text="Limpar", width=12, command=limpar)
btn_limpar.grid(row=3, column=1, pady=20)

root.mainloop()
