import numpy as np
from matplotlib import pyplot as plt
x=np.linspace(-np.pi,np.pi,15)
C=np.cos(x)
S=np.sin(x)
ax=plt.axes([0.1,0.1,0.9,0.9])
ax1=ax.plot(x,C,'bs:')
ax2=ax.plot(x,S,'oc-')
ax.legend(labels=('Cosine Func','Sine Func'),loc='upper left')
ax.set_title('Triginometry Functions')
plt.show()