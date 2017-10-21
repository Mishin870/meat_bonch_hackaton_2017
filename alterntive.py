import datetime, db, statPlot
#ALTERNATIVE SOLUTION BY Mishin870
import matplotlib

"""
Функция выводит одну строку таблицы в красивом виде
headerItems - это заголовки столбцов
"""
def printItem(items):
    global headerItems
    print("===============================")
    for hi, ii in zip(headerItems, items):
        if hi == "\n" or ii == "\n":
            break;
        print(hi + ' = ' + str(ii))
    print("===============================")

"""
Эта функция обрабатывает список элементов, принадлежащих одной неделе
"""
def processWeekItems(list, week):
    global headerItems, weekLabels, weekStat
    days = len(list)
    #костыль (изначально неделя = -1, чтобы не было лишних обработок. записей ведь 2 млн, а эту функция запускается в 100 раз реже)
    #и на будущее. вдруг что-то случится и в неделе станет 0 дней
    if days == 0:
        return

    #если нужны статы по неделе
    #print("processing one week...")
    #import sys
    #print("len = " + str(days))
    #print("from: " + str(list[0][0]))
    #print("to: " + str(list[days - 1][0]))

    i = 0
    iterList = iter(list)

    summ = 0
    for items in iterList:
        #проверяем на сторность только тогда, когда это не последний элемент списка
        if i < days - 1:
            nextCode = list[i + 1][7]
            #проверка на сторность (два варианта - номер символьный с Z и номер числовой)
            if nextCode[0] == 'Z':
                if nextCode in db.stornoSym:
                    #print("nextCode (" + str(nextCode) + ") in stornoSym!")
                    i = i + 2
                    next(iterList)
                    continue
            else:
                nextCode = int(nextCode)
                if nextCode in db.stornoNum:
                    #print("nextCode (" + str(nextCode) + ") in stornoNum!")
                    i = i + 2
                    next(iterList)
                    continue
        #if int(items[14]) in db.errorShops or int(items[7]) in db.errors:
            #continue
        i = i + 1
        if int(items[14]) in db.errorShops:
            continue
        if items[7][0] != 'Z':
            if int(items[7]) in db.incrOps:
                check = float(items[12].replace(",", "."))
                if check != 0:
                    average = float(items[11].replace(",", "."))
                    summ = summ + (check - average)
            if int(items[7]) in db.decrOps:
                check = float(items[12].replace(",", "."))
                if check != 0:
                    average = float(items[11].replace(",", "."))
                    summ = summ - (check - average)

    # weekLabels.append(len(weekLabels))
    weekLabels.append(len(weekLabels))
    weekStat.append(summ)

headerItems = []
weekLabels = []
weekStat = []

with open("db.csv", encoding='UTF-8') as f:
    iterlines = iter(f)
    header = next(iterlines)
    headerItems = header.split("\t")
    i = 0
    prevWeek = -1
    weekList = []

    dvizh = []
    for line in iterlines:
        items = line.split("\t")
        #парсим дату на составляющие
        date = items[0].split('.')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])

        # dvizh = []
        tovaro_dvizh = items[17]
        dvizh.append(tovaro_dvizh)
        #На случай если нужно будет что-то сделать с уже распаршенной датой
        items[0] = date
        #получаем номер недели по календарю (числа могут быть неожиданными, но верными)
        week = datetime.date(year, month, day).isocalendar()[1]
        if week != prevWeek:
            #если неделя кончилась, то обрабатываем предыдущую неделю, очищаем и продолжаем
            processWeekItems(weekList, prevWeek)
            weekList = []
            prevWeek = week
        weekList.append(items)
        #это просто предохранитель для тестов
        i = i + 1
        #if i >= 500000:
            #break
    # statPlot.drawPlot(weekLabels, weekStat, title='Недельная прибыль', xlabel='Недели', ylabel='Прибыль, руб')
    print(dvizh)