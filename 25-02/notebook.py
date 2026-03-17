import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('500x300')
root.title('Exemplo Notebook')

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

frame1 = ttk.Frame(notebook, width=500, height=280)
frame2 = ttk.Frame(notebook, width=500, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')

tk.Label(frame1, text='Label of the General Information').pack(pady=20)
tk.Label(frame2, text='Edit profile').pack(pady=20)

root.mainloop()