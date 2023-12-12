from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.title("Vienādie attēli")

btn0=Button(width=200, height=300)
btn1=Button(width=200, height=300)
btn2=Button(width=200, height=300)
btn3=Button(width=200, height=300)
btn4=Button(width=200, height=300)
btn5=Button(width=200, height=300)
btn6=Button(width=200, height=300)
btn7=Button(width=200, height=300)
btn8=Button(width=200, height=300)
btn9=Button(width=200, height=300)
btn10=Button(width=200, height=300)
btn11=Button(width=200, height=300)

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


gameWindow.mainloop()