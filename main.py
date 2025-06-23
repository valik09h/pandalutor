from tkinter import *
window = Tk()
window.title('пандалятор')
window.geometry('350x400+200+200')
def input(symbol):
    entry.insert(END, symbol)
def enter(symbol):
    entry.insert(END, symbol)
def clear():
    entry.delete(0, END)
def enter():
    text = entry.get()
    result = 0
    if '+' in text:
        split = text.split('+')
        first = float(split[0])
        second = float(split[1])
        result = first + second
        print(result)
    if '-' in text:
        split = text.split('-')
        first = float(split[0])
        second = float(split[1])
        result = first - second
        print(result)
    if '*' in text:
        split = text.split('*')
        first = float(split[0])
        second = float(split[1])
        result = first * second
        
        print(result)
    if '/' in text:
        split = text.split('/')
        first = float(split[0])
        second = float(split[1])
        result = first / second
    clear()
    entry.insert(0, result)
entry = Entry(window, width=10, font = ("" , 20))
entry.place(x=100, y=126, width=170, height=22)
btn1 = Button(window,bg='black', fg='white', text='1', command=lambda: input('1'))
btn1.place(x=100, y=150, width=50, height=50)
btn2 = Button(window,bg='black', fg='white', text='2', command=lambda: input('2'))
btn2.place(x=150, y=150, width=50, height=50)
btn3 = Button(window,bg='black', fg='white', text='3', command=lambda: input('3'))
btn3.place(x=200, y=150, width=50, height=50)
btn4 = Button(window,bg='black', fg='white', text='4', command=lambda: input('4'))
btn4.place(x=100, y=200, width=50, height=50)
btn5 = Button(window,bg='black', fg='white', text='5', command=lambda: input('5'))
btn5.place(x=150, y=200, width=50, height=50)
btn6 = Button(window,bg='black', fg='white', text='6', command=lambda: input('6'))
btn6.place(x=200, y=200, width=50, height=50)
btn7 = Button(window,bg='black', fg='white', text='7', command=lambda: input('7'))
btn7.place(x=100, y=250, width=50, height=50)
btn8 = Button(window,bg='black', fg='white', text='8', command=lambda: input('8'))
btn8.place(x=150, y=250, width=50, height=50)
btn9 = Button(window,bg='black', fg='white', text='9', command=lambda: input('9'))
btn9.place(x=200, y=250, width=50, height=50)
btn0 = Button(window,bg='black', fg='white', text='0', command=lambda: input('0'))
btn0.place(x=150, y=300, width=50, height=50)
btn_plus = Button(window,bg='black', fg='white', text='+', command=lambda: input('+'))
btn_plus.place(x=250, y=150, width=50, height=50)
btn_minus = Button(window,bg='black', fg='white', text='-', command=lambda: input('-'))
btn_minus.place(x=250, y=200, width=50, height=50)
btn_multiply = Button(window,bg='black', fg='white', text='*', command=lambda: input('*'))
btn_multiply.place(x=250, y=250, width=50, height=50)
btn_enter = Button(window,bg='black', fg='white', text='enter',command=lambda: enter())
btn_enter.place(x=250, y=300, width=50, height=50)
btn_divide = Button(window,bg='black', fg='white', text='/', command=lambda: input('/'))
btn_divide.place(x=200, y=300, width=50, height=50)
btn_point= Button(window,bg='black', fg='white', text='.', command=lambda: input('.'))
btn_point.place(x=100, y=300, width=50, height=50)
bnt_clear = Button(window,bg='black', fg='white', text='clear', command=lambda: clear())
bnt_clear.place(x=250, y=126, width=50, height=25)


window.mainloop()