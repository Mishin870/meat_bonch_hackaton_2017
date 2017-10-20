import datetime

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
        print(hi + ' = ' + ii)
    print("===============================")

def processWeekItems(list):
    global headerItems
    days = len(list)
    if days == 0:
        return
    print("processing one week...")
    print("len = " + str(days))
    print("from: " + str(list[0][0]))
    print("to: " + str(list[days - 1][0]))
    i = 0
    for items in list:
        i = i + 1
        pass

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
        if i >= 200:
            break