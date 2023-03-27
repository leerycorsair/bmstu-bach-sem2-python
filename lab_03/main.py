#Программа для исследования метода сортировки вставками с барьером
#Леонов Владислав ИУ7-26Б


from tkinter import *
from tkinter.font import Font
from tkinter import messagebox as mb
from tkinter import ttk
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from numpy import*
import matplotlib.pyplot as plt
from random import *


def prog_info():
    info = '''Данная программа предназначена для исследования метода сортировки \
вставкаими с барьером.

Исследование предполагает работу в 3 режимах:
1-ый (СММ):
    проверка корректности сортировки на массивах малой\n    размерности до 10 элементов;
2-ой (СМРП):
    сравнение времени сортировки трех различных\n    размерностей (для каждой размерности
    исследуем случайный список, отсортированный в\n    прямом и обратном порядке массив);
3-ий (РВХ):
    построение графика зависимости времени работы для\n    10 равномерно распределенных
    на отрезке размерностей массивов;

Версия: 0.1.0
    '''
    messagebox.showinfo(title = 'О программе', message = info)
    
def cr_info():
    info ='''Создателем данной программы является\nстудент МГТУ им. Н.Э. Баумана группы ИУ7-26Б,\n\
Леонов Владислав Вячеславович'''
    messagebox.showinfo(title = 'О создателе', message = info)


def ins_sort(a:list):
    a = [0] + a
    for i in range (2,len(a)):
        j = i-1
        a[0] = a[i]
        while a[j]>a[0]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = a[0]
    return a[1:]
  

def sort_e():
    global fm_e, fm_source
    fm_source = fm_e.get()
    if fm_source == '' or len(fm_source.split()) <= 1:
        messagebox.showerror(title = 'Ошибка', message = 'Вы не ввели массив.')
        fm_source = ''
    else:
        try:
            res = [float(fm_source.split()[i]) for i in range(len(fm_source.split()))]
            res = ins_sort(res)
            fm_e.delete(0, 'end')
            for i in range(len(res)):
                fm_e.insert('end','{:.6g}'.format(res[i])+' ')
        except:
            messagebox.showerror(title = 'Ошибка', message = 'Некорректный ввод.')
            fm_source = ''

def get_fm_source():
    global fm_source, fm_e
    if fm_source != '':
        fm_e.delete(0,'end')
        fm_e.insert(0, fm_source)
      
def get_time(a):
    t0 = datetime.now()
    a = ins_sort(a)
    t1 = datetime.now()
    return (t1-t0).total_seconds()
    
    
def table_creation():
    global table, fs, ss, ts
    table.delete(*table.get_children())
    try:
        s = []
        s.append(int(fs.get()))
        s.append(int(ss.get()))
        s.append(int(ts.get()))
        t = []
        for i in range(3):
            a = linspace(0,1000,num = int(s[i]))
            t.append(get_time(a))
        table.insert('', 'end', text = 'Упорядоченный', values = t)
        t = []
        for i in range(3):
            a = (linspace(0,1000,num = int(s[i])))
            shuffle(a)
            t.append(get_time(a))
        table.insert('', 'end', text = 'Случайный', values = t)
        t = []
        for i in range(3):
            a = (linspace(1000,0,num = int(s[i])))
            t.append(get_time(a))
        table.insert('', 'end', text = 'Упорядоченный в обратном порядке', values = t)
    except:
        messagebox.showerror(title = 'Ошибка', message = 'Некорректный ввод.')

        
        
def graph_creation():
    r_b = 4000
    l_b = 1000
    l_b0 = l_b
    global fig, canvas
    fig.clf()
    step = (r_b - l_b) // 10 
    x_axis = []
    y_axis = []
    while l_b <= r_b:
        
        x_axis.append(l_b)
        a = linspace(0,1000, num = l_b) 
        shuffle(a)
        y_axis.append(get_time(a))
        
        if l_b + step < r_b:
            l_b += step
        elif l_b == r_b:
            l_b += step
        else:
            l_b = r_b
    tmp = fig.add_subplot(111)
    fig.add_subplot(111).plot(x_axis,y_axis, 'c')
    fig.add_subplot(111).scatter(x_axis,y_axis, color = 'r', s = 10, zorder = 10)
    tmp.set_ylabel('Время (c)')
    tmp.set_xticks([i for i in range(l_b0, r_b+1,step)])
    tmp.grid(True)
    tmp.set_xlabel('Кол-во элементов в массиве')
    canvas.draw()




win = Tk()
win.title('Исследование метода сортировки вставками с барьером')
win.configure(background = '#3caa3c')
win.geometry('1500x580+10+10')
fm_source = ''

lf = Frame(win,background = '#3caa3c')
lf.grid(row = 0, column = 0)
rf = Frame(win,background = '#3caa3c')
rf.grid(row = 0, column = 1)




#СММ
fm = LabelFrame(lf, text = 'Сортировка малого массива', font = ('Times New Roman Bold',14),\
padx = 10, pady = 30,background = '#3caa3c',fg = '#ffffff')
fm_e = Entry(fm, width = 60, font = ('Times New Roman Bold',14), background = '#00a550', fg = '#ffffff')
fm_e.grid(row = 0, column = 0, pady = 5)
fm.grid(row = 0, column = 0, padx = 10, pady = 10)
fm_but_fr = Frame(fm, padx = 10, pady = 10,background = '#3caa3c')
fm_sort_but = Button (fm_but_fr, text = 'Отсортировать',font = ('Times New Roman Bold',14),\
width = 30, command = lambda: sort_e(), background = '#00a550', fg = '#ffffff')
fm_sort_but.grid (row = 0, column = 0)
fm_source_but = Button(fm_but_fr, text = 'Исходный массив',font = ('Times New Roman Bold',14),\
width = 30, command = lambda: get_fm_source(),background = '#00a550', fg = '#ffffff')
fm_source_but.grid (row = 0, column = 1)
fm_but_fr.grid (row = 1, column = 0)




#СМРП
sm = LabelFrame(lf, text = 'Сортировка массивов разного порядка', \
font = ('Times New Roman Bold',14), padx = 10, pady = 20,background = '#3caa3c',fg = '#ffffff' )
ent_fr = LabelFrame(sm,text = 'Размерности', font = ('Times New Roman Bold',14), padx = 10, pady = 10,\
background = '#3caa3c',fg = '#ffffff')
fs = Entry(ent_fr, font = ('Times New Roman Bold',14), width = 15,background = '#00a550', fg = '#ffffff')
fs.insert(0, '1000')
fs.grid(row = 0, column = 0, padx = 6)
ss = Entry(ent_fr, font = ('Times New Roman Bold',14), width = 15,background = '#00a550', fg = '#ffffff')
ss.grid(row = 0, column = 1, padx = 6)
ss.insert(0, '2000')
ts = Entry(ent_fr, font = ('Times New Roman Bold',14), width = 15,background = '#00a550', fg = '#ffffff')
ts.grid(row = 0, column = 2, padx = 6)
ts.insert(0, '3000')
sm_but = Button(ent_fr, text = 'Рассчитать',font = ('Times New Roman Bold',14),\
command = lambda: table_creation(),background = '#00a550', fg = '#ffffff')
sm_but.grid(row = 0, column = 3, pady = 10)
ent_fr.grid(row = 0)

table_frame = LabelFrame(sm, text = 'Таблица времени сортировки',\
font = ('Times New Roman Bold',14), padx = 10, pady = 20,background = '#3caa3c',fg = '#ffffff')
style = ttk.Style()
style.configure("Treeview.Heading", font = ('Times New Roman Bold',14))
style.configure("Treeview", font = ('Times New Roman Bold',14))
table = ttk.Treeview(table_frame)
table.configure(columns = ['Р1', 'Р2', 'Р3'], height = 3)
table.heading('#0', text = 'Тип массива')
table.heading('Р1', text = 'Р1')
table.heading('Р2', text = 'Р2')              
table.heading('Р3', text = 'Р3')       

table.column('#0', width = 360,anchor= 'center')  
table.column('Р1', width = 105,anchor= 'center')
table.column('Р2', width = 105,anchor= 'center')
table.column('Р3', width = 105,anchor= 'center')  

table_frame.grid(row = 1, column = 0, pady = 7)
table.pack()
sm.grid(row = 1, column = 0, padx = 10, pady = 10)

#РВХ
tm = LabelFrame (rf, text = 'Размерно-временная характеристика',font = ('Times New Roman Bold',14),\
padx = 10, pady = 27,background = '#3caa3c',fg = '#ffffff' )
tm.grid(row = 2, column = 0)
tm_e = Frame(tm,background = '#3caa3c')
tm_but = Button(tm_e, text = 'Построить',font = ('Times New Roman Bold',14),\
command = lambda: graph_creation (), background = '#00a550',fg = '#ffffff')
tm_but.grid(row = 0, column = 0)
tm_e.grid(row = 0, column = 0)

graph_frame = Frame(tm, padx = 10, pady = 10,background = '#3caa3c')
fig = Figure(figsize=(7,4), dpi = 100)
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
graph_frame.grid(row = 1, column = 0)

mainmenu = Menu(win, tearoff = 0)
win.config (menu = mainmenu)

helpmenu = Menu(mainmenu, tearoff = 0)
helpmenu.add_command(label = 'О программе', command = lambda: prog_info())
helpmenu.add_command(label = 'О создателе', command = lambda: cr_info())
mainmenu.add_cascade(label = 'Справка', menu = helpmenu )

win.mainloop()
