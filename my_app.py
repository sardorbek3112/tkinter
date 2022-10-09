from tkinter import *
from random import randint
def tozala():
    textbox_output.delete(0.0, END)
def qoshish():
    number = int(textbox_input.get())
    number1 = int(textbox_input1.get())
    
    t_son = str (number+number1) + '\n'
    textbox_output.insert(END, t_son)
def kop():
    number = int(textbox_input.get())
    number1 = int(textbox_input1.get())
    t_son = str (number*number1) + '\n'
    textbox_output.insert(END, t_son)
def bol():
    number = int(textbox_input.get())
    number1 = int(textbox_input1.get())
    t_son = str (number/number1) + '\n'
    textbox_output.insert(END, t_son)
def ayir():
    number = int(textbox_input.get())
    number1 = int(textbox_input1.get())
    t_son = str (number-number1) + '\n'
    textbox_output.insert(END, t_son)
window = Tk()
window.title('Kalkulator')
window.geometry('250x250')
window.configure(background='yellow')
input_label = Label (window,text='Son: ', bg='yellow')
input_label.grid (row=0, column=0)

output_label = Label(window, text ='\nNatija', bg='yellow')
output_label.grid(row=2, column=0)

textbox_input = Entry(window, width=15)
textbox_input.grid (row=1, column=0)

textbox_input1 = Entry(window, width=15)
textbox_input1.grid (row=1, column=1)

textbox_output = Text(window, width=15,height = 5)
textbox_output.grid (row=4, column=0)

kubik_qosh = Button(window,text="qo'shish", command=qoshish)
kubik_qosh.grid(row=2,column=0)

kubik_kop = Button(window,text="ko`paytirish", command=kop)
kubik_kop.grid(row=2,column=1)

kubik_ayir = Button(window,text="ayirish", command=ayir)
kubik_ayir.grid(row=3,column=0)

kubik_bol = Button(window,text="bo`lish", command=bol)
kubik_bol.grid(row=3,column=1)

kubik_tozala = Button(window,text="tozalash", command=tozala)
kubik_tozala.grid(row=4,column=1)

window.mainloop()