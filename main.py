# importando tkinter
from tkinter import *
from tkinter import ttk

#cores

cor1 = "#1e1f1e"     #preto
cor2 = "#feffff"     #branco
cor3 = "#38576b"     #azul
cor4 = "#292929"     #cinza
cor5 = "#FFAB40"     #laranja    
cor6 = "#2e2e2e"        

janela = Tk()
janela.title("Calculadora")
janela.geometry("250x335")
janela.config(bg=cor1)


#criando frames

frame_tela = Frame(janela, width=315, height=110, bg=cor4)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=315, height=335, bg=cor1)
frame_corpo.grid(row=1, column=0)


todos_valores = ''
texto_tela = StringVar()

#criando funcoes
def entrar_valores(event):
    
    global todos_valores
    
    todos_valores = todos_valores + str(event)

    #passando o valor para tela
    texto_tela.set(todos_valores)
    
def calcular():
    global todos_valores
    
    resultado = eval(todos_valores)
    
    texto_tela.set(resultado)


def limpar_tela():
    global todos_valores
    
    todos_valores = ""
    texto_tela.set("")

#criando label

app_label = Label(frame_tela, textvariable=texto_tela, width=10, height=1, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 30'), bg=cor4, fg=cor2)
app_label.place(x=0, y=60)

#criando botoes

b_1 = Button(frame_corpo, command= limpar_tela, text="C", width=7, height=2, bg=cor3, fg=cor2, relief=RAISED, overrelief=RIDGE)
b_1.place(x=4, y=4)

b_2 = Button(frame_corpo, command= limpar_tela, text="CE", width=7, height=2, bg=cor6, fg=cor2, relief=RAISED, overrelief=RIDGE)
b_2.place(x=65, y=4)

b_3 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_3.place(x=126, y=4)

b_4 = Button(frame_corpo, command = lambda: entrar_valores('/'), text="÷", width=7, height=2, bg=cor5, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_4.place(x=187, y=4)

b_5 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_5.place(x=4, y=48)

b_6 = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_6.place(x=65, y=48)

b_7 = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_7.place(x=126, y=48)

b_8 = Button(frame_corpo, command = lambda: entrar_valores('*'), text="x", width=7, height=2, bg=cor5, fg=cor2, relief=RAISED, overrelief=RIDGE)
b_8.place(x=187, y=48)

b_9 = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_9.place(x=4, y=92)

b_10 = Button(frame_corpo, command = lambda: entrar_valores('5'), text="5", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_10.place(x=65, y=92)

b_11 = Button(frame_corpo, command = lambda: entrar_valores('6'), text="6", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_11.place(x=126, y=92)

b_12 = Button(frame_corpo, command = lambda: entrar_valores('-'), text="-", width=7, height=2, bg=cor5, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_12.place(x=187, y=92)

b_13 = Button(frame_corpo, command = lambda: entrar_valores('1'), text="1", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_13.place(x=4, y=136)

b_14 = Button(frame_corpo, command = lambda: entrar_valores('2'), text="2", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_14.place(x=65, y=136)

b_15 = Button(frame_corpo, command = lambda: entrar_valores('3'), text="3", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_15.place(x=126, y=136)

b_16 = Button(frame_corpo, command = lambda: entrar_valores('+'), text="+", width=7, height=2, bg=cor5, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_16.place(x=187, y=136)

b_17 = Button(frame_corpo, text="±", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_17.place(x=4, y=180)

b_18 = Button(frame_corpo, command = lambda: entrar_valores('0'), text="0", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_18.place(x=65, y=180)

b_19 = Button(frame_corpo, command = lambda: entrar_valores('.'), text=",", width=7, height=2, bg=cor6, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_19.place(x=126, y=180)

b_20 = Button(frame_corpo, command = calcular, text="=", width=7, height=2, bg=cor5, fg=cor2,  relief=RAISED, overrelief=RIDGE)
b_20.place(x=187, y=180)


janela.mainloop()
