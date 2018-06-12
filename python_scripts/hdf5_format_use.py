# -*- coding: utf-8 -*-
"""

hdf5 tutorial
example from uetke.com

"""

import h5py
import numpy as np

arr = np.random.randn(1000)

with h5py.File('random.hdf5', 'w') as f:
    dset = f.create_dataset("default", data=arr)

with h5py.File('random.hdf5', 'r') as f:
    data = f['default']
    print(min(data))
    print(max(data))
    print(data[:15])

# code that raises an error
f = h5py.File('random.hdf5', 'r')
data = f['default']
f.close()
try:
    print(data[1])  # ValueError: Not a dataset (Not a dataset)
except Exception as e:
    print(e, " !!!!!!!  error raised")
# No more access to dataset. file closed. f['default'] generates a pointer to data on hard drive.

# code that works
f = h5py.File('random.hdf5', 'r')
data = f['default'][:]
f.close()
print(data[10])
