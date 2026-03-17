import tkinter as tk

root = tk.Tk()
paned = tk.PanedWindow(root, orient="horizontal")
paned.pack(fill="both", expand=True)

left = tk.Label(paned, text="Painel Esquerdo", bg="lightblue")
right = tk.Label(paned, text="Painel Direito", bg="lightgreen")

paned.add(left)
paned.add(right)

root.mainloop()
