import matplotlib.pyplot as plot
import numpy
import scipy.stats as scipy

def graph_bauen():

    punkte = []
    graph = []
    for g in range(-20, 100):
        if abs(g - 40) > 40:
            punkte.append(g)
            graph.append(4)

        elif abs(g - 40) > 30:
            punkte.append(g)
            graph.append(3)

        elif abs(g - 40) > 20:
            punkte.append(g)
            graph.append(2)

        else:
            punkte.append(g)
            graph.append(1)

    fig_hilfsgraph = plot.figure()
    ax_hilfsgraph = fig_hilfsgraph.add_subplot(1, 1, 1)

    ax_hilfsgraph.set_xlim([-20, 100])
    ax_hilfsgraph.set_ylim([0, 5])

    ax_hilfsgraph.plot(punkte, graph)


def graph_bauen_2():

    x = numpy.arange(-20, 100, 1)
    y = scipy.norm.pdf(x, 40,15)
    y_2 = scipy.norm.pdf(x, 40,7.5)
    y_3 = scipy.norm.pdf(x, 40,3.75)

    fig = plot.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(x, y, color='r', label='Alter = 40')
    ax.plot(x, y_2, color='g', label='Alter = 20 bzw. 60')
    ax.plot(x, y_3, color='b', label='Alter = 10 bzw. 70')

    #ax.set_xlabel("Alter")
    ax.set_ylabel("Warscheinlichkeit")

    plot.legend()

    #fig = plot.figure()
    #ax_1 = fig.add_subplot(1, 2, 1)  # x,y,z heißt x*y großes feld, z'ter subplot
    #ax_2 = fig.add_subplot(1, 2, 2)
    #ax_1.plot(x,y)
    #ax_2.plot(x, y_2)
