from pylab import *
import matplotlib.pyplot as plt

# x and y axis from 0 to 100 at 0.1 step increment
s, i = meshgrid(arange(0, 100, 0.1), arange(0, 100, 0.1))

r = 1 # Transmission rate
y = 5 # Tendency to enter r-state (recover/die, cannot pass on virus)

# Derivative equations
sDot = -r*s*i
iDot = r*s*i-y*i

# Plot both  normal and derivative equations
streamplot(s, i, sDot, iDot)
show()
