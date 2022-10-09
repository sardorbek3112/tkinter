from tkinter import*
def change():
    label.config(text = 'hello Sardorbek!!!',bg = 'blue')
root = Tk()
main = Frame(root)
root.title('my_App')
main.configure(bg='yellow')
label = Label(main,text = '',bg = 'yellow')
label.grid(row = 0,column = 0)
label.pack(padx = 5,pady = 10)
button = Button(main,command=change,width = 10,text = 'press me!')

button.pack(padx = 5,pady = 10)
main.pack(padx = 10,pady = 10)
root.mainloop()