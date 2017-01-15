#Learning 3D visualization

data = []
with open("C:\Users\...biodata.txt") as protein:
    for lines in protein:
        if "ATOM   " in lines:
            lines = lines.split()
            data.append(map(float, lines[6:9]))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x,y,z = zip(*data)

fig = plt.figure()
ax = Axes3D(fig)

ax.plot(x,y,z, "o")
ax.axis("off")

plt.show()
