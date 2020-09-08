import numpy as np
import matplotlib.pyplot as plt
import time

for t in np.linspace(1,4000,301):
    for i in np.linspace(0,10,11):
        data = np.loadtxt("traject"+str(int(i))+".txt",comments="#",delimiter=";")
        plt.xlim([-1,11])
        plt.ylim([-1,11])
        plt.plot(data[int(t)-1:int(t)+1,0],data[int(t)-1:int(t)+1,1],marker=".",label="c="+str(round(i,2)))
        plt.hlines(y=5.5,xmin=5.5,xmax=10.5,color="red")
        plt.hlines(y=5.5,xmin=-0.5,xmax=-1,color="red")
        plt.hlines(y=0,xmin=0,xmax=10,color="black")
        plt.hlines(y=10,xmin=0,xmax=10,color="black")
        plt.vlines(x=10.5,ymin=0,ymax=5.5,color="red")
        plt.vlines(x=-0.5,ymin=0,ymax=5.5,color="red")
        plt.vlines(x=0,ymin=0,ymax=10,color="black")
        plt.vlines(x=10,ymin=0,ymax=10,color="black")
    plt.savefig("./fig/"+str(int(t))+".png",dpi=190)
    plt.close()
