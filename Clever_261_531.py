import os
from tkinter import *


text = ['Дата Проводки', 'Код Материала', 'Код EAN/UPC', 'Описание материала', 'Код Вида Материала',
        'Код Группы Материала', 'Описание Группы Материала', 'Код Вида Движения Материала',
        'Описание Вида Движения Материала', 'Количество', 'Еденица Измерения', 'Сумма в средней цене',
        'Сумма Стоимости в Чеке', 'Код Поставщика', 'Код Магазина', 'Код Склада', 'Ссылка на Заказ Поставщика',
        'Ссылка на Документ Товародвижения', 'Ссылка на Счет-фактуру']

root = Tk()
root.geometry('{}x{}'.format(600, 600))
tx = Text(root, font=('courier new',12),width=50,height=15)
tx.place(x=5, y=30, width=500, height=500)

def btn_cl(event):
    import


btn = Button(root)
btn['text'] = 'PRESS ME TO DOWNLOAD FILE'
btn.place(x=5, y=5, width=500, height=20)
btn.bind('<Button-1>', btn_cl)

directory = 'files'
files = os.listdir(directory)

# def open_file():
#     for file in files:
#         with open(file, encoding='UTF-8') as f:
#             for line in f:
#                 items = line.split("\t")
#                 return str(items)



root.mainloop()