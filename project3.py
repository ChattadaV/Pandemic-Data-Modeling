# Different derivative equations with constant R

from pylab import *
import matplotlib.pyplot as plt

#s and i in meshgrid with range from -10 to 100 at step increment of 0.1
s, i = meshgrid(arange(0, 100, 0.1), arange(0, 100, 0.1))

#constant values
r = 0.02 #transmission rate
y = 0.2 #tendency to enter r-state (recove/die, cannot pass on virus)

m = 1/75
n = 1000

#derivative equations (streamline)
sDot = (((-r * i * s) / n) + m - ((m * s) / n))
iDot = ((r * s * i) / n) - ((y + m) * (i / n))

#plot
streamplot(s, i, sDot, iDot)
plt.title("Infected-Susceptible among Population with Constant R", fontsize = 12)
plt.xlabel("Number of Susceptible", fontsize = 10)
plt.ylabel("Number of Infected", fontsize = 10)
show()