import numpy

from matplotlib import pyplot as plt
from scipy.optimize import rosen

x = numpy.arange(-1, 3, .01)
X, Y = numpy.meshgrid(x, x)

z = rosen((X, Y))
plt.pcolormesh(X, Y, z, norm='log', vmin=1e-3)
c = plt.colorbar()
plt.show()
