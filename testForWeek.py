import datetime, db

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

def processWeekItems(list):
    global headerItems
    days = len(list)
    if days == 0:
        return

    #print("processing one week...")
    #print("len = " + str(days))
    #print("from: " + str(list[0][0]))
    #print("to: " + str(list[days - 1][0]))

    i = 0
    iterList = iter(list)

    summ = 0
    for items in iterList:
        if i < days - 1:
            nextCode = list[i + 1][7]
            #проверка на сторность
            if nextCode[0] == 'Z':
                if nextCode in db.stornoSym:
                    print("nextCode (" + str(nextCode) + ") in stornoSym!")
                    i = i + 1
                    next(iterList)
                    continue
            else:
                nextCode = int(nextCode)
                if nextCode in db.stornoNum:
                    print("nextCode (" + str(nextCode) + ") in stornoNum!")
                    i = i + 1
                    next(iterList)
        #incr = float(items[12]) - float(items[11])
        #print(incr)
        #summ = summ + incr
        i = i + 1

headerItems = []

with open("input.csv", encoding='UTF-8') as f:
    iterlines = iter(f)
    header = next(iterlines)
    headerItems = header.split("\t")
    i = 0
    prevWeek = -1
    weekList = []
    for line in iterlines:
        items = line.split("\t")
        date = items[0].split('.')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        #На случай если нужно будет что-то сделать с уже распаршенной датой
        items[0] = date
        week = datetime.date(year, month, day).isocalendar()[1]
        if week != prevWeek:
            processWeekItems(weekList)
            weekList = []
            prevWeek = week
        weekList.append(items)
        i = i + 1
        if i >= 5000:
            break