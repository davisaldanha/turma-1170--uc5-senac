import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

paned = tk.PanedWindow(root, orient=tk.VERTICAL)

left = tk.Label(paned, text='Painel Esquerdo', bg='lightblue')
right = tk.Label(paned, text='Painel Direito', bg='lightgreen')

paned.add(left)
paned.add(right)

paned.pack(fill='both', expand=True)

root.mainloop()