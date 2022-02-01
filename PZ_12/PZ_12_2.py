# вариант 17
# Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 3 – 8.
# PZ_4_2

from tkinter import *       # импортирование tkinter
root = Tk()
root.title("PZ_4_2")
root.geometry('520x300')        # root.geometry() - устанавливает размер окна
fr1 = Frame(root, bg='gray60', bd=100, height='50', width='520', highlightthickness='2', highlightbackground='black')
fr1.place(relx=.0, rely=.0)
fr2 = Frame(root, bg='gray94', bd=100, height='250', width='520', highlightthickness='2', highlightbackground='black')
fr2.place(relx=.0, y=50)    # highlightthickness - ширина краёв рамки, highlightbackground - цвет краёв рамки
label0 = Label(text='Длина незанятой части отрезка a', bg='gray60', fg='white', font=('Arial', 16), justify=CENTER)
label0.place(x=90, rely=.02)
label1 = Label(text='Введите положительное число a:', fg='black', font=('Arial', 16), justify=LEFT)
label1.place(relx=.02, rely=.25)    # font=('Arial', 16) - шрифт и его размер, justify - выравнивание текста
label2 = Label(text='Введите положительное число b:', fg='black', font=('Arial', 16), justify=LEFT)
label2.place(relx=.02, rely=.45)
label3 = Label(text='', fg='black', font=('Arial', 16), justify=LEFT)
label3.place(relx=.1, rely=.75)
entry1 = Entry(borderwidth='2', width=5, font=('arial', 18))
entry1.place(x=370, rely=.25)
entry2 = Entry(borderwidth='2', width=5, font=('arial', 18))
entry2.place(x=370, rely=.45)


def b1_clicked():       # def - функция
    try:
        a = float(entry1.get())     # get - возврат входного текста из текстового поля
        b = float(entry2.get())
        c = 0
        if 0 < a > b > 0:
            while c <= a:
                c += b
            c = c - b
            d = a - c
            label3.config(fg='black', text='Результат = {0}'.format(round(d, 1)))
    except ValueError:      # .config - используется для простого изменения текста в Label
        label3.config(text='ОШИБКА!', fg='red')     # fg - цвет текста


b1 = Button(root, text='Вычислить', width=10, height=1, bg='gray60', fg='white', font=('arial', 18), command=b1_clicked)
b1.place(x=330, rely=.72)
root.mainloop()
