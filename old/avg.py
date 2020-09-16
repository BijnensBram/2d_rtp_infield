import numpy as np
import matplotlib.pyplot as plt

c1 = np.loadtxt("c=1_0.txt", comments="#",delimiter=";")
a20 = np.loadtxt("a=20_0.txt", comments="#",delimiter=";")
a30 = np.loadtxt("a=30_0.txt", comments="#",delimiter=";")
c1_5 = np.loadtxt("c=1_5_0.txt", comments="#",delimiter=";")
print(c1)
for i in range(1,20):
    c1 += np.loadtxt("c=1_"+str(i)+".txt", comments="#",delimiter=";")
    a20 += np.loadtxt("a=20_"+str(i)+".txt", comments="#",delimiter=";")
    a30 += np.loadtxt("a=30_"+str(i)+".txt", comments="#",delimiter=";")
    c1_5 += np.loadtxt("c=1_5_"+str(i)+".txt", comments="#",delimiter=";")
    # pulselin += np.loadtxt("./datafinal/pulsegradient/"+str(i)+".txt", comments="#",delimiter=";")

c1 = c1/20
a20 = a20/20
c1_5 = c1_5/20
# pulselin = pulselin/20

print(c1)

plt.plot(c1[:,0],c1[:,1],label=r"c=1",marker=".")
plt.plot(c1_5[:,0],c1_5[:,1],label=r"c=1.5",marker=".")
plt.plot(a20[:,0],a20[:,1],label=r"a=20",marker=".")
plt.plot(a30[:,0],a30[:,1],label=r"a=30",marker=".")
plt.legend()
plt.show()
# # plt.plot(x,pulselin[int(i),:],label=r"$a(x)=ax$")
# # plt.ylim([0,500])
# plt.savefig("./current/jvse"+str(int(i))+".png",dpi=190)
# plt.close()
