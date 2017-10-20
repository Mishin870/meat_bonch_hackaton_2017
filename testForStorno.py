"""
Функция выводит одну строку таблицы в красивом виде
headerItems - это заголовки столбцов
"""
def printItem(headerItems, items):
    print("===============================")
    for hi, ii in zip(headerItems, items):
        if hi == "\n" or ii == "\n":
            break;
        print(hi + ' = ' + ii)
    print("===============================")

with open("input.csv", encoding='UTF-8') as f:
    iterlines = iter(f)
    header = next(iterlines)
    headerItems = header.split("\t")
    for line in iterlines:
        items = line.split("\t")
        #код движения
        if items[7][0] == 'Z':
            continue
        move = int(items[7])
        if move == 962:
            printItem(headerItems, items)
            print("предыдущее:")
            printItem(headerItems, prevItems)
            break
        prevItems = items