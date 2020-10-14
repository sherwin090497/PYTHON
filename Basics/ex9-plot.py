
from matplotlib import pyplot as plt 
import math as math
from numpy import arange as arange

x = [i for i in arange(0,2 *math.pi, .1)]
y = [ math.sin(p) for p in x]
plt.plot(x, y)
plt.show()
print("Complete")