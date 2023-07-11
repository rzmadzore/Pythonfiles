import matplotlib.pyplot as plt
import numpy as np
from numpy import random
from random import random 
import matplotlib.pyplot as plt
import scipy as sp 

def f(x):
    return (x-3)**2 

def g(x):
    return (x)**3 -3*x +6 
def zero(x):
    return 0 



x1= np.linspace(-2*np.pi,2*np.pi,66)
y1 = np.sin(x1)  
plt.title('Trig Graph',fontdict={'fontsize':20})
plt.xlabel('x')
plt.ylabel('y')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.plot(x1,y1)
plt.show()

