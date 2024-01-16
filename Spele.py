import time
from distutils.cmd import Command
from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.title("Vienādie attēli")

myImg0=ImageTk.PhotoImage(Image.open("1.png"))
myImg1=ImageTk.PhotoImage(Image.open("2.png"))
myImg2=ImageTk.PhotoImage(Image.open("3.png"))
myImg3=ImageTk.PhotoImage(Image.open("4.png"))
myImg4=ImageTk.PhotoImage(Image.open("5.png"))
myImg5=ImageTk.PhotoImage(Image.open("6.png"))

bgImg=ImageTk.PhotoImage(Image.open("7.png"))

ImageList=[myImg0,myImg0,myImg1,myImg1,myImg2,myImg2,myImg3,myImg3,myImg4,myImg4,myImg5,myImg5]
random.shuffle(ImageList)
myLabel=Label(image=myImg1)


btn0=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn0,0))
btn1=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn1,1))
btn2=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn2,2))
btn3=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn3,3))
btn4=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn4,4))
btn5=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn5,5))
btn6=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn6,6))
btn7=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn7,7))
btn8=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn8,8))
btn9=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn9,9))
btn10=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn10,10))
btn11=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn11,11))

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

count=0
correctAnswers=0
answers=[]
answers_dict={}
answerCount=0

def btnClick(btn,number):
    global count, correctAnswers, answers, answers_dict, answerCount
    if btn["image"]=="pyimage7" and count<2:
        btn["image"]=ImageList[number]
        count+=1
        answers.append(number)
        answers_dict[btn]=ImageList[number]
    if len(answers)==2:
        if ImageList[answers[0]]==ImageList[answers[1]]:
            for key in answers_dict:
                key["state"]=DISABLED
            correctAnswers=+2
            if correctAnswers==2:
                correctAnswers=0
                answerCount+=1
                    
        else:
            Tk.update(btn)
            time.sleep(1.5)
            for key in answers_dict:
                key["image"]="pyImage7"
        count=0
        answers=[]
        answers_dict={}
    if answerCount==4:
        messagebox.showinfo("You win!")
        reset()   
    
    return 0

gameWindow.mainloop()