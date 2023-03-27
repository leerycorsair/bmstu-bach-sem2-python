#Программа для сложения и вычитания восьмеричных чисел с интерфейсом tkinter.

#Леонов Владислав
#ИУ7-26Б

from tkinter import *
from tkinter import messagebox
from tkinter.font import Font


def prog_info():
    info = '''Данная программа предназначена для иммитации операций арифметики \
в восьмеричной системе счисления.

Доступные операции: сложение, вычитание

При работе в 10-ой системе используются цифры "0123456789" и знаки "+-.".
При работе в 8-ой системе используются цифры "01234567" и знаки "+-.".

Примечание 1: пользователь может вводить числа как в восьмеричной, так и в \
десятиричной системе счисления (Можно выбрать СС в соответствующем поле)

Примечание 2: при работе в 8-ой системе предполагается, после каждого знака идет \
число. 

Версия: 0.1.0
    '''
    messagebox.showinfo(title = 'О программе', message = info)
    
def cr_info():
    info ='''Создателем данной программы является студент МГТУ им. Н.Э. Баумана группы ИУ7-26Б ,\n\
Леонов Владислав Вячеславович'''
    messagebox.showinfo(title = 'О создателе', message = info)
    
def insertion(st):
    global ss
    if ss.get() == 1 and (st == '8' or st == '9'):
        error_info = '''В выбранной вами системе счисления отсутствует данная цифра'''
        messagebox.showerror(title = 'Ошибка', message = error_info)
    else: 
        global ent
        ent.insert(len(ent.get()), st)
        
def last_del():
    global ent
    ent.delete(len(ent.get())-1,len(ent.get()))

def clear():
    global ent
    ent.delete(0,len(ent.get()))
    
def check(s,ss):
    if ss == 0:
        for i in range(len(s)):
            if s[i] not in '0123456789+-. ':
                return False
    else:
        for i in range(len(s)):
            if s[i] not in '01234567+-. ':
                return False  
    return True

def oct_conv(n):
    b = ''
    mc = False
    if n<0:
        mc = True
        n = abs(n)
    while n > 0:
        b = str(n % 8) + b
        n = n // 8
    b = '0o'+b
    if b == '0o' or b =='-0o':
        b = '0o0'
    if mc:
        b = '-'+b
    return b

def octsum(a,b):
    if '.' not in a:
        a += '.0'
    if '.' not in b:
        b += '.0'
    
    if a.count('.') == 1:
        a = a.split('.')
    else:
        return 'ERROR'
    if b.count('.') == 1:
        b = b.split('.')
    else:
        return 'ERROR'
    
    a_f = a[1]
    b_f = b[1]
    if len(a_f)>len(b_f):
        while len(a_f)!=len(b_f):
            b_f += '0'
    elif len(b_f)>len(a_f):
        while len(a_f)!=len(b_f):
            a_f += '0'
        
    leng= len(a_f)
    num_1 = a[0]+a_f
    num_2 = b[0]+b_f
    res = oct_conv(eval(num_1 + num_2))
    if res[0][0]=='0':
        res = '+'+ res
    res_1 = res[:len(res)-leng]+'.'+res[len(res)-leng:]
    while res_1[len(res_1)-1] == '0':
        res_1 = res_1[:-1]
    if res_1[len(res_1)-1] =='.':
        res_1= res_1[:-1]
    if len(res_1)>3:
        if res_1[3]=='.':
            res_1 = res_1[:3]+'0'+res_1[3:]
    else:
        return ('+0o0')
    return res_1
    
        
def oct_r(exp):
    exp = exp.replace('+', 'p+')
    exp = exp.replace('-', 'p-')
    a = exp.split('p')
    if a[0] == '' or a[0] == '0o':
         del(a[0])
    if len(a) == 1:
        if a[0][0]== '-':
            return a[0]
        else:
            return ('+'+a[0])
    while len(a)!= 1:
        if a[0] == '' or a[0] == '0o':
            del(a[0])
        a[0] = octsum(a[0], a[1])
        if a[0]=='ERROR':
            messagebox.showerror(title = 'Ошибка', message = 'Не верное выражение.')
            return 'ERROR'
        del(a[1])
    return a[0]
    

def result():
    global ent, ss
    exp = ent.get()
    if check(exp, ss.get()):
        if ss.get() == 0:
            try: 
                res = eval(exp)
                res = '{:^.3f}'.format(res)
                clear()
                ent.insert(0, res)
            except:
                messagebox.showerror(title = 'Ошибка', message = 'Не верное выражение.')
        else:
            exp = '0o' + exp
            exp = exp.replace('+','+0o')
            exp = exp.replace('-','-0o')
            try:
                res = oct_r(exp)
                if res == 'ERROR':
                    return
                clear()
                if res[0]=='-':
                    ent.insert(0,'-' + res[3:])
                else:
                    ent.insert(0,res[3:])
            except:
                messagebox.showerror(title = 'Ошибка', message = 'Не верное выражение.')
    else:
        messagebox.showerror(title = 'Ошибка', message = 'Не верное выражение.')
            
win = Tk()
win.geometry('640x285')
win.configure(background = '#9C1D1D')
win.title('Калькулятор восьмеричных чисел')
win.resizable(0,0)

mainmenu = Menu(win, tearoff = 0)
win.config (menu = mainmenu)

optionsmenu = Menu(mainmenu, tearoff = 0)
optionsmenu.add_command(label = 'Сложение', command = lambda n='+':insertion(n))
optionsmenu.add_command(label = 'Вычитание', command = lambda n='-':insertion(n))
optionsmenu.add_command(label = 'Результат', command = lambda: result())
optionsmenu.add_command(label = 'Очистить', command = lambda: clear())
mainmenu.add_cascade(label = 'Опции', menu = optionsmenu)

helpmenu = Menu(mainmenu, tearoff = 0)
helpmenu.add_command(label = 'О программе', command = lambda: prog_info())
helpmenu.add_command(label = 'О создателе', command = lambda: cr_info())
mainmenu.add_cascade(label = 'Справка', menu = helpmenu )

e_frame = Frame (win, padx = 10, pady = 10, bg = '#9C1D1D')
e_frame.grid(row = 0)
ent = Entry (e_frame, width = 26, font = ('Times New Roman',28))
ent.pack(side = 'left')
del_but = Button (e_frame,font = ('Times New Roman Bold',18), text = '<--', \
command = last_del, bg = '#620B0B', fg = '#eee')
del_but.pack(side = 'left')
bot_frame = Frame(win, bg = '#9C1D1D')
sys_frame = LabelFrame (bot_frame, text = 'Cистема\n счисления:',\
font = ('Times New Roman Bold', 14), fg = '#eee', labelanchor = 'n',bg = '#9C1D1D')
sys_frame.grid(row = 1, column = 0, sticky = 'n',padx = 5)

ss = IntVar()
dec_s = Radiobutton(sys_frame, text = 'Десятичная', variable = ss, value = 0, \
font = ('Times New Roman Bold',14), \
command = clear, bg = '#eee', fg = '#620B0B', width = 12)
oct_s = Radiobutton(sys_frame, text = 'Восьмиричная', variable = ss, value = 1,\
font = ('Times New Roman Bold',14), \
command = clear, bg = '#eee', fg = '#620B0B', width = 12)
dec_s.pack()
oct_s.pack()

but_frame = Frame(bot_frame, padx = 10, pady = 10, bg = '#9C1D1D')
but_frame.grid(row = 1, column = 1)
but_1 = Button(but_frame, text = '1',font = ('Times New Roman Bold',18), width = 8, \
command = lambda n='1':insertion(n), bg = '#620B0B', fg = '#eee')
but_1.grid(row = 0, column = 0)
but_2 = Button(but_frame, text = '2',font = ('Times New Roman Bold',18),width = 8, \
command = lambda n='2':insertion(n), bg = '#620B0B', fg = '#eee')
but_2.grid(row = 0, column = 1)
but_3 = Button(but_frame, text = '3',font = ('Times New Roman Bold',18),width = 8, \
command = lambda n='3':insertion(n), bg = '#620B0B', fg = '#eee')
but_3.grid(row = 0, column = 2)
but_c = Button(but_frame, text = 'C',font = ('Times New Roman Bold',18),width = 4, \
command = clear, bg = '#620B0B', fg = '#eee')
but_c.grid(row = 0, column = 3, padx = 10)
but_4 = Button(but_frame, text = '4',font = ('Times New Roman Bold',18),width = 8, \
command = lambda n='4':insertion(n), bg = '#620B0B', fg = '#eee')
but_4.grid(row = 1, column = 0)
but_5 = Button(but_frame, text = '5',font = ('Times New Roman Bold',18),width = 8, \
command = lambda n='5':insertion(n), bg = '#620B0B', fg = '#eee')
but_5.grid(row = 1, column = 1)
but_6 = Button(but_frame, text = '6',font = ('Times New Roman Bold',18),width = 8, \
command = lambda n='6':insertion(n), bg = '#620B0B', fg = '#eee')
but_6.grid(row = 1, column = 2)
but_p = Button(but_frame, text = '+',font = ('Times New Roman Bold',18),width = 4, \
command = lambda n='+':insertion(n), bg = '#620B0B', fg = '#eee')
but_p.grid(row = 1, column = 3, padx = 10)
but_7 = Button(but_frame, text = '7',font = ('Times New Roman Bold',18),width = 8, \
command = lambda n='7':insertion(n), bg = '#620B0B', fg = '#eee')
but_7.grid(row = 2, column = 0)
but_8 = Button(but_frame, text = '8',font = ('Times New Roman Bold',18),width = 8, \
command = lambda n='8':insertion(n), bg = '#620B0B', fg = '#eee')
but_8.grid(row = 2, column = 1)
but_9 = Button(but_frame, text = '9',font = ('Times New Roman Bold',18),width = 8, \
command = lambda n='9':insertion(n), bg = '#620B0B', fg = '#eee')
but_9.grid(row = 2, column = 2)
but_m = Button(but_frame, text = '-',font = ('Times New Roman Bold',18),width = 4, \
command = lambda n='-':insertion(n), bg = '#620B0B', fg = '#eee')
but_m.grid(row = 2, column = 3, padx = 10)
but_0 = Button(but_frame, text = '0',font = ('Times New Roman Bold',18),width = 8, \
command = lambda n='0':insertion(n), bg = '#620B0B', fg = '#eee')
but_0.grid(row = 3, column = 1)
but_d = Button(but_frame, text = '.',font = ('Times New Roman Bold',18),width = 8, \
command = lambda n='.':insertion(n), bg = '#620B0B', fg = '#eee')
but_d.grid(row = 3, column = 2)
but_e = Button(but_frame, text = '=',font = ('Times New Roman Bold',18),width = 4, \
command = result, bg = '#620B0B', fg = '#eee')
but_e.grid(row = 3, column = 3, padx = 10)
bot_frame.grid(row = 1)
win.mainloop()