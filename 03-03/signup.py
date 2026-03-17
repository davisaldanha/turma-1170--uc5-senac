import tkinter as tk
from tkinter import messagebox as mg, ttk
from datetime import datetime as dt


'''
    from tkinter import ttk

    ttk - módulo criado com base no tkinter, porém trazendo
    mais possibilidades visuais.
'''

def salvar():
    nome = entry_nome.get()
    email = entry_email.get()
    genero = entry_genero.get()
    interesses = []

    if chk_python_var.get():
        interesses.append("Python")
    if chk_java_var.get():
        interesses.append("Java")
    if chk_javascript_var.get():
        interesses.append("Javascript")
    
    comentarios = txt_comentarios.get('1.0', tk.END).strip()
    cidade = listbox_cidades.get(tk.ACTIVE)

    resumo = f'''
Nome: {nome}
Email: {email}
Gênero: {genero}
Interesses: {', '.join(interesses)}
Cidade: {cidade}
Comentários: {comentarios}

Cadastrado em {dt.today().strftime("%d/%m/%y - %H:%M:%S")}
'''
    mg.showinfo("Cadastro Salvo", resumo)
    
#Janela Principal
root = tk.Tk()
root.title("Tela de Cadastro")

root.geometry('500x500')

#Estilo ttk
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background="#f5f5f5", font=("Arial", 11))
style.configure("TButton", background="#120a8f", foreground="white", font=("Arial", 12, "bold"), padding=6)
style.configure("TRadiobutton", background="#f5f5f5", font=("Arial", 11))
style.configure("TCheckbutton", background="#f5f5f5", font=("Arial", 11))

# modifica o estilo do botão ao clicar ou passar mouse por cima
style.map(
    "TButton",
    background=[("active", "white")],
    foreground=[("active", "black")]
)


#MenuBar
menubar = tk.Menu(root)
root.configure(menu=menubar)

menu_arquivo = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=root.quit)

#Frame principal
frame_form = ttk.Frame(root, padding=15)
frame_form.pack()

#Nome
ttk.Label(frame_form, text="Nome: ").grid(row=0, column=0, sticky='e')
entry_nome = ttk.Entry(frame_form, width=30)
entry_nome.grid(row=0, column=1)


#Email
ttk.Label(frame_form, text="Email: ").grid(row=1, column=0, sticky='e')
entry_email = ttk.Entry(frame_form, width=30)
entry_email.grid(row=1, column=1)

#Gênero (Radiobutton)
ttk.Label(frame_form, text="Gênero: ").grid(row=2, column=0, sticky='e')
entry_genero = tk.StringVar(value='N/A')
ttk.Radiobutton(frame_form, text="Masculino", 
               variable=entry_genero, 
               value="Masculino").grid(row=2, column=1, sticky="w")
ttk.Radiobutton(frame_form, text="Feminino", 
               variable=entry_genero, 
               value="Feminino").grid(row=2, column=2, sticky="w")

#Interesses (Checkbutton)
ttk.Label(frame_form, text="Interesses: ").grid(row=3, column=0, sticky='e')
chk_java_var = tk.BooleanVar()
chk_python_var = tk.BooleanVar()
chk_javascript_var = tk.BooleanVar()
ttk.Checkbutton(frame_form, text="Java", variable=chk_java_var).grid(row=3,
                                                                    column=1,
                                                                    sticky='w')
ttk.Checkbutton(frame_form, text="Python", variable=chk_python_var).grid(row=3,
                                                                    column=2,
                                                                    sticky='w')
ttk.Checkbutton(frame_form, text="JavaScript", variable=chk_javascript_var).grid(row=3,
                                                                    column=3,
                                                                    sticky='w')

#Listbox (Cidades)
ttk.Label(frame_form, text="Cidade: ").grid(row=4, column=0, sticky='e')
listbox_cidades = tk.Listbox(frame_form, height=5)
cidades = ['Fortaleza', "São Paulo", "Rio de Janiero", "Belo Horizonte", "Curitiba"]
for cidade in cidades:
    listbox_cidades.insert(tk.END, cidade)
listbox_cidades.grid(row=4, column=1, columnspan=2, sticky='w')

#Text (Comentários)
ttk.Label(frame_form, text="Comentários: ").grid(row=5, column=0, sticky='ne')
txt_comentarios = tk.Text(frame_form, width=40, height=5)
txt_comentarios.grid(row=5, column=1, columnspan=3)


#Botão (Salvar)
btn_salvar = ttk.Button(root, text="Salvar Cadastro", command=salvar)
btn_salvar.pack(pady=10)


root.mainloop()


