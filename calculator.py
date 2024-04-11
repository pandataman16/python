from tkinter import *

exp = ""

def press(num):
    global exp
    exp += str(num)
    equation.set(exp)
    output_label.config(text=exp)
def equalpress():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = total
        output_label.config(text=total)
        print(total)

    except:
        equation.set("Error")
        exp = ""

def clear():
    global exp
    exp = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="white")
    gui.title("Simple Calculator")
    gui.geometry("360x250")

    equation = StringVar()
    exp_field = Entry(gui, textvariable=equation)
    exp_field.grid(columnspan=4,ipadx=70)
    output_label = Label(gui,text="",fg="black",bg="white",font=("Arial",12))
    output_label.grid(row=5,column=0,columnspan=4)
    
    button1 = Button(gui, text='1', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
    button2 = Button(gui, text='2', fg='black', bg='red', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
    button3 = Button(gui, text='3', fg='black', bg='red', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
    button4 = Button(gui, text='4', fg='black', bg='red', command=lambda: press(4), height=1, width=7)
    button4.grid(row=1, column=0)
    button5 = Button(gui, text='5', fg='black', bg='red', command=lambda: press(5), height=1, width=7)
    button5.grid(row=1, column=1)
    button6 = Button(gui, text='6', fg='black', bg='red', command=lambda: press(6), height=1, width=7)
    button6.grid(row=1, column=2)
    button7 = Button(gui, text='7', fg='black', bg='red', command=lambda: press(7), height=1, width=7)
    button7.grid(row=0, column=0)
    button8 = Button(gui, text='8', fg='black', bg='red', command=lambda: press(8), height=1, width=7)
    button8.grid(row=0, column=1)
    button9 = Button(gui, text='9', fg='black', bg='red', command=lambda: press(9), height=1, width=7)
    button9.grid(row=0, column=2)
    button0 = Button(gui, text='0', fg='black', bg='red', command=lambda: press(0), height=1, width=7)
    button0.grid(row=3, column=1)

    plus = Button(gui, text='+', fg='black', bg='red', command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
    minus = Button(gui, text='-', fg='black', bg='red', command=lambda: press("-"), height=1, width=7)
    minus.grid(row=1, column=3)
    multi = Button(gui, text='*', fg='black', bg='red', command=lambda: press("*"), height=1, width=7)
    multi.grid(row=0, column=3)
    divi = Button(gui, text='/', fg='black', bg='red', command=lambda: press("/"), height=1, width=7)
    divi.grid(row=3, column=3)
    deci = Button(gui, text='c', fg='black', bg='red', command=lambda: clear(), height=1, width=7)
    deci.grid(row=3, column=2)
    equal = Button(gui, text='=', fg='black', bg='red', command=lambda: equalpress(), height=1, width=7)
    equal.grid(row=3, column=0)


    gui.mainloop()