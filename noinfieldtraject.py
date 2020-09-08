import numpy as np
import matplotlib.pyplot as plt
import time

data = np.loadtxt("noa=10.txt",comments="#",delimiter=";")
data2 = np.loadtxt("noa=1000.txt",comments="#",delimiter=";")
# data4 = np.loadtxt("4rates4.txt",comments="#",delimiter=";")

# plt.figure()
# for i in np.linspace(0,500,101):
#     # plt.scatter(data[int(i),0],data[int(i),1])
#     # plt.scatter(data2[0:int(i),0],data2[0:int(i),1])
#     plt.scatter(data3[int(i),0],data3[int(i),1])
#     # plt.scatter(data4[0:int(i),0],data4[0:int(i),1])
#     plt.xlim([0,6])
#     plt.ylim([0,6])
#     # plt.vlines(100,0,50)
#     # plt.savefig(str(int(i))+"png",dpi=190)
#     plt.show()
   
plt.title("dt=0.01, c=1")
plt.plot(data[:,0],data[:,1],marker=".",label="a=10")
plt.plot(data2[:,0],data2[:,1],marker=".",label="a=1000")
plt.legend()
plt.savefig("no_obstacle.png",dpi=190)
plt.show()
