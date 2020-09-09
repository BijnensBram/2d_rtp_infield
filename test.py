import matplotlib.pyplot as plt
import numpy as np

x,y,count = np.loadtxt("test.txt",comments="#",delimiter=";",unpack=True)

for i in range(int(9*len(x)/10),len(x)):
    plt.scatter(x[i],y[i])
    plt.xlim([0,10])
    plt.ylim([0,10])
    plt.title(count[i])
    plt.savefig("./fig/"+str(i)+".png",dpi=190)
    plt.close()
