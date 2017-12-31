import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)

def draw():
    x = np.arange(-5.0, 5.0, 0.1)
    y = relu(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.savefig('output/ch03_relu.png')
    plt.gcf().clear()
