from tkinter import *
window=Tk()
window.title('Smaylik')
c=Canvas(window, width=400, height=400)
c.pack()
head=c.create_oval(50,50,350,350, fill='yellow')
eye1=c.create_oval(120,130,170,180,fill='white')
eyeball1=c.create_oval(135,145,155,165,fill='black')
eye2=c.create_oval(220,130,270,180, fill='white')
eyeball2=c.create_oval(235,145,255,165,fill='black')
mouth=c.create_oval(130,225,260,270,fill='red')
def eye_right():
    c.move(eyeball1, -10, 0)
    c.move(eyeball2, -10, 0)
    c.itemconfig(mouth, fill='gray')
def eye_left():
    c.move(eyeball1, 10, 0)
    c.move(eyeball2, 10, 0)
    c.itemconfig(mouth, fill='red')
def blink():
    c.itemconfig(eye1, fill='yellow')
    c.itemconfig(eyeball1, state='hidden')
    c.itemconfig(eye2, fill='yellow')
    c.itemconfig(eyeball2, state='hidden')
def unblink():
    c.itemconfig(eye1, fill='white')
    c.itemconfig(eyeball1, state='NORMAL')
    c.itemconfig(eye2, fill='white')
    c.itemconfig(eyeball2, state='NORMAL')
def mouth_open():
    c.itemconfig(mouth, fill='gray')
def mouth_close():
    c.itemconfig(mouth, fill='red')
def cange(event):
    eye_right()
    mouth_open()
def change(event):
    eye_left()
    mouth_close()
window.attributes('-topmost',1)
c.bind_all('<Right>', cange)
c.bind_all('<Left>', change)
window.mainloop()