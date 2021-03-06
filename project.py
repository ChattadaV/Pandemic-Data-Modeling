# Normal derivative equations with constant R

from pylab import *
import matplotlib.pyplot as plt

#s and i in meshgrid with range from 0 to 100 at step increment of 0.1
s, i = meshgrid(arange(0, 100, 0.1), arange(0, 100, 0.1))

#constant values
r = 0.02 #transmission rate
y = 0.2 #tendency to enter r-state (recove/die, cannot pass on virus)

#derivative equations (streamline)
sDot = -r*s*i
iDot = r*s*i-y*i

#plot
streamplot(s, i, sDot, iDot)
plt.title("Relationship between Infected and Susceptible among the Population", fontsize = 12)
plt.xlabel("Number of Susceptible", fontsize = 10)
plt.ylabel("Number of Infected", fontsize = 10)
show()