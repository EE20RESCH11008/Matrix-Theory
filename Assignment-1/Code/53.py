# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
# Create the vectors X and Y
x1 = np.linspace(-5,5,300)
y1 = (4-x1)

x2 = np.linspace(-5,5,300)
y2 = (6 + 4*x2)


P1= np.array([4, 0])
Q1 = np.array([0, 4])

P2= np.array([-1.5, 0])
Q2 = np.array([0, 6])



# Create the plot
plt.plot(x1,y1,label='x+y=4')
plt.plot(x2,y2,label='4x-y=-6')


plt.plot(P1[0],P1[1],'o')
plt.text(P1[0]*(1+0.1), P1[1]*(1-0.1), 'P1')
plt.plot(Q1[0],Q1[1],'o')
plt.text(Q1[0]*(1-0.2), Q1[1]*(1), 'Q1')

plt.plot(P2[0],P2[1],'o')
plt.text(P2[0]*(1+0.1), P2[1]*(1-0.1), 'P2')
plt.plot(Q2[0],Q2[1],'o')
plt.text(Q2[0]*(1-0.2), Q2[1]*(1), 'Q2')



# Add a title
plt.title('lines and planes ')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')

# Add a Legend
plt.legend()
#plt.savefig('../figures/line/lines_and_planes/lines_and_planes.eps')
# Show the plot
plt.show()