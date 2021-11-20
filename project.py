from pylab import *
import matplotlib.pyplot as plt

#x and y axis from 0 to 100 at 0.1 step increment
s, i = meshgrid(arange(0, 100, 0.1), arange(0, 100, 0.1))

r = 1 #transmission rate
y = 5 #tendency to enter r-state (recover/die, cannot pass on virus)

#derivative equations
sDot = -r*s*i
iDot = r*s*i-y*i

streamplot(s, i, sDot, iDot)
show()
