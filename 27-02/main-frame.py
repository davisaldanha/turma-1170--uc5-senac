import tkinter as tk
from tkinter import messagebox
from datetime import datetime as dt


def verificar_checkbutton():
    estado = var_check.get()
    if estado == 1:
        messagebox.showinfo('Selecionado', 'Você selecionou o item!')
    else:
        messagebox.showinfo('Não Selecionado', 'Você não selecionou o item!')

def mostrar_opcao_radio():
    messagebox.showinfo('Opção Selecionada', f'Selecionado: {var_radio.get()}')


root = tk.Tk()
root.title('Revisão Widgets')
root.geometry('700x400')

date_now = dt.now()

dias_semana = [ 'Segunda-Feira', 'Terça-Feira', 
                'Quarta_feira', 'Quinta-Feira', 
                'Sexta-Feira', 'Sábado', 'Domingo']

#Label
tk.Label(root, text=f"{dias_semana[date_now.weekday()]} - {dt.strftime(date_now, '%d/%m/%Y')}",
         font=('Caprasimo', 16), fg='green').pack(fill='both', pady=(20, 5))

#Frame
frame = tk.Frame(root, bg='#333333', padx=10, pady=10, width=500, height=100)
frame.pack_propagate(False)
frame.pack(pady=20)

#Botão dentro do frame
btn_frame = tk.Button(frame, text='Botão do Frame', command=verificar_checkbutton).pack(pady=5)

#Checkbutton exemplo
var_check = tk.IntVar()
checkbutton = tk.Checkbutton(frame, text='Opção', variable=var_check, bg='#75701b')
checkbutton.pack()

#Frame 2
frame2 = tk.Frame(root, bg='#555555', pady=10, padx=10, width=500, height=100)
frame2.pack_propagate(False)
frame2.pack(pady=20)

#RadioButtons dentro do frame2
var_radio = tk.StringVar(value="Opção 1")
radio1 = tk.Radiobutton(frame2, text='Opção 1', variable=var_radio, value='Opção 1', bg='#555555')
radio2 = tk.Radiobutton(frame2, text='Opção 2', variable=var_radio, value='Opção 2', bg='#555555')
radio1.pack()
radio2.pack()

#Botão para mostrar a opção selecionada
btn_radio = tk.Button(frame2, text='Mostrar Opção', command=mostrar_opcao_radio)
btn_radio.pack(pady=10)


root.mainloop()