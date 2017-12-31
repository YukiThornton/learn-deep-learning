import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    # if x > 0:
    #     return 1
    # else:
    #     return 0
    y = x > 0
    return y.astype(np.int)

def draw():
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.savefig('output/ch03_step_function.png')
    plt.gcf().clear()
