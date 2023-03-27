#Программа для уточнения корней методом касательных c интерфейсом tkinter
#и графической иллюстрацией решения

#Леонов Владислав
#ИУ7-26Б

from tkinter import *
from tkinter.font import Font
from tkinter import messagebox as mb
from tkinter import ttk
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from numpy import*
import matplotlib.pyplot as plt

#Вычисление значения функции в точке
def function(x):
    return (x*x-4)

#Вычисление значения производной в точке
def derivative(x):
    derivative_value = 2*x
    return derivative_value

def show_error_info():
    info = '''Коды ошибок:
1 - Производная не существует;
2 - Производная равна нулю;
3 - Корень находится на границе интервала;
4 - Превышено число итераций;
5 - Выход за границы отрезка.'''
    messagebox.showinfo(title = 'Информация об ошибках', message = info)


def ans_init():
    
    time = datetime.now()
    
    answer = Tk()
    answer.title('Программа')
    answer.geometry('750x400+525+20')
    answer.resizable(0,0)
    
    table_frame = LabelFrame(answer, text = 'Таблица корней уравнения, найденных методом Ньютона', padx = 5 ,pady = 5)
    table_frame.grid(row = 0, column = 0, padx = 20, pady = 10)
    
    table = ttk.Treeview(table_frame)
    table.configure(columns = ['Отрезок', 'Корень', 'Значение f(x)', 'Кол-во итераций', \
    'Время работы', 'Код ошибки'])
    
    table.heading('#0', text = '№')
    table.heading('Отрезок', text = 'Отрезок')
    table.heading('Корень', text = 'Корень')              
    table.heading('Значение f(x)', text = 'Значение f(x)')              
    table.heading('Кол-во итераций', text = 'Кол-во итераций') 
    table.heading('Время работы', text = 'Время работы')
    table.heading('Код ошибки', text = 'Код ошибки')             
                                           
    table.column('#0', width = 40,anchor= 'center')  
    table.column('Отрезок', width = 100,anchor= 'center')
    table.column('Корень', width = 70,anchor= 'center')
    table.column('Значение f(x)', width = 80,anchor= 'center')  
    table.column('Кол-во итераций', width = 120,anchor= 'center')
    table.column('Время работы', width = 100,anchor= 'center')
    table.column('Код ошибки', width = 80,anchor= 'center')
    
    max_iterations = 1e5
    
    check = 0
    roots = []
    uroots = []
    
    x_l = input_data[0]
    stop = input_data[1]
    step = input_data[2]
    acc = input_data[3]
    max_iterations = input_data[4]
    counter = 1
    
    while x_l < stop:
        
        x_r = x_l + step
        if x_r > stop: x_r = stop
        
        #Проверка разности знаков на концах рассматриваемого отрезка
        if function(x_l) * function(x_r) < 0:
    
            check = 1
            root = x_l
            prev_point = root + 10 * acc
            num_of_iterations = 0
            error_code = '-'
    
            while abs(root - prev_point) >= acc and\
                  num_of_iterations < max_iterations:
                #Проверка существования производной
                try:
                    derivative(root)
                except:
                    error_code = '1'
                    break
                #Проверка нулевой производной
                if derivative(root) == 0:
                    error_code = '2'
                    break
                #Новое значение приближения при помощи касательной
                prev_point = root
                root = root - function(root)/derivative(root)
                num_of_iterations += 1
                
            if error_code == '2':
                check = 1
                root = x_r
                prev_point = root - 10 * acc
                num_of_iterations = 0
                error_code = '-'
        
                while abs(root - prev_point) >= acc and\
                      num_of_iterations < max_iterations:
                    #Проверка существования производной
                    try:
                        derivative(root)
                    except:
                        error_code = '1'
                        break
                    #Проверка нулевой производной
                    if derivative(root) == 0:
                        error_code = '2'
                        break
                    #Новое значение приближения при помощи касательной
                    prev_point = root
                    root = root - function(root)/derivative(root)
                    num_of_iterations += 1
            
            if num_of_iterations >= max_iterations:
                error_code = '4'
                   
            if root < x_l or root >x_r or error_code != '-':
                l = x_l
                r = x_r
                roooot = (l+r)/2
                while abs(l - r) > acc:
                    if function(roooot)*function(l)<0:
                        r = roooot
                    else:
                        l = roooot
                    roooot = (l+r)/2
                uroots.append(roooot)
                error_code = '5'
                
                
            #Печать информации в зависиости от возникновения ошибки
            if error_code == '-':
                table.insert('','end', text = counter, values = (\
                '[{:^8.3g};{:^9.3g}]'.format(x_l,x_r),'{:<14.5g}'.format(root),\
                '{:<14.4g}'.format(function(root)), num_of_iterations, datetime.now()-time, '-'))
                roots.append(root)
                counter += 1
            else:
                table.insert('','end', text = counter, values = (\
                '[{:^8.3g};{:^9.3g}]'.format(x_l,x_r),'-','-', '-', '-', error_code))
                counter += 1
                
    
        #Если корень попадает на границу отрезка
        elif function(x_l) * function(x_r) == 0:
    
            check = 1
            error_code = '3'
            if function(x_l) == 0:
                root = x_l
            else:
                root = x_r
            if root not in roots:
                table.insert('','end', text = counter, values = (\
                '[{:^8.3g};{:^9.3g}]'.format(x_l,x_r),'{:<14.5g}'.format(root),\
                '{:<14.4g}'.format(function(root)), '-' , datetime.now()-time, error_code))
                roots.append(root)
                counter += 1
        x_l += step
    
    graph_frame = LabelFrame(answer, text = 'График функции на заданном интервале', padx = 5, pady = 5)
    graph_frame.grid(row = 1, column = 0, padx = 20, pady = 10)
    
    fig = Figure(figsize=(7,3), dpi = 100)
    t = arange(input_data[0],input_data[1], 0.01)
    fig.add_subplot(111).plot(t, function(t), 'g', [input_data[0],input_data[1]], [0,0], 'c')
    fig.add_subplot(111).scatter(roots, [0 for i in range(len(roots))], color = 'r', s = 10, zorder = 10)
    fig.add_subplot(111).scatter(uroots, [0 for i in range(len(uroots))], color = 'k', s = 10, zorder = 10)
    
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    toolbar = NavigationToolbar2Tk(canvas, graph_frame)
    
    
    if check == 1:
        
        answer.geometry('750x675+525+20')
        table.pack(side = 'left')
       
        button = Button(table_frame, text = "Error's \ncodes", command = show_error_info)
        button.pack(side = 'right')
        
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
        vsb.pack(side='right', fill='y')
    else: 
        messagebox.showinfo(title = 'Ответ', message = 'Корни на заданном отрезке отсутствуют\n\
Вы можете ознакомится с графической иллюстрацией') 
        
    answer.mainloop()

    
#Проверка исходных данных
def check_input():
    global input_data
    input_data = []
    input_data.append(lb_e.get())
    input_data.append(rb_e.get())
    input_data.append(st_e.get())
    input_data.append(acc_e.get())
    input_data.append(max_iter_e.get())
    for i in range(len(input_data)):
        try : 
            input_data[i] = float(input_data[i])
        except ValueError:
            mb.showerror("Ошибка", "Вы не ввели некорректные числа или заполнили не все поля ввода")
            return False
    if input_data[0]>=input_data[1]:
        mb.showerror("Ошибка", "Правая граница должна быть больше левой")
        return False
    if input_data[2]>=input_data[1]-input_data[0] or input_data[2]<=0:
        mb.showerror("Ошибка", "Некорректный шаг")
        return False
    if input_data[3] < 0:
        mb.showerror("Ошибка", "Точность не может быть меньше нуля")
        return False
    if input_data[4] != int(input_data[4]) or int(input_data[4]) <= 0:
        mb.showerror("Ошибка", "Количество итераций - целое положительное число")
        return False        
    return True            
       

#Уточнение корней 
def calc():
    
    if check_input() == True: ans_init()
        
#Виджеты окна   
win = Tk()
win.geometry('500x250+20+20')
win.title('Вычисление корней уравнения')
win.resizable(0,0)

frame1 = LabelFrame(win, text="Введите данные для вычисления:", padx = 10, labelanchor = 'n',\
font = ('Times New Roman',20))
frame1.pack( padx = 10, expand = 'True')

lb_w = Label(frame1, text = 'Левая граница', font = ('Times New Roman',14), width = 15, anchor = 'e')
lb_w.grid(row = 0, column = 0)
lb_e = Entry(frame1, width = 20, font = ('Times New Roman',14))
lb_e.grid(row = 0, column = 1)

rb_w = Label(frame1, text = 'Правая граница', font = ('Times New Roman',14), width = 15, anchor = 'e')
rb_w.grid(row = 1, column = 0)
rb_e = Entry(frame1, width = 20, font = ('Times New Roman',14))
rb_e.grid(row = 1, column = 1)

st_w = Label(frame1, text = 'Шаг', font = ('Times New Roman',14), width = 15, anchor = 'e')
st_w.grid(row = 2, column = 0)
st_e = Entry(frame1, width = 20, font = ('Times New Roman',14))
st_e.grid(row = 2, column = 1)

acc_w = Label(frame1, text = 'Точность', font = ('Times New Roman',14), width = 15, anchor = 'e')
acc_w.grid(row = 3, column = 0)
acc_e = Entry(frame1, width = 20, font = ('Times New Roman',14))
acc_e.insert(END, '1e-8')
acc_e.grid(row = 3, column = 1)

max_iter = Label(frame1, text = 'Кол-во итераций', font = ('Times New Roman',14), width = 15, anchor = 'e')
max_iter.grid(row = 4, column = 0)
max_iter_e = Entry (frame1, width = 20, font = ('Times New Roman',14))
max_iter_e.insert(END, '100')
max_iter_e.grid(row = 4, column = 1)

frame2 = Frame(win)
frame2.pack()
but = Button(frame2, text = 'Рассчитать',font = ('Times New Roman',14), width = 20, command = calc)
but.pack(pady = 20, side = 'top')

win.mainloop()