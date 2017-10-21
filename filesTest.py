import datetime, db, statPlot

"""
Функция выводит одну строку таблицы в красивом виде
headerItems - это заголовки столбцов
"""
def printItem(items):
    global headerItems
    print("===============================")
    for hi, ii in zip(headerItems, items):
        if hi == "\n" or ii == "\n":
            break
        print(hi + ' = ' + str(ii))
    print("===============================")

with open("db.csv", encoding='UTF-8') as f:
    iterlines = iter(f)
    header = next(iterlines)
    headerItems = header.split("\t")
    i = 0

    for line in iterlines:
        items = line.split("\t")
        open("files/" + str(items[17]), "a+", encoding='UTF-8').write(line)
        #f.write("\t".join(items))