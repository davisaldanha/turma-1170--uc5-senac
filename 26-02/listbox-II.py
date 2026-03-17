#LISTBOX COM BIND
import tkinter as tk
'''
=============
FUNCTIONS
=============
'''
def on_select(event):
    # Recupera o widget que disparou o evento
    listbox = event.widget

    #Capturar os índices selecionados
    indices = listbox.curselection()

    #Capture os valores correspondentes
    valores = [listbox.get(i) for i in indices]

    # Atualiza o valor contido na label com os itens selecionados
    label.config(text=f'Selecionados: {', '.join(valores)}')


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

# Conectar o evento <<ListBoxSelect>> à função on_select
listbox.bind("<<ListboxSelect>>", on_select)

label = tk.Label(root, text='Selecione um item...')
label.pack(pady=10)

root.mainloop()