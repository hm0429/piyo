import numpy as np
import matplotlib.pylab as mpl

def relu_function(x):
	return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu_function(x)
mpl.plot(x, y)
mpl.ylim(-1, 5.5)
mpl.show()
