import matplotlib.pyplot as plt

#сюда неделю нужную выбрать надо
X = [10.0, 40.0, 60.0, 80.0, 100.0]

#сюда занести данные по потерям
Y_10 = [10, 20 , 30, 40, 50]
# Y_20 = [0.96864, 0.93518, 0.89113, 0.84344, 0.78934]
# Y_30 = [0.96395, 0.92770, 0.88278, 0.83473, 0.78075]

# line_10, line_20, line_30 = plt.plot(X, Y_10, 'bD:', X, Y_20, 'r^:', X, Y_30, 'go:')
line_10 = plt.plot(X, Y_10, 'bD:')


x_axis = max(X)
y_axis = max(Y_10)
plt.axis([0, x_axis+25, 0, y_axis+25])

plt.title(u'Потери по мясу')

plt.xlabel(u'Недели')
plt.ylabel(u'Стоимость, руб')

#plt.legend( (line_10, line_20, line_30), (u'Температура 10 \u00b0C', u'Температура 20 \u00b0C', u'Температура 30 \u00b0C'), loc = 'best')
plt.legend( (line_10), (u'Температура 10 \u00b0C'))
plt.grid()

plt.show()