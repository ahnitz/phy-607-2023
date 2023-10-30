import h5py
from matplotlib import pyplot as plt

f = h5py.File('./data.hdf', 'r')

print(f.keys())

print(f['data'].keys())

xpos = f['data/xpos'][:]
ypos = f['data/ypos'][:]

plt.scatter(xpos, ypos)
plt.show()
