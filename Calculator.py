from tkinter import *
import time
from tkinter import messagebox

window = Tk()
window.title("Calculator")
window.geometry("265x273")
screen = Text(window, height=2, width=14, font=("Arial", 24))
screen.grid(columnspan=5)

x = ""
def typing(buffer):
    global x
    x += str(buffer)
    screen.delete(1.0, END)
    screen.insert(1.0, x)
    # print(x)

def calculation():
    try:
        global x 
        x = str(eval(x))
        screen.delete(1.0, END)
        screen.insert(1.0, x)
    except ZeroDivisionError:
        screen.delete(1.0, END)
        screen.insert(1.0, "Error")
    except Exception:
        messagebox.showwarning("Unkown Error", "somthing went wrong!")
        screen.delete(1.0, END)

def clear_field():
    global x
    screen.delete(1.0, END)
    x = ""


btn_1 = Button(window, text="1", width=5, font=("Arail",14), command= lambda: typing(1))
btn_1.grid(row=3,column=0)
btn_2 = Button(window, text="2", width=5, font=("Arail",14), command= lambda: typing(2))
btn_2.grid(row=3,column=1)
btn_3 = Button(window, text="3", width=5, font=("Arail",14), command= lambda: typing(3))
btn_3.grid(row=3,column=2)
btn_4 = Button(window, text="4", width=5, font=("Arail",14), command= lambda: typing(4))
btn_4.grid(row=2,column=0)
btn_5 = Button(window, text="5", width=5, font=("Arail",14), command= lambda: typing(5))
btn_5.grid(row=2,column=1)
btn_6 = Button(window, text="6", width=5, font=("Arail",14), command= lambda: typing(6))
btn_6.grid(row=2, column=2)
btn_7 = Button(window, text="7", width=5, font=("Arail",14), command= lambda: typing(7))
btn_7.grid(row=1,column=0)
btn_8 = Button(window, text="8", width=5, font=("Arail",14), command= lambda: typing(8))
btn_8.grid(row=1,column=1)
btn_9 = Button(window, text="9", width=5, font=("Arail",14), command= lambda: typing(9))
btn_9.grid(row=1, column=2)
btn_0 = Button(window, text="0", width=5, font=("Arail",14), command= lambda: typing(0))
btn_0.grid(row=4, column=1)

btn_plus = Button(window, text="+", width=5, font=("Arail",14), command= lambda: typing("+"))
btn_plus.grid(row=1, column=3)
btn_minus = Button(window, text="-", width=5, font=("Arail",14), command= lambda: typing("-"))
btn_minus.grid(row=2, column=3)
btn_mul = Button(window, text="x", width=5, font=("Arail",14), command= lambda: typing("*"))
btn_mul.grid(row=3, column=3)
btn_div = Button(window, text="/", width=5, font=("Arail",14), command= lambda: typing("/"))
btn_div.grid(row=4, column=3)

btn_open = Button(window, text="(", width=5, font=("Arail",14), command= lambda: typing("("))
btn_open.grid(row=4, column=0)
btn_close = Button(window, text=")", width=5, font=("Arail",14), command= lambda: typing(")"))
btn_close.grid(row=4, column=2)
btn_clc = Button(window, text="clear", width=11, font=("Arail",14), command= clear_field)
btn_clc.grid(row=5, column=0, columnspan=2)
btn_equal = Button(window, text="=", width=11, font=("Arail",14), command= calculation)
btn_equal.grid(row=5, column=2, columnspan=2)

window.mainloop()