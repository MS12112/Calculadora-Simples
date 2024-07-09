# importando tkinter
from tkinter import *

root = Tk()
root.title("Calculdora")

#Funções
def deletar():
    visor.delete(0, END)


def click_ponto():
    visor.insert(END, ".") 


def click_soma():
    primeiro_numero = visor.get()
    global p_numero 
    global matematica
    matematica = "soma"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)


def click_sub():
    primeiro_numero = visor.get()
    global p_numero 
    global matematica
    matematica = "subtracao"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)


def click_divi():
    primeiro_numero = visor.get()
    global p_numero 
    global matematica
    matematica = "divisao"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)


def click_multi():
    primeiro_numero = visor.get()
    global p_numero 
    global matematica
    matematica = "multiplicacao"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)


def click_igual():
    segundo_numero = visor.get()
    visor.delete(0, END)
    if matematica == "soma":
        visor.insert(0, p_numero + float(segundo_numero))

    if matematica == "subtracao":
        visor.insert(0, p_numero - float(segundo_numero))

    if matematica == "multiplicacao":
        visor.insert(0, p_numero * float(segundo_numero))

    if matematica == "divisao":
        visor.insert(0, p_numero / float(segundo_numero))


def click_button(numero):
    atual = visor.get()
    visor.delete(0,END)
    visor.insert(END, str(atual)+ str(numero))


lb1 = Label(root, text="CALCULADORA", font=("verdana", 14, "bold"), pady=10)
lb1.pack()

visor = Entry(root, width=40, bg="lightblue", )
visor.pack(pady=3, ipady=10)

#Fileira 1:]
bt1 = Button(root, text="1", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(1))
bt1.place(x=10, y=100)

bt2 = Button(root, text="2", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(2) )
bt2.place(x=10, y=155)

bt3 = Button(root, text="3", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(3) )
bt3.place(x=10, y=210)

bt0 = Button(root, text="0", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(0))
bt0.place(x=10, y=265)

#Fileira 2

bt4 = Button(root, text="4", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(4))
bt4.place(x=60, y=100)

bt5 = Button(root, text="5", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(5))
bt5.place(x=60, y=155)

bt6 = Button(root, text="6", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(6))
bt6.place(x=60, y=210)

btPonto = Button(root, text=".", bg="lightblue", pady=14, padx=44, command=click_ponto)  
btPonto.place(x=60, y=267)

#Fileira 3

bt7 = Button(root, text="7", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(7))
bt7.place(x=110, y=100)

bt8 = Button(root, text="8", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(8))
bt8.place(x=110, y=155)

bt9 = Button(root, text="9", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(9))
bt9.place(x=110, y=210)

#Fileira 4

btsoma = Button(root, text="+", bg="lightblue", pady=14, padx=14, bd=4, command=click_soma)
btsoma.place(x=160, y=100)

btsubtracao = Button(root, text="-", bg="lightblue", pady=14, padx=14, bd=4, command=click_sub)
btsubtracao.place(x=160, y=155)

btmultiplicacao = Button(root, text="x", bg="lightblue", pady=14, padx=14, bd=4, command=click_multi)
btmultiplicacao.place(x=160, y=210)

btdivisao = Button(root, text="/", bg="lightblue", pady=14, padx=14, bd=4, command=click_divi)
btdivisao.place(x=160, y=265)

#Botão de CE:

btce = Button(root, text="CE", bg="lightblue", pady=119, padx=14, bd=4, command=deletar)
btce.place(x=210, y=100)

#Botão de igual:

btce = Button(root, text="=", bg="lightblue", pady=14, padx=117, bd=4, command=click_igual)
btce.place(x=10, y=320)

root.resizable(False, False)
root.geometry("280x380")
root.mainloop()
