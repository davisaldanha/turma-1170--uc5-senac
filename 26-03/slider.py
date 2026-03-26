'''Exemplo de uso do widget Scale (Slider)'''

from customtkinter import *

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title('Exemplo do Scale')
        self.geometry('400x300')

        self.slider = CTkSlider(
            self,
            from_=0,
            to=100,
            width=200,
            height=30,
            button_color='green',
            progress_color='blue',
            fg_color='lightgray',
            command=self.slider_event,
            number_of_steps=10
        )

        self.slider.pack(pady=20)
    
    def slider_event(self, value):
        print(f'Valor selecionado: {value:.2f}')

if __name__ == "__main__":
    app = App()
    app.mainloop()