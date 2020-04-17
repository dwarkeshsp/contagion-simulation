import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')


def plot(data):
    x = range(len(data[0]))
    plt.stackplot(x, data, labels=['sick', 'immune', 'healthy'])
    plt.xlabel('Time')
    plt.legend(loc='upper left')
    plt.show()
