from tkinter import *


gw = Tk()
gw.title('Элемент ниже')
gw.geometry('800x600+300+200')

lbl = Label(gw, text="Все элементы расположены ниже,"
                     "это просто Надпись(Label)",
            width=50, height=4,
            bg='black', fg='red')
lbl.pack(side='top', fill='x')

btn1 = Button(gw, text="Все элементы расположены ниже, "
                       "это просто Кнопка(Button)",
              width=50, height=4,
              bg='white', fg='blue')
btn1.pack(side='top')

listbox1 = Listbox(gw, height=6, width=30, selectmode=EXTENDED)
listbox2 = Listbox(gw, height=6, width=30, selectmode=SINGLE)
list1 = ["Можете выбрать", "Сколько угодно", "Элементов", "Но", "Ничего", "Не произойдёт"]
list2 = ["А тут", "И вовсе", "Можно выбрать", "Только один", "Ведь", "selectmode=SINGLE"]
for i in list1:
        listbox1.insert(END, i)
for i in list2:
        listbox2.insert(END, i)
listbox1.place(relx=0.5, x=-240, rely=0.23)
listbox2.place(relx=0.5, x=40, rely=0.23)

var1 = IntVar()
check1 = Checkbutton(gw, text='Вы узнали все элементы выше?',
                     variable=var1, onvalue=1, offvalue=0)
check1.place(relx=0.5, x=-40, rely=0.42)

var = IntVar()
rbutton1 = Radiobutton(gw, text='Верх', variable=var, value=1)
rbutton2 = Radiobutton(gw, text='Низ', variable=var, value=2)
rbutton3 = Radiobutton(gw, text='Нет', variable=var, value=3)
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()

lbl = Label(gw, text="Опишите свои эмоции от ознакомления "
                     "со всеми элементами и оцените свои знания с помощью шкалы",
            width=50, height=4,
            bg='black', fg='red')
lbl.pack(side='bottom', fill='x')

text1 = Text(gw, height=7, width=7, font='Arial 14', wrap=WORD)
text1.pack(side='bottom', fill='x')


def getV(gw):
    a = scale1.get()
    print("Значение", a)


scale1 = Scale(gw, orient=HORIZONTAL, length=300, from_=50, to=100, tickinterval=5,
               resolution=5)
button1 = Button(gw, text="Оценить!")
scale1.pack(side='bottom', fill='x')
button1.place(relx=0.45, rely=0.48)
button1.bind("<Button-1>", getV)


gw.mainloop()
