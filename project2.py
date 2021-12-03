# Normal derivative equations with non-constant R

from pylab import *
import matplotlib.pyplot as plt


s, i = meshgrid(arange(0, 100, 0.1), arange(0, 100, 0.1))

k = 30
b = 0.85
n = 3.1

r = ( b*(k**n) ) / ( (i**n) + (k**n) ) #transmission rate
y = 10 #tendency to enter r-state (recove/die, cannot pass on virus)

sDot = -r*s*i
iDot = (r*s*i) - (y*i)

streamplot(s, i, sDot, iDot)
plt.title("Relationship between Infected and Susceptible among the Population", fontsize = 12)
plt.xlabel("Number of Susceptible", fontsize = 10)
plt.ylabel("Number of Infected", fontsize = 10)
show()



