#LISTBOX COM BIND
import tkinter as tk
'''
=============
FUNCTIONS
=======
'''
def on_double_click(event):
    listbox = event.widget

    indices = listbox.curselection()

    if indices:
        valor = listbox.get(indices[0])
        label.config(text=f'Você deu duplo clique em: {valor}')   

'''
=============
INTERFACES
=============
'''
#Janela Principal
root = tk.Tk()
root.title("Exemplo de Listbox com bind()")
root.geometry('300x250')

# Criando Listbox com múltipla seleção
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, bg='lightgreen', 
                     font=('Arial', 16, 'bold'))

listbox.pack(pady=20)

items = ["Java", "Python", "C++", "Javascript", "Go", "Swift"]

for item in items:
    listbox.insert(tk.END, item)

listbox.bind("<Double-Button-1>", on_double_click)

label = tk.Label(root, text='Dê um duplo clique em um item')
label.pack(pady=10)

root.mainloop()