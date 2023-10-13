from tkinter import *
import math

class Calculadora:
    def __init__(self):
        self.janela = Tk()

        self.janela.title("Calculadora")
        self.janela.geometry('415x315')
        self.janela.iconbitmap("Calculadora_Logo.ico")
        self.janela.resizable(0,0)
        self.CanvasContainer = Canvas(self.janela, bg='#112348', height=500, width=500)
        self.CanvasContainer.pack()

        #Label

        self.LabelMostrador =Label(self.janela, bg='White', justify="right", text="0.00", font="Arial 20", borderwidth=10, relief="sunken", anchor="e")
        self.LabelMostrador.place(x=10,y=10,width=392,height=50)

        #Buttons

        self.bt1 = Button(self.janela, text="9",bg="#6E6B6D", fg="white", font="Arial 20", command=lambda: self.AdicionarNumero('9'))
        self.bt1.place(x=10, y=70, width=75, height=55)
        self.bt2 = Button(self.janela, text="8",bg="#6E6B6D", fg="white", font="Arial 20", command=lambda: self.AdicionarNumero('8'))
        self.bt2.place(x=90,y=70,width=75,height=55)
        self.bt3 = Button(self.janela, text="7",bg="#6E6B6D", fg="white", font="Arial 20", command=lambda: self.AdicionarNumero('7'))
        self.bt3.place(x=170, y=70, width=75, height=55)
        self.bt4 = Button(self.janela, text="√",bg="#B8B4B7", fg="white", font="Arial 20", command=lambda: self.AdicionarOperador('√'))
        self.bt4.place(x=250, y=70, width=75, height=55)
        self.bt5 = Button(self.janela, text="AC",bg='#2CA5EF', font="Arial 20", command=self.Limpar)
        self.bt5.place(x=330, y=70, width=75, height=55)
        self.bt6 = Button(self.janela, text="6",bg="#6E6B6D", fg="white", font="Arial 20", command=lambda: self.AdicionarNumero('6'))
        self.bt6.place(x=10, y=130, width=75, height=55)
        self.bt7 = Button(self.janela, text="5",bg="#6E6B6D", fg="white", font="Arial 20", command=lambda: self.AdicionarNumero('5'))
        self.bt7.place(x=90, y=130, width=75, height=55)
        self.bt8 = Button(self.janela, text="4",bg="#6E6B6D", fg="white", font="Arial 20", command=lambda: self.AdicionarNumero('4'))
        self.bt8.place(x=170, y=130, width=75, height=55)
        self.bt9 = Button(self.janela, text="*",bg="#B8B4B7", fg="white", font="Arial 20", command=lambda: self.AdicionarOperador('*'))
        self.bt9.place(x=250, y=130, width=75, height=55)
        self.bt10 = Button(self.janela, text="/",bg="#B8B4B7", fg="white", font="Arial 20", command=lambda: self.AdicionarOperador('/'))
        self.bt10.place(x=330, y=130, width=75, height=55)
        self.bt11 = Button(self.janela, text="3",bg="#6E6B6D", fg="white", font="Arial 20", command=lambda: self.AdicionarNumero('3'))
        self.bt11.place(x=10, y=190, width=75, height=55)
        self.bt12 = Button(self.janela, text="2",bg="#6E6B6D", fg="white", font="Arial 20", command=lambda: self.AdicionarNumero('2'))
        self.bt12.place(x=90, y=190, width=75, height=55)
        self.bt13 = Button(self.janela, text="1",bg="#6E6B6D", fg="white", font="Arial 20", command=lambda: self.AdicionarNumero('1'))
        self.bt13.place(x=170, y=190, width=75, height=55)
        self.bt14 = Button(self.janela, text="+",bg="#B8B4B7", fg="white", font="Arial 20", command=lambda: self.AdicionarOperador('+'))
        self.bt14.place(x=250, y=190, width=75, height=55)
        self.bt15 = Button(self.janela, text="-",bg="#B8B4B7", fg="white", font="Arial 20", command=lambda: self.AdicionarOperador('-'))
        self.bt15.place(x=330, y=190, width=75, height=55)
        self.bt16 = Button(self.janela, text="0",bg="#6E6B6D", fg="white", font="Arial 20", command=lambda: self.AdicionarNumero('0'))
        self.bt16.place(x=10, y=250, width=75, height=55)
        self.bt17 = Button(self.janela, text=".",bg="#B8B4B7", fg="white", font="Arial 25", command=lambda: self.AdicionarPonto('.'))
        self.bt17.place(x=90, y=250, width=75, height=55)
        self.bt18 = Button(self.janela, text="^",bg="#B8B4B7", fg="white", font="Arial 20", command=lambda: self.AdicionarOperador('^'))
        self.bt18.place(x=170, y=250, width=75, height=55)
        self.bt19 = Button(self.janela, text="=",bg='#2CA5EF', font="Arial 20", command=self.Calcular)
        self.bt19.place(x=250, y=250, width=155, height=55)
        
        self.janela.mainloop()

    def RaizQuadrada(self):
        numero = float(self.LabelMostrador["text"])
        resultado = math.sqrt(numero)
        self.LabelMostrador["text"] = str(resultado)

    def Potenciacao(self, base, expoente):
        return math.pow(base, expoente)
    
    def AdicionarNumero(self, numero):
        NumeroAtual = self.LabelMostrador["text"]
        if (NumeroAtual == '0.00'):
            self.LabelMostrador["text"] = numero
        else:
            self.LabelMostrador["text"] = NumeroAtual + numero

    def AdicionarOperador(self, operador):
        NumeroAtual = self.LabelMostrador["text"]
        if NumeroAtual[-1] not in ['+', '-', '*', '/', '^', '√']:
            self.LabelMostrador["text"] = NumeroAtual + operador

    def AdicionarPonto(self, ponto):
        NumeroAtual = self.LabelMostrador["text"]
        if '.' not in NumeroAtual:
            self.LabelMostrador["text"] = NumeroAtual + ponto
 
    def Calcular(self):
        expressao = self.LabelMostrador["text"]
        if '√' in expressao:
            partes = expressao.split('√')
            if len(partes) == 2:
                try:
                    base = float(partes[1])
                    resultado = math.sqrt(base)
                    self.LabelMostrador["text"] = resultado
                except Exception as e:
                    self.LabelMostrador["text"] = "ERRO"
            else:
                self.LabelMostrador["text"] = "ERRO"
        else:
            if '^' in expressao:
                expressao = expressao.replace('^', '**')
            try:
                resultado = eval(expressao)
                self.LabelMostrador["text"] = str(resultado)
            except Exception as e:
                self.LabelMostrador["text"] = "ERRO"
                
    def Limpar(self):
        self.LabelMostrador["text"] = "0.00"

if __name__ == "__main__":
    CALCULADORA = Calculadora()