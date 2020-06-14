from tkinter import *

def leftClickButton(event):
    bmi = int(textBoxWeight.get()) / ((int(textBoxHeight.get()) / 100) ** 2)
    if bmi >= 30:
        labelResult.configure(text="อ้วนมาก")
    elif bmi >= 25:
        labelResult.configure(text="อ้วน")
    elif bmi >= 23:
        labelResult.configure(text="น้ำหนักเกิน")
    elif bmi >= 18.6:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        labelResult.configure(text="ผอมเกินไป")

home = Tk()
labelHeight = Label(home, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(home)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(home, text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(home)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(home, text="คำนวณ")
calculateButton.bind("<Button-1>", leftClickButton)
calculateButton.grid(row=2)
labelResult = Label(home, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)
home.mainloop()