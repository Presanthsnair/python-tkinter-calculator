from tkinter import *

window = Tk()
window.geometry("350x450")  # window size
window.configure(bg="white")

display = Entry(window, width=35, bg="black", fg="white", font=90, bd=5)  # input field
display.place(x=15, y=7)


def cal(val):
    value = display.get()
    display.delete(0, END)
    display.insert(0, str(value) + str(val))


def clr():
    display.delete(0, END)


def calculate(v):
    r = eval(display.get())
    display.delete(0, END)
    display.insert(0, r)


clr_button = Button(window, text="CLR", command=lambda: clr(), width=10, height=3, bg="white",
                    activebackground="DODGERBLUE", bd=3, activeforeground="white")
button1 = Button(window, text="7", command=lambda: cal(7), width=7, height=3, bg="white", activebackground="DODGERBLUE",
                 bd=3, activeforeground="white")
button2 = Button(window, text="8", command=lambda: cal(8), width=7, height=3, bg="white", activebackground="DODGERBLUE",
                 bd=3, activeforeground="white")
button3 = Button(window, text="9", command=lambda: cal(9), width=7, height=3, bg="white", activebackground="DODGERBLUE",
                 bd=3, activeforeground="white")
button4 = Button(window, text="X", command=lambda: cal("*"), width=7, height=3, bg="white",
                 activebackground="DODGERBLUE", bd=3, activeforeground="white")
button5 = Button(window, text="4", command=lambda: cal(4), width=7, height=3, bg="white", activebackground="DODGERBLUE",
                 bd=3, activeforeground="white")
button6 = Button(window, text="5", command=lambda: cal(5), width=7, height=3, bg="white", activebackground="DODGERBLUE",
                 bd=3, activeforeground="white")
button7 = Button(window, text="6", command=lambda: cal(6), width=7, height=3, bg="white", activebackground="DODGERBLUE",
                 bd=3, activeforeground="white")
button8 = Button(window, text="-", command=lambda: cal("-"), width=7, height=3, bg="white",
                 activebackground="DODGERBLUE", bd=3, activeforeground="white")
button9 = Button(window, text="1", command=lambda: cal(1), width=7, height=3, bg="white", activebackground="DODGERBLUE",
                 bd=3, activeforeground="white")
button10 = Button(window, text="2", command=lambda: cal(2), width=7, height=3, bg="white",
                  activebackground="DODGERBLUE", bd=3, activeforeground="white")
button11 = Button(window, text="3", command=lambda: cal(3), width=7, height=3, bg="white",
                  activebackground="DODGERBLUE", bd=3, activeforeground="white")
button12 = Button(window, text="+", command=lambda: cal("+"), width=7, height=3, bg="white",
                  activebackground="DODGERBLUE", bd=3, activeforeground="white")
button13 = Button(window, text="/", command=lambda: cal("/"), width=7, height=3, bg="white",
                  activebackground="DODGERBLUE", bd=3, activeforeground="white")
button14 = Button(window, text="0", command=lambda: cal(0), width=7, height=3, bg="white",
                  activebackground="DODGERBLUE", bd=3, activeforeground="white")
button15 = Button(window, text=".", command=lambda: cal("."), width=7, height=3, bg="white",
                  activebackground="DODGERBLUE", bd=3, activeforeground="white")
button16 = Button(window, text="=", command=lambda: calculate("="), width=7, height=3, bg="white",
                  activebackground="DODGERBLUE", bd=3, activeforeground="white")

clr_button.place(x=15, y=40)
button1.place(x=15, y=110)
button2.place(x=95, y=110)
button3.place(x=170, y=110)
button4.place(x=245, y=110)

button5.place(x=15, y=190)
button6.place(x=95, y=190)
button7.place(x=170, y=190)
button8.place(x=245, y=190)

button9.place(x=15, y=270)
button10.place(x=95, y=270)
button11.place(x=170, y=270)
button12.place(x=245, y=270)

button13.place(x=15, y=350)
button14.place(x=95, y=350)
button15.place(x=170, y=350)
button16.place(x=245, y=350)

display.config(cursor="none")

window.mainloop()
