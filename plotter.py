import matplotlib.pyplot as plt
import numpy as np

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')


def plotter(x_vec, people, sick_data, sick_line, identifier='', pause_time=0.1):

    if sick_line == []:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        sick_line, = ax.plot(x_vec, sick_data, '-o', alpha=0.8)
        # update plot label/title
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()

    # after the figure, axis, and line are created, we only need to update the y-data
    sick_line.set_ydata(sick_data)
    # adjust limits if new data goes beyond bounds
    if np.min(sick_data) <= sick_line.axes.get_ylim()[0] or np.max(sick_data) >= sick_line.axes.get_ylim()[1]:
        plt.ylim([np.min(sick_data)-np.std(sick_data),
                  np.max(sick_data)+np.std(sick_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    # plt.pause(pause_time)

    # return line so we can update it again in the next iteration
    return sick_line
