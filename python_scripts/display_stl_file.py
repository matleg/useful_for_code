import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import time

cwd = os.getcwd()
print(cwd)
listfi = os.listdir(cwd)

t0 = time.ctime()
print(t0)

listMarkers = ['|', 'o', 'v', '^', '<', '>', '1', '2',
               '3', '4', 's', 'p', 'h', '+', 'H', '*', 'x', 'D', 'd']
listColors = ["b", "g", "r", "c", "m", "y", "k"]  # "w" #white not added

with open('pont.stl', 'r') as fifi:
    lines = fifi.readlines()

triangles = []
vertices = []
triangle = []
tri = 0

for l in lines:
    l = l[:-1]
    if 'vertex' in l:
        tri += 1
        l = l.split()
        x, y, z = [float(i) for i in [l[-3], l[-2], l[-1]]]
        vertices.append((x, y, z))
        triangle.append((x, y, z))
        if tri % 3 == 0:
            triangles.append(triangle)
            triangle = []

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

x = [p[0] for p in vertices]
y = [p[1] for p in vertices]
z = [p[2] for p in vertices]

ax.plot(x, y, z, 'bo')

plt.show()
