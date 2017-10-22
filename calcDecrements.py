<<<<<<< HEAD
# модуль расчета потерь мяса по кодам товаров

def getDecrements(list):
    OPEN_CODE = 261
    CLOSE_CODE = 531
    OPEN_STORNO = 262
    CLOSE_STORNO = 532
    PORCHA_CODE1 = 950
    PORCHA_CODE2 = 951
    PORCHA_CODE3 = 952

    # STORNO_PORCHA = 'Z50', 'Z51'
    isOpen = False
    # summ = 0
    #prevSumm = 0
    #i = -1

    sum = 0
    infos = []
    obj = [sum, infos]
=======
#модуль расчета потерь мяса по кодам товаров

def getDecrements(list):
    isDecr = False
    summ = 0
    prevSumm = 0
>>>>>>> eee275df2d5df4f882159dc88cef5bf98f344deb
    for el in list:
        code = el[7]
        if code[0] == 'Z':
            continue
<<<<<<< HEAD

        code = int(code)
        val = float(el[11].replace(',', '.'))
        if code == OPEN_CODE:
            sum += val
            infos.append(el)
        elif code == OPEN_STORNO:
            sum -= val
            infos.append(el)
        elif code == CLOSE_CODE:
            sum -= val
            infos.append(el)
        elif code == CLOSE_STORNO:
            sum += val
            infos.append(el)
        # elif code == PORCHA_CODE1 or PORCHA_CODE2 or PORCHA_CODE3:
        #     sum -= val
        #    infos.append(el)
    obj[0] = sum
    obj[1] = infos
    return obj
        # i = i + 1
        # code = el[7]
        # if code[0] == 'Z':
        #     continue
        # code = int(code)
        # val = float(el[12].replace(',', '.'))
        #
        # try:
        #     nextEl = list[i + 1]
        # except:
        #     nextEl = None
        # nextCode = nextEl[7]
        # if nextCode[0] == 'Z':
        #     nextCode = -1
        # else:
        #     nextCode = int(nextCode)
        #
        # if code == OPEN_CODE and nextCode != OPEN_STORNO:
        #     pass

        # if code == 261:
        #     try:
        #         tmp = list[i + 1]
        #         if tmpCode[0] == 'Z':
        #             pass
        #         tmpCode = tmp[12].replace(",", ".")
        #     except:
        #         pass
        #     prevSumm = val
        #     isDecr = True
        # elif code == 531 and isDecr == True:
        #     summ += val - prevSumm
        #     isDecr = False
        # i += 1
    # return summ
=======
        code = int(code)
        if code == 261:
            prevSumm = int(el[12])
            isDecr = True
        elif code == 531 and isDecr == True:
            summ = summ + (int(el[12]) - prevSumm)
            isDecr = False
    return summ
>>>>>>> eee275df2d5df4f882159dc88cef5bf98f344deb
