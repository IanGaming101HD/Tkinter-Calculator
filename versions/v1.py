from tkinter import *

window = Tk()

e = Entry(window)
e.grid(row=0,column=0, columnspan=3)

button = Button(window, text='1', bg='grey', padx=25, pady=25)
button2 = Button(window, text='2', bg='grey', padx=25, pady=25)
button3 = Button(window, text='3', bg='grey', padx=25, pady=25)
button4 = Button(window, text='4', bg='grey', padx=25, pady=25)
button5 = Button(window, text='5', bg='grey', padx=25, pady=25)
button6 = Button(window, text='6', bg='grey', padx=25, pady=25)
button7 = Button(window, text='7', bg='grey', padx=25, pady=25)
button8 = Button(window, text='8', bg='grey', padx=25, pady=25)
button9 = Button(window, text='9', bg='grey', padx=25, pady=25)
button10 = Button(window, text='0', bg='grey', padx=25, pady=25)

button.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button10.grid(row=4,column=1)

# screen = Entry(root, width=30, borderwidth=5)
# screen.grid(row=0,column=0, columnspan=3, padx=10,pady=10)


window.mainloop()

# def numberPress(number):
    
#     current = screen.get()
#     screen.delete(0,END)
#     screen.insert(0,str(current) + str(number))
