# import matplotlib.pyplot as plt
# import numpy
import csv
import datetime
import matplotlib.pyplot as plt

with open('db2.csv', newline='', encoding='utf-8') as f:
    text = ['Дата Проводки', 'Код Материала', 'Код EAN/UPC', 'Описание материала', 'Код Вида Материала',
            'Код Группы Материала', 'Описание Группы Материала', 'Код Вида Движения Материала',
            'Описание Вида Движения Материала', 'Количество', 'Еденица Измерения', 'Сумма в средней цене',
            'Сумма Стоимости в Чеке', 'Код Поставщика', 'Код Магазина', 'Код Склада', 'Ссылка на Заказ Поставщика',
            'Ссылка на Документ Товародвижения', 'Ссылка на Счет-фактуру']


    def show(reader, list=[], *args):
        """
        Выводит на экран полную информацию по Ссылке на докумет товародвижения\n
        Пример show(reader, '4906461659', '4906463289')
        """
        # print(*args)
        retf = []
        for row in reader:
            ret = []
            tmp = ''
            for el in row:
                tmp = tmp + str(el) + '.'
            arr = tmp.split('\t')

            if list == []:
                if arr[17] in args:
                    for el in range(len(text)):
                        # print(str(el) + ') ' + text[el] + ':', arr[el])
                        ret.append(arr[el])
                    # print('\n')
                    # print('ret', ret)
                    retf.append(ret)
                    # print('1', retf)
            else:
                if arr[17] in list:
                    for el in range(len(text)):
                        # print(str(el) + ') ' + text[el] + ':', arr[el])
                        ret.append(arr[el])
                    # print('\n')
                    # print('ret', ret)
                    retf.append(ret)
                    # print('2', retf)
        # print(retf)
        return retf


    def search(reader, interval='', **kwargs):
        """
        Выводит на экран Ссылку на документ товародвижения(число)\n
        имя параметра задаётся буквой 'а' и числом, число число соответсвует номеру по списку\n
        пример search(reader=reader, a0='30.09.2017', a9='1.800')\n
        где a0 параметр 'Дата Проводки'\n
        где a9 параметр 'Количество'\n
        возвращает числа списком\n
        пример 2 search(reader=reader, interval='25.09.2017 30.09.2017', a9='1.800')\n
        где в interval вносятся даты в формате 'ДД.ММ.ГГГГ ДД.ММ.ГГГГ'
        """
        ret = []
        if interval != '':
            date1 = interval.split(' ')[0]
            date1 = date1.split('.')
            date2 = interval.split(' ')[1]
            date2 = date2.split('.')
            d1 = datetime.date(day=int(date1[0]), month=int(date1[1]), year=int(date1[2]))
            d2 = datetime.date(day=int(date2[0]), month=int(date2[1]), year=int(date2[2]))
            # print('Для ')
            # if interval != '':
            # print('Интервал:', d1.strftime("%d.%m.%Y"), '-', d2.strftime("%d.%m.%Y"))
            # for name, value in kwargs.items():
            # print(text[int(name.lstrip('a'))] + ': ' + value)
        # print('Найдено:\n')

        for row in reader:
            tmp = ''
            for el in row:
                tmp = tmp + str(el) + '.'
            arr = tmp.split('\t')

            i = 0
            for name, value in kwargs.items():
                if interval != '':
                    tmp = arr[0].split('.')
                    d3 = datetime.date(day=int(tmp[0]), month=int(tmp[1]), year=int(tmp[2]))
                    if arr[int(name.lstrip('a'))] == value and d1 <= d3 <= d2:
                        i += 1
                else:
                    if arr[int(name.lstrip('a'))] == value:
                        i += 1
            if i == len(kwargs):
                # print(text[17] + ': ' + arr[17])
                ret.append(arr[17])
        return ret


    def show_me_money(reader):
        n531 = search(reader=reader, a7='531')  # запись номеров документов
        for e in n531:
            # print('1', e)
            f.seek(0)
            info = show(reader, str(e))
            # print(type(info), info)
            minus = 0
            suma = 0
            for i in info:
                if i[4] == 'ROH':
                    minus += float(i[11])
                else:
                    suma += float(i[11])
                dif = suma - minus
                m = []
                if dif < 0:
                    print('Убыток', -dif, 'в товародвижении:', i[17])
                    m.append(i[17])
        print(m)
                # else:
                #     print('Доход', dif, 'в товародвижении:', i[17])


    reader = csv.reader(f)
    # search(reader=reader, a0='30.09.2017', a9='1.800')
    # m = search(reader=reader, a17='4902915057')
    # f.seek(0)
    # m = m + search(reader=reader, interval='1.1.2016 2.1.2016', a7='531')
    # print('\n')


    show_me_money(reader=reader)


    # f.seek(0)
    # show(reader, list=n)
    # f.seek(0)
    # show(reader, list=m)
    # f.seek(0)
    # reader = csv.reader(f)
    # show(reader, '4906461659', '4906463289')

    def drawPlot(x, y, title=u'Мясные потери', xlabel='Недели', ylabel='Стоимость, руб'):
        line_plot = plt.plot(x, y, 'g,:')
        x_axis = max(x)
        y_axis = max(y)
        plt.axis([0, x_axis + 25, 0, y_axis + 25])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        # plt.legend((line_10), (u'Температура 10 \u00b0C'))
        plt.grid()
        plt.show()

        # drawPlot()
