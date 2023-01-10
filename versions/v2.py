# trying to find out how to use ANS in my calculator

from tkinter import *

window = Tk()
window.title('Calculator')
window.configure(bg='WHITE')
# window.geometry('400x300')
window.resizable(False, False) 

newCalculation = False
calculation = ''
answer = ''

input_field = Entry(window, width = 30)

def on_click(string):
    global newCalculation, calculation, answer
    # print(newCalculation)
    print(input_field.get())

    if newCalculation == True and '(' not in input_field.get() and ')' not in input_field.get() and string not in ['+', '-', '/', '*']:
        newCalculation = False
        input_field.delete(0, END)
    if string in ['+', '-', '/', '*']:
        calculation += string
        input_field.delete(0, END)
    elif string == 'AC':
        calculation = ''
        input_field.delete(0, END)
    elif string == 'DEL':
        newValue = input_field.get()[:-1]
        if input_field.get()[-5:] == 'Error':
            newValue = input_field.get()[:-5]
        elif input_field.get()[-3:] == 'ANS':
            newValue = input_field.get()[:-3]
        input_field.delete(0, END)
        input_field.insert(0, newValue)
    elif string == '=':
        calculation = answer.join(calculation.split('ANS'))
        try:
            total = eval(calculation)
        except:
            total = 'Error'
        if len(str(total).split('.')) == 2 and str(total).split('.')[1] == '0':
            total = int(total)
        input_field.delete(0, END)
        input_field.insert(0, total)
        answer = str(total)
        newCalculation = True
    else:
        input_field.insert(len(input_field.get()), string)
        if string == '^':
            string = '**'
        calculation += string

num_0 = Button(window, text = '0', bg = 'GREY', padx = 25, pady = 5, command = lambda: on_click('0'))
num_1 = Button(window, text = '1', bg = 'GREY', padx = 25, pady = 5, command = lambda: on_click('1'))
num_2 = Button(window, text = '2', bg = 'GREY', padx = 25, pady = 5, command = lambda: on_click('2'))
num_3 = Button(window, text = '3', bg = 'GREY', padx = 25, pady = 5, command = lambda: on_click('3'))
num_4 = Button(window, text = '4', bg = 'GREY', padx = 25, pady = 5, command = lambda: on_click('4'))
num_5 = Button(window, text = '5', bg = 'GREY', padx = 25, pady = 5, command = lambda: on_click('5'))
num_6 = Button(window, text = '6', bg = 'GREY', padx = 25, pady = 5, command = lambda: on_click('6'))
num_7 = Button(window, text = '7', bg = 'GREY', padx = 25, pady = 5, command = lambda: on_click('7'))
num_8 = Button(window, text = '8', bg = 'GREY', padx = 25, pady = 5, command = lambda: on_click('8'))
num_9 = Button(window, text = '9', bg = 'GREY', padx = 25, pady = 5, command = lambda: on_click('9'))
char_left_bracket = Button(window, text = '(', bg = 'BLUE', padx = 25, pady = 5, command = lambda: on_click('('))
char_right_bracket = Button(window, text = ')', bg = 'BLUE', padx = 25, pady = 5, command = lambda: on_click(')'))
char_power = Button(window, text = '^', bg = 'BLUE', padx = 25, pady = 5, command = lambda: on_click('^'))
char_percentage = Button(window, text = '%', bg = 'BLUE', padx = 25, pady = 5, command = lambda: on_click('%'))
char_divide = Button(window, text = '/', bg = 'BLUE', padx = 25, pady = 5, command = lambda: on_click('/'))
char_multiply = Button(window, text = 'x', bg = 'BLUE', padx = 25, pady = 5, command = lambda: on_click('*'))
char_subtract = Button(window, text = '-', bg = 'BLUE', padx = 25, pady = 5, command = lambda: on_click('-'))
char_add = Button(window, text = '+', bg = 'BLUE', padx = 25, pady = 5, command = lambda: on_click('+'))
char_dot = Button(window, text = '.', bg = 'BLUE', padx = 25, pady = 5, command = lambda: on_click('.'))
char_equals = Button(window, text = ' = ', bg = 'GREEN', padx = 25, pady = 5, command = lambda: on_click('='))
ac = Button(window, text = 'AC', bg = 'RED', padx = 25, pady = 5, command = lambda: on_click('AC'))
backspace = Button(window, text = 'DEL', bg = 'RED', padx = 25, pady = 5, command = lambda: on_click('DEL'))
ans = Button(window, text = 'ANS', bg = 'RED', padx = 25, pady = 5, command = lambda: on_click('ANS'))
blank = Button(window, bg = 'GREY', padx = 25, pady = 5)

input_field.grid(row = 0, column = 1, columnspan = 3, sticky='NWSE')
char_left_bracket.grid(row = 1, column = 0, sticky='NWSE')
char_right_bracket.grid(row = 1, column = 1, sticky='NWSE')
char_power.grid(row = 1, column = 2, sticky='NWSE')
char_percentage.grid(row = 1, column = 3, sticky='NWSE')
ac.grid(row = 1, column = 4, sticky='NWSE')
num_1.grid(row = 2, column = 0, sticky='NWSE')
num_2.grid(row = 2, column = 1, sticky='NWSE')
num_3.grid(row = 2, column = 2, sticky='NWSE')
char_divide.grid(row = 2, column = 3, sticky='NWSE')
num_4.grid(row = 3, column = 0, sticky='NWSE')
num_5.grid(row = 3, column = 1, sticky='NWSE')
num_6.grid(row = 3, column = 2, sticky='NWSE')
char_multiply.grid(row = 3, column = 3, sticky='NWSE')
backspace.grid(row = 3, column = 4, sticky='NWSE')
num_7.grid(row = 4, column = 0, sticky='NWSE')
num_8.grid(row = 4, column = 1, sticky='NWSE')
num_9.grid(row = 4, column = 2, sticky='NWSE')
char_subtract.grid(row = 4, column = 3, sticky='NWSE')
ans.grid(row = 4, column = 4, sticky='NWSE')
char_dot.grid(row = 5, column = 0, sticky='NWSE')
num_0.grid(row = 5, column = 1, sticky='NWSE')
char_equals.grid(row = 5, column = 2, sticky='NWSE')
char_add.grid(row = 5, column = 3, sticky='NWSE')
blank.grid(row = 5, column = 4, sticky='NWSE')

window.mainloop()