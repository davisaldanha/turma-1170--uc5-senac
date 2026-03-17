import tkinter as tk

def main_window():
    root = tk.Tk()
    root.title('Aula 02 - Tkinter')
    root.geometry('500x300')

    root.configure(bg='#000000')

    title_pg = tk.Label(root, 
                        text='Aula 02 - Tkinter', 
                        fg='#ffffff',
                        bg='#000000',
                        font=('Berlin Sans FB', 18))
    title_pg.pack(pady=(10, 5))

    name_lb = tk.Label(root, 
                        text='Nome Completo', 
                        fg='#ffffff',
                        bg='#000000',
                        font=('Berlin Sans FB', 12),
                        anchor='w'
                        )
    name_lb.pack(pady=5, padx=10, fill='both')

    var_name = tk.StringVar()
    name_entry = tk.Entry(root, textvariable=var_name, font=('Berlin Sans FB', 12))
    name_entry.pack(padx=10, fill='both')

    description_lb = tk.Label(root, 
                        text='Descreva suas habilidades', 
                        fg='#ffffff',
                        bg='#000000',
                        font=('Berlin Sans FB', 12),
                        anchor='w')
    description_lb.pack(pady=5, padx=10, fill='both')

    description_text = tk.Text(root, height=5, font=('Berlin Sans FB', 12))
    description_text.pack(padx=10, fill='x')

    def event_button():
        var_description = description_text.get('1.0', tk.END).strip()
        root.destroy()
        second_window(var_name.get(), var_description)
        

    button = tk.Button(root, 
                       bg='#ffff00', 
                       text='Enviar', 
                       font=('Berlin Sans FB', 12, 'bold'), 
                       fg='#000000',
                       command=event_button)
    button.pack(pady=10)

    root.mainloop()

def second_window(name, description):
    root = tk.Tk()
    root.title('Aula 02 - Tkinter')
    root.geometry('500x300')

    root.configure(bg='#000000')

    title_pg = tk.Label(root, 
                        text='Aula 02 - Tkinter', 
                        fg='#ffffff',
                        bg='#000000',
                        font=('Berlin Sans FB', 18))
    title_pg.pack(pady=(10, 5))

    name_title_lb = tk.Label(root, 
                        text='Nome Completo', 
                        fg='#ffffff',
                        bg='#000000',
                        font=('Berlin Sans FB', 12, 'bold'),
                        anchor='w'
                        )
    name_title_lb.pack(pady=5, padx=10, fill='both')

    name_lb = tk.Label(root, 
                        text=name, 
                        fg='#ffffff',
                        bg='#000000',
                        font=('Berlin Sans FB', 12),
                        anchor='w')
    name_lb.pack(pady=(0, 5), padx=10, fill='x')

    description_title_lb = tk.Label(root, 
                        text='Habilidades', 
                        fg='#ffffff',
                        bg='#000000',
                        font=('Berlin Sans FB', 12, 'bold'),
                        anchor='w')
    description_title_lb.pack(pady=(5, 0), padx=10, fill='both')

    description_lb = tk.Label(root, 
                        text=description, 
                        fg='#ffffff',
                        bg='#000000',
                        font=('Berlin Sans FB', 12),
                        anchor='w',
                        wraplength=500,
                        justify='left'
                        )
    
    description_lb.pack(pady=(0, 5), padx=10, fill='x')

    root.mainloop()

if __name__ == "__main__":
    main_window()



