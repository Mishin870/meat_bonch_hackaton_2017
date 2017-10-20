# import matplotlib.pyplot as plt
# import numpy
import csv

with open('db_100.csv', newline='', encoding='utf-8') as f:

    text = ['Дата Проводки', 'Код Материала', 'Код EAN/UPC', 'Описание материала', 'Код Вида Материала',
            'Код Группы Материала', 'Описание Группы Материала', 'Код Вида Движения Материала',
            'Описание Вида Движения Материала', 'Количество', 'Еденица Измерения', 'Сумма в средней цене',
            'Сумма Стоимости в Чеке', 'Код Поставщика', 'Код Магазина', 'Код Склада', 'Ссылка на Заказ Поставщика',
            'Ссылка на Документ Товародвижения', 'Ссылка на Счет-фактуру']


    def show(reader, value='-1'):
        for row in reader:
            tmp = ''
            for el in row:
                tmp = tmp + str(el) + '.'
            arr = tmp.split('\t')
            if value == '-1':
                for el in range(len(text)):
                    print(str(el) + ') ' + text[el] + ':', arr[el])
                print('\n')
            else:
                if arr[17] == value:
                    for el in range(len(text)):
                        print(str(el) + ') ' + text[el] + ':', arr[el])
                    print('\n')


    def search(reader, param=0, value=''):
        print(text[param] + ': ' + value)
        for row in reader:
            tmp = ''
            for el in row:
                tmp = tmp + str(el) + '.'
            arr = tmp.split('\t')
            if arr[param] == value:
                print(text[17] + ': ' + arr[17])


    reader = csv.reader(f)
    search(reader, param=9, value='2.000')

    # reader = csv.reader(f)
    show(reader, value='4902915744')

