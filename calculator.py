from tkinter import *

window = Tk()
window.geometry("500x500")  # window size
window.configure(bg="red")

display = Entry(window, width=80, bg="black", fg="white")  # input field
display.grid(row=0, column=0)

def cal(val):
    display.insert(0,val)


button1 = Button(window, text="7", command=lambda :cal(7), width=10, height=5, bg="white", activebackground="light blue")
button2 = Button(window, text="8", command=lambda :cal(8), width=10, height=5, bg="white", activebackground="light blue")
button3 = Button(window, text="9", command=lambda :cal(9), width=10, height=5, bg="white", activebackground="light blue")
button4 = Button(window, text="X", command=lambda :cal(X), width=10, height=5, bg="white", activebackground="light blue")
button5 = Button(window, text="4", command=lambda :cal(4), width=10, height=5, bg="white", activebackground="light blue")
button6 = Button(window, text="5", command=lambda :cal(5), width=10, height=5, bg="white", activebackground="light blue")
button7 = Button(window, text="6", command=lambda :cal(6), width=10, height=5, bg="white", activebackground="light blue")
button8 = Button(window, text="-", command=lambda :cal("-"), width=10, height=5, bg="white", activebackground="light blue")
button9 = Button(window, text="1", command=lambda :cal(1), width=10, height=5, bg="white", activebackground="light blue")
button10 = Button(window, text="2", command=lambda :cal(2), width=10, height=5, bg="white", activebackground="light blue")
button11 = Button(window, text="3", command=lambda :cal(3), width=10, height=5, bg="white", activebackground="light blue")
button12 = Button(window, text="+", command=lambda :cal("+"), width=10, height=5, bg="white", activebackground="light blue")
button13 = Button(window, text="/", command=lambda :cal("/"), width=10, height=5, bg="white", activebackground="light blue")
button14 = Button(window, text="0", command=lambda :cal(0), width=10, height=5, bg="white", activebackground="light blue")
button15 = Button(window, text=".", command=lambda :cal("."), width=10, height=5, bg="white", activebackground="light blue")
button16 = Button(window, text="=", command=lambda :cal("="), width=10, height=5, bg="white", activebackground="light blue")

button1.grid(row=1, column=2)
button2.grid(row=1, column=4)
button3.grid(row=1, column=6)
button4.grid(row=1, column=8)

button5.grid(row=3, column=2)
button6.grid(row=3, column=4)
button7.grid(row=3, column=6)
button8.grid(row=3, column=8)

button9.grid(row=4, column=2)
button10.grid(row=4, column=4)
button11.grid(row=4, column=6)
button12.grid(row=4, column=8)

button13.grid(row=6, column=2)
button14.grid(row=6, column=4)
button15.grid(row=6, column=6)
button16.grid(row=6, column=8)

window.mainloop()
