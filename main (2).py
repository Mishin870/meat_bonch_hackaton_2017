# import matplotlib.pyplot as plt
# import numpy
import csv

with open('db_100.csv', newline='', encoding='utf-8') as f:
    text = ['Дата Проводки', 'Код Материала', 'Код EAN/UPC', 'Описание материала', 'Код Вида Материала',
            'Код Группы Материала', 'Описание Группы Материала', 'Код Вида Движения Материала',
            'Описание Вида Движения Материала', 'Количество', 'Еденица Измерения', 'Сумма в средней цене',
            'Сумма Стоимости в Чеке', 'Код Поставщика', 'Код Магазина', 'Код Склада', 'Ссылка на Заказ Поставщика',
            'Ссылка на Документ Товародвижения', 'Ссылка на Счет-фактуру']

    def show(reader, value=0):
        if value == 0:
            for row in reader:
                tmp = ''
                for el in row:
                    tmp = tmp + str(el) + '.'
                arr = tmp.split('\t')
                for el in range(len(text)):
                    print(str(el) + ') ' + text[el] + ':', arr[el])
                    # if el%5 == 0: print('')
                print('\n')


    def search(reader, param=0, value=''):
        for row in reader:
            tmp = ''
            for el in row:
                tmp = tmp + str(el) + '.'
            arr = tmp.split('\t')
            if arr[param] == value:
                print(text[17] + ': ' + arr[17])
                print(text[param] + ': ' + arr[param])
                print('\n')
        pass


    reader = csv.reader(f)
    # show(reader)
    search(reader, param=9, value='2.000')
