import matplotlib.pyplot as plt
import numpy as np
x=np.arange(12,20)
y=10*x+14
plt.title("Graph")
plt.xlabel("X axis")
plt.ylabel("y axis")
plt.plot(x,y)
plt.show()