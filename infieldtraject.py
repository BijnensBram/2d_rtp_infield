import numpy as np
import matplotlib.pyplot as plt
import time

# for i in np.linspace(0.1,1,10):
#     data = np.loadtxt("a="+str(round(i,2))+".txt",comments="#",delimiter=";")
#     plt.plot(data[:,0],data[:,1],marker=".",label="a="+str(round(i,2)))

# plt.legend(ncol=2)
# plt.savefig("a=0-1.png",dpi=190)
# plt.show()
    
# for i in np.linspace(0.1,1,10):
#     data = np.loadtxt("c="+str(round(i,2))+".txt",comments="#",delimiter=";")
#     plt.plot(data[:,0],data[:,1],marker=".",label="c="+str(round(i,2)))

# plt.legend(ncol=2)
# plt.savefig("c=0-1.png",dpi=190)
# plt.show()

# for i in np.linspace(0.1,1,10):
#     # data = np.loadtxt("c="+str(round(i,2))+".txt",comments="#",delimiter=";")
#     data2 = np.loadtxt("passive_c="+str(round(i,2))+".txt",comments="#",delimiter=";")
#     # plt.plot(data[:,0],data[:,1],marker=".",label="c="+str(round(i,2)))
#     plt.plot(data2[:,0],data2[:,1],marker=".",label="passive c="+str(round(i,2)))

# plt.legend(ncol=2)
# plt.savefig("pasc=0-1.png",dpi=190)
# plt.show()

# for i in np.linspace(0.5,1.5,3):
#     data = np.loadtxt("no_neg_c="+str(round(i,2))+".txt",comments="#",delimiter=";")
#     plt.plot(data[:,0],data[:,1],marker=".",label="c="+str(round(i,2)))

# plt.hlines(0,xmin=-0.01,xmax=1,colors="black")
# plt.vlines(0,ymin=-0.0,ymax=0.5,colors="black")
# plt.xlim([-0.1, 0.1])
# plt.ylim([-0.1, 0.1])
# plt.legend(ncol=2)
# plt.savefig("negc_no_obstacle.png",dpi=190)
# plt.show()

# for i in np.linspace(0.5,1.5,3):
#     data = np.loadtxt("neg_c="+str(round(i,2))+".txt",comments="#",delimiter=";")
#     plt.plot(data[:,0],data[:,1],marker=".",label="c="+str(round(i,2)))

# plt.hlines(0,xmin=-0.01,xmax=1,colors="black")
# plt.vlines(0,ymin=-0.0,ymax=0.5,colors="black")
# plt.xlim([-0.01, 1])
# plt.ylim([-0.01, 0.12])
# plt.legend(ncol=2)
# plt.savefig("negc_obstacle.png",dpi=190)
# plt.show()

# for i in np.linspace(0.1,1,10):
#     data = np.loadtxt("noa="+str(round(i,2))+".txt",comments="#",delimiter=";")
#     plt.plot(data[:,0],data[:,1],marker=".",label="c="+str(round(i,2)))

# plt.legend(ncol=2)
# plt.savefig("noc=0-1.png",dpi=190)
# plt.show()

# data = np.loadtxt("onelane.txt",comments="#",delimiter=";")
# data1 = np.loadtxt("onelane1.txt",comments="#",delimiter=";")
# plt.plot(data[:,0],data[:,1],marker=".")
# plt.plot(data1[:,0],data1[:,1],marker=".")
# plt.xlim([-0,1])
# plt.ylim([-0.1,1])
# plt.hlines(0,xmin=-1,xmax=1,colors="black")
# plt.vlines(0,ymin=-1,ymax=1,colors="black")
# plt.savefig("noc=0-1.png",dpi=190)
# plt.show()

data = np.loadtxt("inverted.txt",comments="#",delimiter=";")
plt.plot(data[:,0],data[:,1],marker=".")

plt.hlines(0,xmin=-0.01,xmax=1,colors="black")
plt.vlines(0,ymin=-0.0,ymax=0.5,colors="black")
# plt.xlim([-0.1, 0.1])
# plt.ylim([-0.1, 0.1])
plt.legend(ncol=2)
plt.savefig("symrates.png",dpi=190)
plt.show()
