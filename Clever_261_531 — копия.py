import os, sys
from tkinter import *
from p.calcDecrements import getDecrements
import matplotlib.pyplot as plt
import datetime

text = ['Дата Проводки', 'Код Материала', 'Код EAN/UPC', 'Описание материала', 'Код Вида Материала',
        'Код Группы Материала', 'Описание Группы Материала', 'Код Вида Движения Материала',
        'Описание Вида Движения Материала', 'Количество', 'Еденица Измерения', 'Сумма в средней цене',
        'Сумма Стоимости в Чеке', 'Код Поставщика', 'Код Магазина', 'Код Склада', 'Ссылка на Заказ Поставщика',
        'Ссылка на Документ Товародвижения', 'Ссылка на Счет-фактуру']
metas = []

def prepareText(meta):
    ret = ""
    for items in meta:
        ret += items[3] + ";" + items[17] + "\n"
    return ret

def on_click(event):
    if event.inaxes is not None:
        day = int(round(event.xdata))
        if day < 0 or day >= len(metas):
            print("out of bounds")
            return
        else:
            #for items in metas[day]:
            #    print(items)
            #print("===================================")
            pos = root.winfo_pointerxy()
            x = pos[0]
            y = pos[1]
            # sub
            sub = Tk()
            sub.wm_title(metas[day][0][0])
            sub.geometry('400x400+' + str(x) + '+' + str(y))
            txt = Text(sub)
            txt.pack()
            txt.insert('1.0', prepareText(metas[day]))
            txt.config(state=DISABLED)

mousePressed = False
storedX = 0
storedY = 0
THRESHOLD = 5

def mousePress(event):
    global mousePressed, storedY, storedX
    mousePressed = True
    pos = root.winfo_pointerxy()
    storedX = pos[0]
    storedY = pos[1]

def mouseRelease(event):
    global mousePressed, storedX, storedY
    if mousePressed == True:
        mousePressed = False
        pos = root.winfo_pointerxy()
        dx = pos[0] - storedX
        dy = pos[1] - storedY
        print(dx, dy)
        if abs(dx) < THRESHOLD and abs(dy) < THRESHOLD:
            on_click(event)

def drawPlot(x, y, title=u'Мясные потери', xlabel='Недели', ylabel='Стоимость, руб'):
    # matplotlib.style.use('ggplot')
    line_plot = plt.plot(x, y, linewidth=0.5)
    x_axis = max(x)
    y_axis = max(y)
    plt.axis([0, x_axis + 25, 0, y_axis + 25])
    plt.title(title)
    plt.colors = 'g'
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.legend((line_10), (u'Температура 10 \u00b0C'))
    plt.grid()

    # value = plt.xscale
    # print(value)

    plt.connect('button_release_event', mouseRelease)
    plt.connect('button_press_event', mousePress)
    plt.show()


root = Tk()
root.geometry('300x150')


def btn_2_cl(event):
    path = str(sys.path[0]) + "/files_date/"
    files = sorted(os.listdir(path), key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y'))
    dates = []
    i = 0
    for file in files:
        f = open(path + file, 'r', encoding='utf-8')
        tmp = []
        for line in f:
            tmp.append(line.split("\t"))
        obj = getDecrements(tmp)
        dates.append(obj[0])
        metas.append(obj[1])
        i = i + 1
    drawPlot(x=range(i), y=dates, title=u'Мясные потери', xlabel=u'Дни', ylabel=u'Потери, руб')


def btn_3_cl(event):
    pass


def btn_4_cl(event):
    pass


def select_item(event):
    value = listbox.get(listbox.curselection())
    print('value:', value)
    return value


listbox_items = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
                 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

listbox = Listbox(root)
listbox.place(x=5, y=20, width=80, height=80)
# value = select_item(event='<Button-1>')
for item in listbox_items:
    listbox.insert(END, item)

# def select_item(event):
#     value = (listbox.get(listbox.curselection()))
#     print(value)


listbox.bind('<<ListboxSelect>>', select_item)

# value = listbox.get(first=listbox.curselection())


def btn_1_cl(event):
    path = str(sys.path[0]) + "/files_date/"
    files = sorted(os.listdir(path), key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y'))
    dates = []
    i = 0
    for file in files:
        f = open(path + file, 'r', encoding='utf-8')
        tmp = []
        for line in f:
            tmp.append(line.split("\t"))
        obj = getDecrements(tmp)
        dates.append(obj[0])
        metas.append(obj[1])
        i = i + 1
    drawPlot(x=range(i), y=dates, color='green', title=u'Мясные потери за {}'.format(select_item(event)), xlabel=u'Дни', ylabel=u'Потери, руб')


lb1 = Label(root)
lb1['text'] = 'Потери при движении 261 > 531'
lb1.place(x=95, y=0)

# lb2 = Label(root)
# lb2['text'] = 'Прибыль'
# lb2.place(x=100, y=60)

btn1 = Button(root)
btn1['text'] = 'За месяц'
btn1.place(x=100, y=20, width=80, height=40)
btn1.bind('<Button-1>', btn_1_cl)

btn2 = Button(root)
btn2['text'] = 'За всё время'
btn2.place(x=190, y=20, width=80, height=40)
btn2.bind('<Button-1>', btn_2_cl)

# btn3 = Button(root)
# btn3['text'] = 'За месяц'
# btn3.place(x=100, y=80, width=80, height=40)
# btn3.bind('<Button-1>', btn_3_cl)
#
# btn4 = Button(root)
# btn4['text'] = 'За всё время'
# btn4.place(x=190, y=80, width=80, height=40)
# btn4.bind('<Button-1>', btn_4_cl)

#butTest = Button(root)
#butTest['text'] = 'test'
#butTest.place(x=190+80+10, y=20, width=80, height=60)
#butTest.bind('<Button-1>', butTestClick)

directory = 'files'

root.mainloop()
