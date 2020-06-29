import random as r
import itertools
import matplotlib.pyplot as plt

colors = itertools.cycle(['red', 'green', 'orange', 'purple',
                          'black', 'blue', 'pink', 'grey', 'yellow', 'cyan'])

markers = itertools.cycle(['.', 's'])


def randPOS():
    return r.randint(1000, 9999) / 100, r.randint(1000, 9999) / 100


def randVACANCY():
    return r.randint(3, 20)


def is_unique(locatable, reference):
    return True if locatable.pos not in reference else False


def plot_points(locatables, title, m):
    x = []
    y = []
    for l in locatables:
        x.append(l.x)
        y.append(l.y)
    plt.scatter(x, y, marker=m)
    plt.title(title)
    plt.show()


def connect(connections):
    for pri, secondary in connections:
        color = next(colors)
        plt.scatter(pri.x, pri.y, marker='s', color=color)
        for sec in secondary:
            plt.scatter(sec.x, sec.y, marker='.', color=color)
            plt.arrow(pri.x, pri.y, sec.x - pri.x, sec.y - pri.y, color=color)
            
            
