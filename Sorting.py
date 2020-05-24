import random
import time
from matplotlib import pyplot as plt
import matplotlib.animation as animation


x=random.sample(range(1,101),100)
y=range(1,101)
plt.subplot(1,2,1)
plt.scatter(x,y)
plt.subplot(1,2,2)
x.sort()
plt.scatter(x,y)
plt.show()