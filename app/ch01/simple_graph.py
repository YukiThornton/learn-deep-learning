import numpy as np
import matplotlib.pyplot as plt

def show():
    x = np.arange(-6, 12, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.savefig('output/plot.png')
