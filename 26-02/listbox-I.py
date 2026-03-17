# APRESENTAÇÃO DO WIDGET LISTBOX
import tkinter as tk

#Janela Principal
root = tk.Tk()
root.title("Exemplo de Listbox")
root.geometry('300x250')

#Criando um listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
# selectmode pode ser:
#tk.SINGLE -> apenas um item
#tk.MULTIPLE -> múltiplos itens
#tk.BROWSE -> parecido com SIGLE, mas permite arrastar
#tk.EXTENDED -> múltiplos item com Shift ou CTRL

items = ["Java", "Python", "C++", "Javascript", "Go", "Swift"]

for item in items:
    listbox.insert(tk.END, item)

listbox.pack(pady=10)

#Função para mostrar o item selecionado
def mostrar_item():
    selecionado = listbox.get(tk.ACTIVE) #pegar o item ativo
    label.config(text=f'Você selecionou: {selecionado}')

#Botão para confirmar seleção
tk.Button(root, text='Mostrar Seleção', 
                bg='lightblue', command=mostrar_item).pack()

#Label para exibir resultado
label = tk.Label(root, text='Selecione um item da lista')
label.pack()

root.mainloop()