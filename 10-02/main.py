import tkinter as tk

def main_window():
    janela = tk.Tk()
    janela.title('Minha Primeira GUI')
    janela.geometry('500x500')

    #Configurações Básicas da Janela
    '''
    - Título ✅
    - Tamanho ✅
    - Redimensionamento ✅
    - Ícone ✅
    - Cor de Fundo ✅
    - Fonte Padrão ✅
    - Widgets - Label e Button ✅
    '''
    # Redimensionamento
    janela.resizable(width=False, height=False)

    #Ícone da janela
    janela.iconbitmap('./computador.ico')

    #Cor de Fundo
    janela.configure(bg="#5391c7")

    #Fonte Padrão
    janela.option_add('*Font', 'Autography 24')

    #Widgets  - Adicionando um rótulo
    pg_title = tk.Label(janela, text='Olá, Mundo!', 
                        font=('Britannic Bold', 24), fg='#c75357', bg='#5391c7')
    pg_title.pack(pady=20)

    #Widget - Adicionando uma imagem
    image = tk.PhotoImage(file='python.png', format='png')

    image = image.subsample(4)
    img_label = tk.Label(janela, image=image, bg='#5391c7')

    img_label.pack(pady=20)

    #Widget - Adicionando um botão
    def event_button():
        pg_title.config(text="Botão Ativado!") 
        #janela.destroy() # Para destruir(encerrar) uma janela

    button = tk.Button(janela, text='Clique aqui!', command=event_button)
    button.pack(pady=20)


    janela.mainloop()

def login_window():
    pass

def initial_window():
    pass

if __name__ == "__main__":
    main_window()
