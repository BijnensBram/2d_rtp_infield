import matplotlib.pyplot as plt
import numpy as np

x,y = np.loadtxt("test.txt",comments="#",delimiter=";",unpack=True)

# for i in np.linspace(0,len(x),201):
#     plt.plot(x[0:int(i)],y[0:int(i)])
#     plt.xlim([0,11])
#     plt.ylim([0,11])
#     plt.show()

plt.plot(x,y)
plt.show()
