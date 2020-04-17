import matplotlib.pyplot as plt


def plot(data):
    x = range(len(data[0]))
    plt.stackplot(x, data, labels=['sick', 'immune', 'healthy'], colors=[
                  'orange', 'blue', 'green'])
    plt.xlabel('Time')
    plt.legend(loc='upper left')
    plt.show()
