import os
from tkinter import *
import p.calcDecrements

text = ['Дата Проводки', 'Код Материала', 'Код EAN/UPC', 'Описание материала', 'Код Вида Материала',
        'Код Группы Материала', 'Описание Группы Материала', 'Код Вида Движения Материала',
        'Описание Вида Движения Материала', 'Количество', 'Еденица Измерения', 'Сумма в средней цене',
        'Сумма Стоимости в Чеке', 'Код Поставщика', 'Код Магазина', 'Код Склада', 'Ссылка на Заказ Поставщика',
        'Ссылка на Документ Товародвижения', 'Ссылка на Счет-фактуру']

root = Tk()
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

directory = 'files'
files = os.listdir(directory)

# def open_file():
#     for file in files:
#         with open(file, encoding='UTF-8') as f:
#             for line in f:
#                 items = line.split("\t")
#                 return str(items)



root.mainloop()
