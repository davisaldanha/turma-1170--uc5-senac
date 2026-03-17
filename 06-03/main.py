'''Exemplo de uso de Treeview'''
import tkinter as tk
from tkinter import ttk

ICON_CITY = './assets/city.png'
ICON_MALE = './assets/male.png'
ICON_FEMALE = './assets/female.png'

root = tk.Tk()
root.title('Exemplo Treeview 🌳')
root.geometry('500x400')
root.state('zoomed') #abrir janela maximizada

frame = ttk.Frame(root)

treeview = ttk.Treeview(frame, columns=('Salary', 'Bonus'))

#adicionando texto do cabeçalho
treeview.heading('#0', text='Employee')
treeview.heading('Salary', text='Salary')
treeview.heading('Bonus', text='Bonus')

#carregar icones
icon_city = tk.PhotoImage(file=ICON_CITY)
icon_male = tk.PhotoImage(file=ICON_MALE)
icon_female = tk.PhotoImage(file=ICON_FEMALE)

#adicionando itens ao Treeview
level1 = treeview.insert('', tk.END, text='San Jose', image=icon_city)

chk = ttk.Checkbutton(text='Checkbutton')

treeview.insert(level1, tk.END, text='John Doe', values=(f'${100000: ,}', f'${8000: ,}'), image=icon_male)
treeview.insert(level1, tk.END, text='Jane Doe', values=(f'${120000: ,}', f'${9000: ,}'), image=icon_female)

#adicionar um scrollbar (barra de rolagem)
v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=treeview.yview)
treeview.configure(yscrollcommand=v_scrollbar.set)

treeview.pack(side=tk.LEFT, fill='both', expand=True)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

frame.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()



