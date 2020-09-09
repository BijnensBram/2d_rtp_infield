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

data = np.loadtxt("rectangle.txt",comments="#",delimiter=";")
data100 = np.loadtxt("rectangle100.txt",comments="#",delimiter=";")
data0_1 = np.loadtxt("rectangle0_1.txt",comments="#",delimiter=";")
data0_3 = np.loadtxt("rectangle0_3.txt",comments="#",delimiter=";")
data0_5 = np.loadtxt("rectangle0_5.txt",comments="#",delimiter=";")
data0_7 = np.loadtxt("rectangle0_7.txt",comments="#",delimiter=";")
data1 = np.loadtxt("longhook.txt",comments="#",delimiter=";")
data2 = np.loadtxt("normal.txt",comments="#",delimiter=";")
data3 = np.loadtxt("0inverted.txt",comments="#",delimiter=";")
data4 = np.loadtxt("shorthook.txt",comments="#",delimiter=";")
# data5 = np.loadtxt("sym_rates.txt",comments="#",delimiter=";")
# plt.plot(data[:,0],data[:,1],marker=".",label="hook is left")
plt.plot(data0_1[:,0],data0_1[:,1],marker=".",label="hook=nx/2 a=0.1")
plt.plot(data0_3[:,0],data0_3[:,1],marker=".",label="hook=nx/2 a=0.3")
plt.plot(data0_5[:,0],data0_5[:,1],marker=".",label="hook=nx/2 a=0.5")
plt.plot(data[:,0],data[:,1],marker=".",label="hook=nx/2 a=1")
plt.plot(data100[:,0],data100[:,1],marker=".",label="hook=nx/2 a=1")
# plt.plot(data3[:,0],data3[:,1],marker=".",label="hook is left c=0")
# plt.plot(data4[:,0],data4[:,1],marker=".",label="hook=nx/4 a=1")
# plt.plot(data1[:,0],data1[:,1],marker=".",label="hook=3nx/4 a=1")
# plt.plot(data5[:,0],data5[:,1],marker=".",label="hook is symmetric")

plt.hlines(0,xmin=-1.5,xmax=1.5,colors="black")
plt.vlines(0,ymin=-0.3,ymax=0.3,colors="black")
plt.xlim([-1.5, 1.5])
plt.ylim([-0.3, 0.3])
plt.legend()
plt.xlabel(r"$\epsilon$")
plt.ylabel(r"j")
plt.savefig("comp_lefthook_righthook.png",dpi=190)
plt.show()
