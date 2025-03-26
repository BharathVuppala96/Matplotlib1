import numpy as np
from matplotlib import pyplot as plt


x = [1,2,3]
y = [0,1,0]
z = [1,0,1]
fig,ax = plt.subplots(2)
ax[0].plot(x,y)
ax[1].plot(x,z)
ax[0].set_xlabel('X1')
ax[0].set_ylabel('Y1')
ax[1].set_xlabel('X2')
ax[1].set_ylabel('Z')
ax[0].set_title('X VS Y')
ax[1].set_title('X vs Z')
plt.tight_layout()
plt.show()




x = np.arange(0.0 , 2.0 , 0.01)
y = 1 + np.sin(2*np.pi * x)
# fig , ((ax1 , ax2) , (ax3, ax4) ,(ax5,ax6)) = plt.subplots(3,2)
fig , ((ax1 , ax4,ax3),(ax2,ax5,ax6)) = plt.subplots(2,3)
# ax1 = plt.axes([0.1,0.9,1,1])
ax1.plot(x, y , color = 'orange')
ax2.plot(x,y , color = 'red')
ax3.plot(x , y , color = 'blue')
ax4.plot(x , y , color = 'g')
ax5.plot(x , y , color = 'magenta')
ax6.plot(x , y , color = 'black')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
plt.tight_layout()
plt.show()