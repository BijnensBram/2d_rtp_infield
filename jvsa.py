import numpy as np
import matplotlib.pyplot as plt

marker = [".","v","^","s","D","o"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]

j=0
for i in [0.6,0.65,0.7,0.8,0.9,1.0]:
    right = np.loadtxt("6eright_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"$\epsilon$="+str(round(i,2)))
    j+=1
    if j > 5:
        j=0

plt.legend(ncol=1,frameon=False,loc="lower left")
plt.xlabel(r"$a$")
h=plt.ylabel("j")
h.set_rotation(0)
# plt.hlines(y=0,xmin=0,xmax=20,colors="black",linewidth=1)
plt.xlim([0,10])
plt.ylim([-500,2500])
plt.savefig("discrete_righthook_results_e.pdf")
plt.show()

j=0
plt.figure(figsize=(6,3))
for i in [0.6,0.65,0.7]:
    right = np.loadtxt("6eright_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=20)

    plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"$\epsilon$="+str(round(i,2)))
    j+=1
    if j > 5:
        j=0

# plt.legend(ncol=2,frameon=False)
# plt.xlabel(r"$a$")
# h=plt.ylabel("j")
# h.set_rotation(0)
plt.xlim([0,2])
plt.ylim([1400,2000])
plt.savefig("zoom_discrete_righthook_results_e.pdf")
plt.show()
