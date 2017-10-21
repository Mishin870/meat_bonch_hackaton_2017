import matplotlib
import matplotlib.pyplot as plt

import pandas as pd

"""
This function draws a plot from x and y vectors same length
X = labels on X axis
Y = values on Y axis
copypasted and changed from test.py by Mishin870 :D
"""
def drawPlot(x, y, title=u'Мясные потери', xlabel='Недели', ylabel='Стоимость, руб'):
    # matplotlib.style.use('ggplot')
    line_plot = plt.plot(x, y, 'g,:')
    x_axis = max(x)
    y_axis = max(y)
    plt.axis([0, x_axis + 25, 0, y_axis + 25])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    #plt.legend((line_10), (u'Температура 10 \u00b0C'))
    plt.grid()
    plt.show()

# def testplot():
#     data = pd.read_csv('information.txt',sep="\t")
    # matplotlib.style.use('ggplot')
    # print(data.head())
    # ts = data.head()
    # ts = pd.Series(data.head())
    # print(ts)
    # ts = ts.cumsum()
    # ts['Код Вида Движения Материала'].plot()
    # print(ts['Код Вида Движения Материала'])
    # print(data.groupby('Код Вида Движения Материала'))

# testplot()

