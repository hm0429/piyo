import numpy as np
import matplotlib.pylab as mpl

def step_function(x):
	return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
mpl.plot(x, y)
mpl.ylim(-0.1, 1.1)
mpl.show()
