from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.title("Vienādie attēli")

btn0=Button(width=20, height=30)
btn1=Button(width=20, height=30)
btn2=Button(width=20, height=30)
btn3=Button(width=20, height=30)
btn4=Button(width=20, height=30)
btn5=Button(width=20, height=30)
btn6=Button(width=20, height=30)
btn7=Button(width=20, height=30)
btn8=Button(width=20, height=30)
btn9=Button(width=20, height=30)
btn10=Button(width=20, height=30)
btn11=Button(width=20, height=30)

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=0, column=4)
btn5.grid(row=0, column=5)

btn6.grid(row=1, column=0)
btn7.grid(row=1, column=1)
btn8.grid(row=1, column=2)
btn9.grid(row=1, column=3)
btn10.grid(row=1, column=4)
btn11.grid(row=1, column=5)


myImg1=ImageTk.PhotoImage(Image.open("1.png"))
myImg2=ImageTk.PhotoImage(Image.open("2.png"))
myImg3=ImageTk.PhotoImage(Image.open("3.png"))
myImg4=ImageTk.PhotoImage(Image.open("4.png"))
myImg5=ImageTk.PhotoImage(Image.open("5.png"))
myImg6=ImageTk.PhotoImage(Image.open("6.png"))

bgImg=ImageTk.PhotoImage(Image.open(""))

gameWindow.mainloop()