# Scientific calculator using tkinter
# john Diaz 
# january 2023
# Based on Tkinter Course - Create Graphic User Interfaces in Python Tutorial video freecodecamp.org

# TO DO List:
#
#


from tkinter import *


# Defining functions for add, substraction, multiplication and division

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b


root = Tk()
root.title("Scientific Calculator")
calc = Entry(root, width=40, borderwidth=7, bg="white", fg="black")
calc.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define function to show clicked numbers in the box
def btnClick(number):
    
    # Get the current number
    current = calc.get()
    # Delete the previous string in the box
    calc.delete(0, END) 
    # Insert the clicked number concatenated with the previous
    calc.insert(0, str(current) + str(number))


def btnClearF():
    calc.delete(0, END) 

def btnAddF():
    number1 = calc.get()
    global num1 
    num1= int(number1)
    global operator
    operator="add"
    calc.delete(0, END) 
    
def btnSubsF():
    number1 = calc.get()
    global num1 
    num1= int(number1)
    global operator
    operator="subs"
    calc.delete(0, END) 
 
def btnMultF():
    number1 = calc.get()
    global num1 
    num1= int(number1)
    global operator
    operator="mult"
    calc.delete(0, END) 
    
def btnDivF():
    number1 = calc.get()
    global num1 
    num1= int(number1)
    global operator
    operator="div"
    calc.delete(0, END) 

    
def btnEqualF():
    num2 = int(calc.get())
    calc.delete(0, END) 
    # Select the result base in the operator
    match operator:
        case "add":
            calc.insert(0, str(num1+num2))

        case "subs":
            calc.insert(0, str(num1-num2))
    
        case "mult":
            calc.insert(0, str(num1*num2))
            
        case "div":
            calc.insert(0, str(num1/num2))
            
        case _:
            calc.insert(0, " Error")
    
# Define Buttons
btn0 = Button(root, text="0", padx=25,pady=25, command=lambda: btnClick(0))
btn1 = Button(root, text="1", padx=25,pady=25, command=lambda: btnClick(1))
btn2 = Button(root, text="2", padx=25,pady=25, command=lambda: btnClick(2))
btn3 = Button(root, text="3", padx=25,pady=25, command=lambda: btnClick(3))
btn4 = Button(root, text="4", padx=25,pady=25, command=lambda: btnClick(4))
btn5 = Button(root, text="5", padx=25,pady=25, command=lambda: btnClick(5))
btn6 = Button(root, text="6", padx=25,pady=25, command=lambda: btnClick(6))
btn7 = Button(root, text="7", padx=25,pady=25, command=lambda: btnClick(7))
btn8 = Button(root, text="8", padx=25,pady=25, command=lambda: btnClick(8))
btn9 = Button(root, text="9", padx=25,pady=25, command=lambda: btnClick(9))

btnEqual = Button(root, text="=", padx=50,pady=25, command=btnEqualF)

btnClear = Button(root, text="AC", padx=25,pady=25, command=btnClearF)
btnDel   = Button(root, text="del", padx=25,pady=25, command=lambda: btnClick(00))
btnAdd   = Button(root, text="+", padx=25,pady=25, command= btnAddF)
btnSubs  = Button(root, text="-", padx=25,pady=25, command= btnSubsF)
btnMult  = Button(root, text="x", padx=25,pady=25, command= btnMultF)
btnDiv   = Button(root, text="÷", padx=25,pady=25, command= btnDivF)

btnDot = Button(root, text=".", padx=25,pady=25, command=lambda: btnClick(00)) 
btnExp = Button(root, text="Exp", padx=25,pady=25, command=lambda: btnClick(00)) 


# Put buttons on the screen
btn0.grid(row=4, column=0)
btnDot.grid(row=4, column=1)
btnExp.grid(row=4, column=2)
btnEqual.grid(row=4, column=3, columnspan=2)


btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btnMult.grid(row=3, column=3)
btnAdd.grid(row=3, column=4)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btnDiv.grid(row=2, column=3)
btnSubs.grid(row=2, column=4)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btnDel.grid(row=1, column=3)
btnClear.grid(row=1, column=4)

root.mainloop()