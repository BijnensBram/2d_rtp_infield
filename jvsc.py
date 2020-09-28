import numpy as np
import matplotlib.pyplot as plt

marker = [".","v","^","s","D","o"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]

j=0
for i in [0.5,0.6,0.7,0.8,0.9,1.0]:
    right = np.loadtxt("c_right_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"$c$="+str(round(i,2)))
    j+=1
    if j > 5:
        j=0

plt.legend(ncol=2,frameon=False,loc="lower right")
plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=3,colors="black",linewidth=1)
# plt.xlim([0,10])
# plt.ylim([-500,2500])
plt.savefig("discrete_righthook_results_c.pdf")
plt.show()

# j=0
# for i in [0.5,1.0,1.5,2.0,2.5,3.0,4.0,5.0]:
#     right = np.loadtxt("2c_right_"+str(round(i,2))+".txt",comments="#",delimiter=";")

#     plt.rc('text', usetex=True)
#     plt.rc('font', family='serif',size=14)
    
#     plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"$c$="+str(round(i,2)))
#     j+=1
#     if j > 5:
#         j=0

# plt.legend(ncol=2,frameon=False,loc="lower right")
# plt.xlabel(r"$\epsilon$")
# h=plt.ylabel("j")
# h.set_rotation(0)
# plt.hlines(y=0,xmin=0,xmax=3,colors="black",linewidth=1)
# # plt.xlim([0,10])
# # plt.ylim([-500,2500])
# plt.savefig("2discrete_righthook_results_c.pdf")
# plt.show()

j=0

right = np.loadtxt("4c_right_0.05.txt",comments="#",delimiter=";")
plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"$c$="+str(round(i,2)))
j+=1

c1 = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
c2 = [1.0,2.0,3.0,4.0,5.0]

for i in c1:
    right = np.loadtxt("3c_right_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],2*right[:,1],marker=marker[j],markersize=3,label=r"$c$="+str(round(i,2)))
    j+=1
    if j > 5:
        j=0

for i in c2:
    right = np.loadtxt("4c_right_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"$c$="+str(round(i,2)))
    j+=1
    if j > 5:
        j=0

plt.legend(ncol=2,frameon=False,loc="lower right")
plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=3,colors="black",linewidth=1)
# plt.xlim([0,10])
# plt.ylim([-500,2500])
plt.savefig("3discrete_righthook_results_c.pdf")
plt.show()

j=0


c2 = [0.05,1.0,2.0,3.0,4.0,5.0]

for i in c2:
    right1 = np.loadtxt("4c_right_"+str(round(i,2))+".txt",comments="#",delimiter=";")
    right2 = np.loadtxt("5c_right_"+str(round(i,2))+".txt",comments="#",delimiter=";")
    right = right1+right2
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"$c$="+str(round(i,2)))
    j+=1
    if j > 5:
        j=0

plt.legend(ncol=2,frameon=False,loc="lower right")
plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=3,colors="black",linewidth=1)
# plt.xlim([0,10])
# plt.ylim([-500,2500])
plt.savefig("3discrete_righthook_results_c.pdf")
plt.show()
