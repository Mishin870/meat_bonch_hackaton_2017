# import matplotlib.pyplot as plt
# import numpy
import csv
import datetime

with open('db.csv', newline='', encoding='utf-8') as f:
    text = ['Дата Проводки', 'Код Материала', 'Код EAN/UPC', 'Описание материала', 'Код Вида Материала',
            'Код Группы Материала', 'Описание Группы Материала', 'Код Вида Движения Материала',
            'Описание Вида Движения Материала', 'Количество', 'Еденица Измерения', 'Сумма в средней цене',
            'Сумма Стоимости в Чеке', 'Код Поставщика', 'Код Магазина', 'Код Склада', 'Ссылка на Заказ Поставщика',
            'Ссылка на Документ Товародвижения', 'Ссылка на Счет-фактуру']


    def show(reader, *args):
        """
        Выводит на экран полную информацию по Ссылке на докумет товародвижения\n
        Пример show(reader, '4906461659', '4906463289')
        """
        for row in reader:
            tmp = ''
            for el in row:
                tmp = tmp + str(el) + '.'
            arr = tmp.split('\t')

            if arr[17] in args:
                for el in range(len(text)):
                    print(str(el) + ') ' + text[el] + ':', arr[el])
                print('\n')


    def search(reader,interval = '', **kwargs):
        """
        Выводит на экран Ссылку на документ товародвижения(число)\n
        имя параметра задаётся буквой 'а' и числом, число число соответсвует номеру по списку\n
        пример search(reader=reader, a0='30.09.2017', a9='1.800')\n
        где a0 параметр 'Дата Проводки'\n
        где a9 параметр 'Количество'\n
        возвращает числа списком
        """
        if interval != '':
            date1 = interval.split(' ')[0]
            date1 = date1.split('.')
            date2 = interval.split(' ')[1]
            date2 = date2.split('.')
            d1 = datetime.date(day=int(date1[0]), month=int(date1[1]), year=int(date1[2]))
            d2 = datetime.date(day=int(date2[0]), month=int(date2[1]), year=int(date2[2]))
        ret = []
        print('Для ')
        if interval != '':
            print('Интервал:', d1.strftime("%d.%m.%Y"), '-', d2.strftime("%d.%m.%Y"))
        for name, value in kwargs.items():
            print(text[int(name.lstrip('a'))] + ': ' + value)
        print('Найдено:\n')

        for row in reader:
            tmp = ''
            for el in row[]:
                tmp = tmp + str(el) + '.'
            arr = tmp.split('\t')

            i = 0
            for name, value in kwargs.items():
                if interval != 0:
                    tmp = arr[0].split('.')
                    print('>>>', arr[0])
                    d3 = datetime.date(day=int(tmp[0]), month=int(tmp[1]), year=int(tmp[2]))
                    if arr[int(name.lstrip('a'))] == value and d1 <= d3 <= d2:
                        i += 1
                else:
                    if arr[int(name.lstrip('a'))] == value:
                        i += 1
            if i == len(kwargs):
                print(text[17] + ': ' + arr[17])
                ret.append(int(arr[17]))
        return ret


    reader = csv.reader(f)
    # search(reader=reader, a0='30.09.2017', a9='1.800')
    search(reader=reader, interval='1.09.2017 30.09.2017', a9='1.800')

    # f.seek(0)
    # reader = csv.reader(f)
    # show(reader, '4906461659', '4906463289')
