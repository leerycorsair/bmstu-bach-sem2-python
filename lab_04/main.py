#Программа предназначенна для решения следующей задачи:
#для заданных точек и окружностей найти прямую, пресекающую наибольшее число
#окружностей + графическая иллюстрация.

#Леонов Владислав
#ИУ7-26Б

from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from tkinter import ttk
from math import *
from random import*

def prog_info():
    info = '''Данная программа предназначена для решения планиметрической задачи \
построения прямой, проходящей через заданные точки и пересекающей наибольшее число \
заданных окружностей.

Внимание!
При использовании ввода с помощью компьютерной мышки, рабочее поле ограниченно \
координатами поля (x[-580;580]; y[-350;350]).

В случае необходимости работы с большим диапазоном координат необходимо \
использовать ручной ввод через соответствующие поля.


Версия: 0.1.0
    '''
    messagebox.showinfo(title = 'О программе', message = info)
    
def cr_info():
    info ='''Создателем данной программы является\nстудент МГТУ им. Н.Э. Баумана группы ИУ7-26Б,\n\
Леонов Владислав Вячеславович'''
    messagebox.showinfo(title = 'О создателе', message = info)

def help_info():
    info = '''Для программы можно использовать ввод данных с клавиатуры, заполняя соответствующие \
поля, а также путем использования компьютерной мышки (ЛКМ - добавить точку, ПКМ - задать центр окружности и, не отпуская, \
отвести на значение необходимого значения радиуса)

Режим ввода с помощью мыши имеет ограничения по координатам (x[-580;580]; y[-350;350])
'''
    messagebox.showinfo(title = 'Помощь', message = info)

def draw_line():
    global canvas, line_id,dots
    if line_id:
        canvas.delete(line_id)
    m_intersections = 0
    for i in range (len(dots) - 1):
        for j in range(i+1, len(dots)):
            intersections = get_intersection(dots[i][0],dots[i][1],dots[j][0],dots[j][1])
            if intersections > m_intersections:
                m_intersections = intersections
                coords = (dots[i][0],dots[i][1],dots[j][0],dots[j][1])
    if m_intersections > 0:
        info ='Результатом выполнения программы является прямая, проходящая через \
точки с координатами (' + str(coords[0]) + ';'+str(coords[1]) + ') и (' +\
str(coords[2]) + ';'+str(coords[3]) + '), пересекающая ' + str(m_intersections) + ' окружность(-ей)'
        
        if coords[2]-coords[0] != 0:
            m = (coords[3]-coords[1])/(coords[2]-coords[0])
            b = coords[1]-(m*coords[0])
            line_id = canvas.create_line((-10000 + 580),-(m*(-10000)+b)+350,+10000+580,-(m*(+10000)+b)+350, width = 3, fill = '#FF0000')
        else:
            line_id = canvas.create_line(coords[0]+580,-((-10000))+350,coords[0]+580,-((+10000))+350, width = 3, fill = '#FF0000')
        messagebox.showinfo(title = 'Результат', message = info)
    else:
        messagebox.showinfo(title = 'Результат', message = 'Прямой, пересекающей окружности и проходящей через заданные точки, не существует.')                  
                                     
def get_intersection(x1,y1,x2,y2):
    intersections = 0
    global circles
    for i in range(len(circles)):
        if is_intersect(x1,y1,x2,y2, circles[i][0],circles[i][1],circles[i][2]):
            intersections += 1    
    return intersections

def is_intersect(x1,y1,x2,y2,c_x, c_y, r):
    dist = (abs((y2-y1)*c_x-(x2-x1)*c_y+x2*y1-y2*x1)/sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1)))
    if r>dist-1e-6:
        return True
    else:
        return False
    
def del_data(data):
    global canvas, dots, circles, line_id
    dots = []
    circles = []
    canvas.delete("all")
    line_id = False
    canvas.create_line(0,350,1160,350,width = 2, arrow = 'last')
    canvas.create_line(580,700, 580, 0, width = 2, arrow = 'last' )
    messagebox.showinfo(title = 'Внимание', message = 'Данные успешно очищены' )
    data.destroy()


def show_data():
    data = Tk()
    data.title('Данные построения')
    data.configure(background = '#FF9200')
    data.resizable(0,0)
    
    
    table_frame = Frame(data, padx = 15, pady = 15, background = '#FF9200')
    dots_label = Label(table_frame, text = 'Точки',font = ('Times New Roman',14),background = '#FF9200')
    dots_label.grid(row = 0, column = 0)
    circ_label = Label(table_frame, text = 'Окружности',font = ('Times New Roman',14),background = '#FF9200')
    circ_label.grid(row = 0, column = 1)
    #dots
    dots_table = ttk.Treeview(table_frame)
    dots_table.configure(columns = ['Координата X', 'Координата Y'])
    dots_table.heading('#0', text = 'N')
    dots_table.heading('Координата X', text = 'Координата X')
    dots_table.heading('Координата Y', text = 'Координата Y')

    dots_table.column('Координата X',width = 185, anchor= 'center')
    dots_table.column('Координата Y',width = 185, anchor= 'center')  
    dots_table.column('#0',width = 70, anchor= 'center')        
    
    global dots
    for i in range(len(dots)):
        dots_table.insert('','end', text = i+1, values = dots[i])
    dots_table.grid(row = 1, column = 0, padx = 10)
    #circles
    circ_table = ttk.Treeview(table_frame)
    circ_table.configure(columns = ['Координата X центра', 'Координата Y центра', 'Радиус'])
    circ_table.heading('#0', text = 'N')
    circ_table.heading('Координата X центра', text = 'Координата X центра')
    circ_table.heading('Координата Y центра', text = 'Координата Y центра')
    circ_table.heading('Радиус', text = 'Радиус')
    
    circ_table.column('Координата X центра',width = 150, anchor= 'center')
    circ_table.column('Координата Y центра',width = 150, anchor= 'center')
    circ_table.column('Радиус',width = 100, anchor= 'center')
    circ_table.column('#0',width = 70, anchor= 'center')
    global circles
    for i in range(len(circles)):
        circ_table.insert('', 'end', text = i+1, values = (circles[i][0], circles[i][1], '{:<14.5g}'.format(circles[i][2])))
    circ_table.grid(row = 1, column = 1, padx = 10)
    table_frame.grid(row = 0, column = 0)
    
    #but
    del_but = Button(data, background = '#FFEF00', text = 'Очистить данные',font = ('Times New Roman',14), \
    command = lambda: del_data(data))
    del_but.grid(row = 1, column = 0, pady = 15)
    data.mainloop()

def add_dot():
    global x_dot_ent, y_dot_ent, dots, canvas
    global minwidth, maxwidth, minheight, maxheight
    x = x_dot_ent.get()
    y = y_dot_ent.get()
    try:
        coordinates = [float(x), float(y)]
        x = float(x) + 580
        y = -(float(y) - 350)
        if coordinates not in dots:
            dots.append(coordinates)
            if x < minwidth:
                minwidth = x - 10
            if x > maxwidth:
                maxwidth = x + 10
            if y < minheight:
                minheight =  y - 10
            if y > maxheight:
                maxheight = y + 10
            canvas.configure(scrollregion = (minwidth, minheight, maxwidth, maxheight))
            canvas.create_oval((x-2),(y-2),(x+2),(y+2), fill = '#0000FF')
        else:
             messagebox.showinfo(title = 'Предупреждение', message = 'Точка уже задана')
    except:
        messagebox.showerror(title = 'Ошибка', message = 'Некорректные входные данные')

def add_circle():
    global x_circ_ent, y_circ_ent, circ_r_ent, circles, canvas
    global minwidth, maxwidth, minheight, maxheight
    x = x_circ_ent.get()
    y = y_circ_ent.get()
    r = circ_r_ent.get()
    try:
        coordinates = [float(x), float(y), float(r)]
        x = float(x) + 580
        y = -(float(y) - 350)
        r = float(r)
        if coordinates not in circles:
            circles.append(coordinates)
            if x - r < minwidth:
                minwidth = x - r - 10
            if x + r > maxwidth:
                maxwidth = x + r + 10
            if y - r < minheight:
                minheight =  y - r - 10
            if y + r> maxheight:
                maxheight = y + r + 10
            canvas.configure(scrollregion = (minwidth, minheight, maxwidth, maxheight))
            canvas.create_oval((x-r),(y-r),(x+r),(y+r), width = 2, outline = '#FF5C00')
        else:
             messagebox.showinfo(title = 'Предупреждение', message = 'Окружность уже задана')
    except:
        messagebox.showerror(title = 'Ошибка', message = 'Некорректные входные данные')

 
def click(event):
    lastx, lasty = event.x, event.y
    global dots
    coords = [lastx-580, -lasty+350]
    dots.append(coords)
    canvas.create_oval((lastx-2, lasty-2, lastx+2, lasty+2), fill = '#0000FF')
 
lastx = 0; lasty =0
def rightclick1(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def rightclick2(event):
    global lastx, lasty, canvas
    r = sqrt((event.x-lastx)*(event.x-lastx)+(event.y-lasty)*(event.y-lasty))
    global circles
    coords = [lastx-580, -lasty+350, r]
    circles.append(coords)
    canvas.create_oval((lastx-r),(lasty-r),(lastx+r),(lasty+r), width = 2, outline = '#FF9200')
    
    
win = Tk()
win.title('Geometry solver')
win.configure(background = '#FF9200')
win.geometry('1500x750+10+10')
win.resizable(0,0)
dots = []
circles = []
line_id = False

ent_frame = Frame(win,background = '#FF9200')

#dots

dot_frame = LabelFrame(ent_frame, text = 'Добавление точки',font = ('Times New Roman',14), padx = 15, pady = 15,background = '#FF9200')

x_dot_label = Label(dot_frame,  text = 'Координата X точки:', font = ('Times New Roman',14), width = 20, anchor = 'center',background = '#FF9200')
x_dot_label.grid(column = 0, row = 0)
x_dot_ent = Entry(dot_frame, width = 20,font = ('Times New Roman',14), bg = '#FFFA64')
x_dot_ent.grid(column = 0, row = 1)

y_dot_label = Label(dot_frame,  text = 'Координата Y точки:', font = ('Times New Roman',14), width = 20, anchor = 'center',background = '#FF9200')
y_dot_label.grid(column = 0, row = 2)
y_dot_ent = Entry(dot_frame, width = 20,font = ('Times New Roman',14),bg = '#FFFA64')
y_dot_ent.grid(column = 0, row = 3)
 
dot_but = Button(dot_frame, text = 'Добавить точку', font = ('Times New Roman',14), width = 20, \
command = lambda: add_dot(),background = '#FFEF00')
dot_but.grid (column = 0, row = 4, pady = 10)

dot_frame.grid(column = 0, row = 0, padx = 15, pady = 15)

#circles
circ_frame = LabelFrame(ent_frame, text = 'Добавление окружности',font = ('Times New Roman',14), padx = 15, pady = 15,background = '#FF9200')

x_circ_label = Label(circ_frame,  text = 'Координата X центра:', font = ('Times New Roman',14), width = 20, anchor = 'center',background = '#FF9200')
x_circ_label.grid(column = 0, row = 0)
x_circ_ent = Entry(circ_frame, width = 20,font = ('Times New Roman',14),bg = '#FFFA64')
x_circ_ent.grid(column = 0, row = 1)

y_circ_label = Label(circ_frame,  text = 'Координата Y центра:', font = ('Times New Roman',14), width = 20, anchor = 'center',background = '#FF9200')
y_circ_label.grid(column = 0, row = 2)
y_circ_ent = Entry(circ_frame, width = 20,font = ('Times New Roman',14),bg = '#FFFA64')
y_circ_ent.grid(column = 0, row = 3)

circ_r_label = Label(circ_frame, text  = 'Радиус окружности', font = ('Times New Roman',14), width = 20, anchor = 'center',background = '#FF9200')
circ_r_label.grid (column = 0, row = 4)
circ_r_ent = Entry(circ_frame, width = 20, font = ('Times New Roman',14),bg = '#FFFA64')
circ_r_ent.grid(column = 0, row = 5)

circ_but = Button(circ_frame, text = 'Добавить окружность', font = ('Times New Roman',14), width = 20,\
command = lambda: add_circle(),background = '#FFEF00')
circ_but.grid (column = 0, row = 6, pady = 10)

circ_frame.grid(column = 0, row = 1, padx = 15, pady = 15)

ent_frame.grid(column = 0,row = 0, padx = 15, pady  = 15)

#bot
bot_frame = Frame(ent_frame, padx = 15, pady = 15,background = '#FF9200')

draw_but = Button(bot_frame, text = 'Построить прямую', font = ('Times New Roman',14), width = 20,background = '#FFEF00',\
command = lambda: draw_line())
draw_but.grid(column = 0, row = 0, pady = 10)

show_but = Button(bot_frame, text = 'Данные построения', font = ('Times New Roman',14), width = 20,background = '#FFEF00',\
command = lambda: show_data())
show_but.grid(column = 0, row = 1, pady = 10)

bot_frame.grid (column = 0, row = 2, padx = 15, pady = 15)

#graph
graph_frame = Frame(win)

minwidth = 0; minheight = 0
maxwidth = 1160; maxheight = 700
canvas=Canvas(graph_frame,bg='white',width=maxwidth,height=maxheight, scrollregion=(minwidth,minheight,maxwidth,maxheight))
hbar=Scrollbar(graph_frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(graph_frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.create_line(0,350,1160,350,width = 2, arrow = 'last')
canvas.create_line(580,700, 580, 0, width = 2, arrow = 'last' )
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

canvas.bind("<Button-1>", click)
canvas.bind("<Button-3>", rightclick1)
canvas.bind("<ButtonRelease-3>", rightclick2)
canvas.pack()

graph_frame.grid(row = 0, column = 1)
#menu

mainmenu = Menu(win, tearoff = 0)
win.config (menu = mainmenu)

helpmenu = Menu(mainmenu, tearoff = 0)
helpmenu.add_command(label = 'О программе', command = lambda: prog_info())
helpmenu.add_command(label = 'О создателе', command = lambda: cr_info())
helpmenu.add_command(label = 'Помощь', command = lambda: help_info())
mainmenu.add_cascade(label = 'Справка', menu = helpmenu )

win.mainloop()
