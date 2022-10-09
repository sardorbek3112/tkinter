from tkinter import *
from random import randint
def tozala():
    textbox_output1.delete(0.0, END)
def hisobla():
    number = textbox_output.get()
    t_son = str (eval(number)) + '\n'
    textbox_output1.delete(0.0, END)
    textbox_output1.insert(END, t_son)
def qoshish():
    textbox_output.insert(END, '+')
def ayir():
    textbox_output.insert(END, '-')
def bol():
    textbox_output.insert(END, '/')
def kop():
    textbox_output.insert(END, '*')
def bir():
    textbox_output.insert(END, '1')
def ikki():
    textbox_output.insert(END, '2')
def uch():
    textbox_output.insert(END, '3')
def tort():
    textbox_output.insert(END, '4')
def besh():
    textbox_output.insert(END, '5')
def olti():
    textbox_output.insert(END, '6')
def yetti():
    textbox_output.insert(END, '7')
def sakkiz():
    textbox_output.insert(END, '8')
def toqqiz():
    textbox_output.insert(END, '9')
def nol():
    textbox_output.insert(END, '0')

window = Tk()
window.title('Kalkulator')
window.geometry('250x250')
window.configure(background='black')


textbox_output = Entry(window, width=15)
textbox_output.grid (row=0, column=0)

textbox_output1 = Text(window, width=15,height = 1)
textbox_output1.grid (row=0, column=1)

kubik_bir = Button(window,text="1", command=bir)
kubik_bir.grid(row=1,column=0)

kubik_ikki = Button(window,text="2", command=ikki)
kubik_ikki.grid(row=1,column=1)

kubik_uch = Button(window,text="3", command=uch)
kubik_uch.grid(row=1,column=2)

kubik_qosh = Button(window,text="+", command=qoshish)
kubik_qosh.grid(row=1,column=3)

kubik_tort = Button(window,text="4", command=tort)
kubik_tort.grid(row=2,column=0)

kubik_besh = Button(window,text="5", command=besh)
kubik_besh.grid(row=2,column=1)

kubik_olti = Button(window,text="6", command=olti)
kubik_olti.grid(row=2,column=2)

kubik_kop = Button(window,text="*", command=kop)
kubik_kop.grid(row=2,column=3)

kubik_yetti = Button(window,text="7", command=yetti)
kubik_yetti.grid(row=3,column=0)

kubik_sakkiz = Button(window,text="8", command=sakkiz)
kubik_sakkiz.grid(row=3,column=1)

kubik_toqqiz = Button(window,text="9", command=toqqiz)
kubik_toqqiz.grid(row=3,column=2)

kubik_ayir = Button(window,text="-", command=ayir)
kubik_ayir.grid(row=3,column=3)

kubik_nol = Button(window,text="0", command=nol)
kubik_nol.grid(row=4,column=0)

kubik_tozala = Button(window,text="C", command=tozala)
kubik_tozala.grid(row=4,column=1)

kubik_hisobla = Button(window,text="=", command=hisobla)
kubik_hisobla.grid(row=4,column=2)

kubik_bol = Button(window,text="/", command=bol)
kubik_bol.grid(row=4,column=3)


window.mainloop()