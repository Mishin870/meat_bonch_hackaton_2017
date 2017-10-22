import os, sys
import random
from tkinter import *
<<<<<<< HEAD
from p.calcDecrements import getDecrements
import matplotlib.pyplot as plt
import datetime
from tkinter.messagebox import *
=======
import p.calcDecrements
>>>>>>> eee275df2d5df4f882159dc88cef5bf98f344deb

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
        if day < 0 or day >= len(metas[0]):
            print("out of bounds")
            return
        else:
            # for items in metas[day]:
            #    print(items)
            # print("===================================")
            pos = root.winfo_pointerxy()
            x = pos[0]
            y = pos[1]
            # sub
            sub = Tk()
            sub.wm_title(metas[0][day][0][0])
            sub.geometry('400x400+' + str(x) + '+' + str(y))
            txt = Text(sub)
            txt.pack()
            text = ""
            for meta in metas:
                text += prepareText(meta[day])
            txt.insert('1.0', text)
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

def drawPlot(xs, ys, colors, legends, title=u'Мясные потери', xlabel='Недели', ylabel='Стоимость, руб'):
    lines = []
    for x, y, color, legend in zip(xs, ys, colors, legends):
        lines.append(plt.plot(x, y, color + 'o:', label=legend))

    xMaxs = []
    for x in xs:
        xMaxs.append(max(x))
    x_axis = max(xMaxs)

    yMaxs = []
    for y in ys:
        yMaxs.append(max(y))
    y_axis = max(yMaxs)

    plt.axis([0, x_axis , 0, y_axis + 25])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    i = 1
    for line in lines:
        tmp = plt.legend(handles=line, loc=i)
        plt.gca().add_artist(tmp)
        i += 1
    plt.grid()

    plt.connect('button_release_event', mouseRelease)
    plt.connect('button_press_event', mousePress)
    plt.show()


root = Tk()
<<<<<<< HEAD
root.geometry('300x150')


def btn_1_cl(event):
    mon = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь']
    try:
        value = listbox.get(listbox.curselection())
        param = mon.index(value) + 1
    except:
        showinfo('Ошибка', 'Выберите месяц!')
        return

    global metas
    vals16 = calcValuesByMon(2016, param)
    vals17 = calcValuesByMon(2017, param)
=======
root.geometry('{}x{}'.format(600, 600))
tx = Text(root, font=('courier new', 12), width=50, height=15)
tx.place(x=5, y=30, width=550, height=500)


def test():
    for file in files:
        with open('files/' + file, encoding='UTF-8') as f:
            for line in f:
                tmp = ''
                items = line.split("\t")
                for el in range(len(text)):
                    tmp += str(el) + ') ' + text[el] + ':' + items[el] + '\n'
                tx.insert('1.0', tmp)
        break


def btn_1_cl(event):
    test()


btn1 = Button(root)
btn1['text'] = 'PRESS ME TO DOWNLOAD FILE'
btn1.place(x=5, y=5, width=550, height=20)
btn1.bind('<Button-1>', btn_1_cl)

btn2 = Button(root)
btn2['test'] = 'CALC'
btn2.place(x = 560, y = 5, width=50, heihgt=20)
btn2.bind('<Button-1>', btn_2_cl)
>>>>>>> eee275df2d5df4f882159dc88cef5bf98f344deb

    metas = [vals16[1], vals17[1]]
    maxLen = max([len(metas[0]), len(metas[1])])
    for meta in metas:
        while len(meta) < maxLen:
            meta.append([])

    drawPlot(xs=[range(len(vals16[0])), range(len(vals17[0]))], ys=[vals16[0], vals17[0]], colors=['r', 'g'], legends=['2016 год', '2017 год'], title=u'Мясные потери', xlabel=u'Дни', ylabel=u'Потери, руб')

def calcValuesByMon(year, mon):
    path = str(sys.path[0]) + "/files_date/"
    tmp = os.listdir(path)
    files = []
    for fileName in tmp:
        if fileName.endswith(str(year)):
            files.append(fileName)
    files = sorted(files, key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y'))
    retDates = []
    retMetas = []
    i = 0
    for file in files:
        buf = file.title()[4]
        if buf != str(mon):
            continue

        f = open(path + file, 'r', encoding='utf-8')
        tmp = []
        for line in f:
            tmp.append(line.split("\t"))
        obj = getDecrements(tmp)
        retDates.append(obj[0])
        retMetas.append(obj[1])
        i = i + 1
    return [retDates, retMetas, i]

def calcValues(year):
    path = str(sys.path[0]) + "/files_date/"
    tmp = os.listdir(path)
    files = []
    for fileName in tmp:
        if fileName.endswith(str(year)):
            files.append(fileName)
    files = sorted(files, key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y'))
    retDates = []
    retMetas = []
    i = 0
    for file in files:
        f = open(path + file, 'r', encoding='utf-8')
        tmp = []
        for line in f:
            tmp.append(line.split("\t"))
        obj = getDecrements(tmp)
        retDates.append(obj[0])
        retMetas.append(obj[1])
        i = i + 1
    return [retDates, retMetas, i]

def btn_2_cl(event):
    global metas
    vals16 = calcValues(2016)
    vals17 = calcValues(2017)

    metas = [vals16[1], vals17[1]]
    maxLen = max([len(metas[0]), len(metas[1])])
    for meta in metas:
        while len(meta) < maxLen:
            meta.append([])

    drawPlot(xs=[range(len(vals16[0])), range(len(vals17[0]))], ys=[vals16[0], vals17[0]], colors=['r', 'g'], legends=[u'2016 год', u'2017 год'], title=u'Мясные потери', xlabel=u'Дни', ylabel=u'Потери, руб')

def btn_3_cl(event):
    pass

def btn_4_cl(event):
    pass


value = 'a'


def select_item(event):
    # value = listbox.get(listbox.curselection())
    # print('value:', value)
    # return value
    pass


listbox_items = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
                 'Сентябрь']

listbox = Listbox(root)
listbox.place(x=5, y=20, width=80, height=80)
listbox.bind('<Button-1>', select_item)
# value = select_item(event='<Button-1>')

for item in listbox_items:
    listbox.insert(END, item)

# value = listbox.get(first=listbox.curselection())


lb1 = Label(root)
lb1['text'] = 'Потери при движении 261 > 531'
lb1.place(x=95, y=0)

# lb2 = Label(root)
# lb2['text'] = 'Прибыль'
# lb2.place(x=100, y=60)

btn1 = Button(root)
btn1['text'] = 'За месяц'
btn1.place(x=100, y=20, width=80, height=40)
btn1.bind('<ButtonRelease>', btn_1_cl)

btn2 = Button(root)
btn2['text'] = 'За всё время'
btn2.place(x=190, y=20, width=80, height=40)
btn2.bind('<ButtonRelease>', btn_2_cl)

# btn3 = Button(root)
# btn3['text'] = 'За месяц'
# btn3.place(x=100, y=80, width=80, height=40)
# btn3.bind('<Button-1>', btn_3_cl)
#
# btn4 = Button(root)
# btn4['text'] = 'За всё время'
# btn4.place(x=190, y=80, width=80, height=40)
# btn4.bind('<Button-1>', btn_4_cl)

directory = 'files'

root.mainloop()
