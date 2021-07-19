from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd
import sys
import random

df = pd.read_csv(sys.argv[1]+'.csv', index_col=False, header=None)
note_numbers = list(df[0])

fig = plt.figure(facecolor='black', figsize=(9.6, 7.2))

X, Y = [], []


def plot(data):
    plt.cla()

    Y.append(note_numbers[data])
    X.append(len(Y))

    plt.plot(X, Y, color='white', linewidth=3)
    plt.xlim(0, len(note_numbers)-4)
    plt.ylim(0, max(note_numbers)*1.1)

    ax = plt.gca()
    ax.set_facecolor('black')
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)


ani = animation.FuncAnimation(
    fig, plot, frames=range(2, len(note_numbers)-3), interval=100)
ani.save('sample.mp4', writer='ffmpeg')
ani.save('sample.gif', writer='imagemagick')
