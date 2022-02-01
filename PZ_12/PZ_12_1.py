# вариант 17
# В соответствии с номером варианта перейти по ссылке на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1).

from tkinter import *       # импортирование tkinter
from tkinter import ttk
root = Tk()
root.title("Testform")
root.geometry('1324x782')
fr1 = Frame(root, bg='gray90', bd=100, height='50', width='1324', highlightthickness='2', highlightbackground='gray60')
fr1.place(relx=.0, rely=.0)
fr2 = Frame(root, bg='white', bd=100, height='702', width='1324', highlightthickness='2', highlightbackground='gray60')
fr2.place(x=0, y=45)        # frame - рамка
fr3 = Frame(root, bg='gray90', bd=100, height='50', width='1324', highlightthickness='2', highlightbackground='gray60')
fr3.place(x=0, y=732)
combo = ttk.Combobox(root, font=('arial', 18), width='14',      # combobox - выпадающий список для выбора
                     values=[
                             "Please select...",
                             "USA",
                             "Russia"])
combo.place(relx=.295, rely=.43)
combo.current(0)
label1 = Label(text='Testform', bg='gray90', fg='black', font=('Arial Black', 19), justify=LEFT)
label1.place(relx=.02, rely=.002)       # place - упаковщик, размещающий виджет в фикс. месте и фикс. размером
label2 = Label(text="Name", bg='white', fg='black', font=('arial', 18), justify=LEFT)
label2.place(relx=.02, rely=.10)
label3 = Label(text='Password', bg='white', fg='black', font=('arial', 18), justify=LEFT)
label3.place(relx=.02, rely=.19)
label4 = Label(text='Gender', bg='white', fg='black', font=('arial', 18), justify=LEFT)
label4.place(relx=.02, rely=.28)
label5 = Label(text='Continent', bg='white', fg='black', font=('arial', 18), justify=LEFT)  # label - неизменяемый текст
label5.place(relx=.02, rely=.43)
label6 = Label(text='Meals', bg='white', fg='black', font=('arial', 18), justify=LEFT)
label6.place(relx=.02, rely=.515)
label7 = Label(text='Remark', bg='white', fg='black', font=('arial', 18), justify=LEFT)
label7.place(relx=.02, rely=.73)
entry1 = Entry(borderwidth='2', width=17, font=('arial', 18))      # entry - поле для ввода одной строки текста
entry1.place(relx=.295, rely=.10)
entry2 = Entry(borderwidth='2', width=17, font=('arial', 18))
entry2.place(relx=.295, rely=.19)
text1 = Text(height=5, width=46, font=('arial', 18), wrap=WORD, borderwidth='2')    # text - поле для ввода текста
text1.place(relx=.295, rely=.73)
var = IntVar()
rbutton1 = Radiobutton(text='Male', variable=var, value=1, bg='white', fg='black', font=('arial', 18))
rbutton1.place(relx=.295, rely=.28)
rbutton2 = Radiobutton(text='Female', variable=var, value=2, bg='white', fg='black', font=('arial', 18))
rbutton2.place(relx=.295, rely=.35)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
check1 = Checkbutton(text='breakfast', variable=var1, onvalue=1, offvalue=0, bg='white', fg='black', font=('arial', 18))
check2 = Checkbutton(text='lunch', variable=var2, onvalue=1, offvalue=0, bg='white', fg='black', font=('arial', 18))
check3 = Checkbutton(text='dinner', variable=var3, onvalue=1, offvalue=0, bg='white', fg='black', font=('arial', 18))
check1.place(relx=.295, rely=.515)
check2.place(relx=.295, rely=.585)
check3.place(relx=.295, rely=.655)
button1 = Button(root, text='Send', width=5, height=1, bg='gray90', fg='black', font=('arial', 18))
button1.place(x=1100, y=734)
button2 = Button(root, text='Cancel', width=6, height=1, bg='gray90', fg='black', font=('arial', 18), command=quit)
button2.place(x=1200, y=734)      # button - кнопка, command=quit - закрывает программу
root.mainloop()
