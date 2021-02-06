import matplotlib.pyplot as plt 
from plot import plot

obj = plot()

x = [1, 2, 4]
y =[2, 34, 56]
obj.scatter(plt, x, y, 'legend-1')
x = [1, 12, 14]
y =[21, 54, 56]
obj.scatter(plt, x, y,  'legend-2')

