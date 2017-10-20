import matplotlib.pyplot as plt

def drawPlot(x, y, title=u'Мясные потери', xlabel='Недели', ylabel='Стоимость, руб'):
    #line_10 = plt.plot(x, y, 'bD:')

    x_axis = max(x)
    y_axis = max(y)
    plt.axis([0, x_axis + 25, 0, y_axis + 25])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    #plt.legend((line_10), (u'Температура 10 \u00b0C'))
    plt.grid()
    plt.show()