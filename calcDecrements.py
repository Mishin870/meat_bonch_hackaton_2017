#модуль расчета потерь мяса по кодам товаров

def getDecrements(list):
    isDecr = False
    summ = 0
    prevSumm = 0
    for el in list:
        code = el[7]
        if code[0] == 'Z':
            continue
        code = int(code)
        if code == 261:
            prevSumm = int(el[12])
            isDecr = True
        elif code == 531 and isDecr == True:
            summ = summ + (int(el[12]) - prevSumm)
            isDecr = False
    return summ