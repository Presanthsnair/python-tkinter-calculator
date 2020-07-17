from tkinter import *
from tkinter import Button

window = Tk()
window.geometry("500x500")  # window size

display = Entry(window,width=80,justify=RIGHT)  # input field
display.grid(row=0,column=0)


button1=Button(window, text="7",command="7",width=10,height=5)
button2=Button(window, text="8",command="8",width=10,height=5)
button3=Button(window, text="9",command="9",width=10,height=5)
button4=Button(window, text="X",command="X",width=10,height=5)
button5=Button(window, text="4",command="4",width=10,height=5)
button6=Button(window, text="5",command="5",width=10,height=5)
button7=Button(window, text="6",command="6",width=10,height=5)
button8=Button(window, text="-",command="-",width=10,height=5)
button9=Button(window, text="1",command="1",width=10,height=5)
button10=Button(window, text="2",command="2",width=10,height=5)
button11=Button(window, text="3",command="3",width=10,height=5)
button12=Button(window, text="+",command="+",width=10,height=5)
button13=Button(window, text="/",command="/",width=10,height=5)
button14=Button(window, text="0",command="0",width=10,height=5)
button15=Button(window, text=".",command=".",width=10,height=5)
button16=Button(window, text="=",command="=",width=10,height=5)

button1.grid(row=1,column=2)
button2.grid(row=1,column=4)
button3.grid(row=1,column=6)
button4.grid(row=1,column=8)

button5.grid(row=3,column=2)
button6.grid(row=3,column=4)
button7.grid(row=3,column=6)
button8.grid(row=3,column=8)

button9.grid(row=4,column=2)
button10.grid(row=4,column=4)
button11.grid(row=4,column=6)
button12.grid(row=4,column=8)

button13.grid(row=6,column=2)
button14.grid(row=6,column=4)
button15.grid(row=6,column=6)
button16.grid(row=6,column=8)




window.mainloop()
