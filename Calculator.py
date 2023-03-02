"""
    Basic calculator using tkinter
    John Diaz
    January 2023
    Based on Tkinter Course - Create Graphic User Interfaces in Python
    Tutorial video freecodecamp.org

    TO DO List:


    """

from tkinter import *


# Defining functions for add, substraction, multiplication and division

def suma(a, b):
    return a+b


def resta(a, b):
    return a-b


def multi(a, b):
    return a*b


def div(a, b):
    return a/b


root = Tk()
root.title("Calculator")
root.resizable(0,0)
root.option_add( "*font", "lucida 23 bold " )
calc = Entry(root, width=25, borderwidth=7, bg="white", fg="black")
calc.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def btn_click(number):
    # Function to show clicked numbers in the box

    # Get the current number
    current = calc.get()
    # Delete the previous string in the box
    calc.delete(0, END)
    # Insert the clicked number concatenated with the previous
    calc.insert(0, str(current) + str(number))


def btn_clear_func():
    calc.delete(0, END)


def btn_add_func():
    number1 = calc.get()
    global num1
    num1 = int(number1)
    global operator
    operator = "add"
    calc.delete(0, END)


def btn_subs_func():
    number1 = calc.get()
    global num1
    num1 = int(number1)
    global operator
    operator = "subs"
    calc.delete(0, END)


def btn_mult_func():
    number1 = calc.get()
    global num1
    num1 = int(number1)
    global operator
    operator = "mult"
    calc.delete(0, END)


def btn_div_func():
    number1 = calc.get()
    global num1
    num1 = int(number1)
    global operator
    operator = "div"
    calc.delete(0, END)


def btn_equal_func():
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
# Number's buttons
btn0 = Button(root, text="0", padx=25, pady=25, command=lambda: btn_click(0))
btn1 = Button(root, text="1", padx=25, pady=25, command=lambda: btn_click(1))
btn2 = Button(root, text="2", padx=25, pady=25, command=lambda: btn_click(2))
btn3 = Button(root, text="3", padx=25, pady=25, command=lambda: btn_click(3))
btn4 = Button(root, text="4", padx=25, pady=25, command=lambda: btn_click(4))
btn5 = Button(root, text="5", padx=25, pady=25, command=lambda: btn_click(5))
btn6 = Button(root, text="6", padx=25, pady=25, command=lambda: btn_click(6))
btn7 = Button(root, text="7", padx=25, pady=25, command=lambda: btn_click(7))
btn8 = Button(root, text="8", padx=25, pady=25, command=lambda: btn_click(8))
btn9 = Button(root, text="9", padx=25, pady=25, command=lambda: btn_click(9))

# Function's buttons
btn_equal = Button(root, text="=", padx=50, pady=25, command=btn_equal_func)
btn_clear = Button(root, text="AC", padx=25, pady=25, command=btn_clear_func)
btn_del = Button(root, text="del", padx=25, pady=25, command=lambda: btn_click(00))
btn_add = Button(root, text="+", padx=25, pady=25, command=btn_add_func)
btn_subs = Button(root, text="-", padx=25, pady=25, command=btn_subs_func)
btn_mult = Button(root, text="x", padx=25, pady=25, command=btn_mult_func)
btn_div = Button(root, text="÷", padx=25, pady=25, command=btn_div_func)

# Put buttons on the screen
# Row 4 buttons
btn0.grid(row=4, column=0)
btn_equal.grid(row=4, column=1, columnspan=4)

# Row 3 buttons
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn_mult.grid(row=3, column=3)
btn_add.grid(row=3, column=4)

# Row 2 buttons
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn_div.grid(row=2, column=3)
btn_subs.grid(row=2, column=4)

# Row 1 buttons
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn_del.grid(row=1, column=3)
btn_clear.grid(row=1, column=4)

root.mainloop()
