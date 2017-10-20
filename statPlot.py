import matplotlib.pyplot as plt

"""
This function draws a plot from x and y vectors same length
X = labels on X axis
Y = values on Y axis
copypasted and changed from test.py by Mishin870 :D
"""
def drawPlot(x, y, title=u'Мясные потери', xlabel='Недели', ylabel='Стоимость, руб'):
    line_plot = plt.plot(x, y, 'bD:')
    x_axis = max(x)
    y_axis = max(y)
    plt.axis([0, x_axis + 25, 0, y_axis + 25])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    #plt.legend((line_10), (u'Температура 10 \u00b0C'))
    plt.grid()
    plt.show()