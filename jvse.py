import numpy as np
import matplotlib.pyplot as plt

marker = [".","v","^","s","D","o"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]

j=0
for i in np.linspace(0.4,0.8,3):
    right = np.loadtxt("right_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"a="+str(round(i,2)))
    j+=1

right = np.loadtxt("right_a_5.txt",comments="#",delimiter=";")
plt.plot(right[:,0],right[:,1],marker=marker[j],color=colors[j],markersize=3,label=r"a=5.0")

plt.legend(ncol=2,frameon=False)
plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
plt.xlim([0,2])
plt.ylim([-100,350])
plt.savefig("discrete_righthook_results_a.pdf")
plt.show()

j=0
for i in np.linspace(0.4,0.8,3):
    right = np.loadtxt("right_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],color=colors[j],markersize=3,label=r"a="+str(round(i,2)))
    j+=1

right = np.loadtxt("rigt_5.0.txt",comments="#",delimiter=";")
plt.plot(right[:,0],right[:,1],marker=marker[j],color=colors[j],markersize=3,label=r"a=5.0")

plt.legend(ncol=2,frameon=False)
plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
plt.xlim([0.5,1.5])
plt.ylim([-100,350])
plt.savefig("zoom_discrete_righthook_results_a.pdf")
plt.show()

j=0
for i in np.linspace(0.4,0.8,3):
    sym = np.loadtxt("sym_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(sym[:,0],sym[:,1],marker=marker[j],color=colors[j],markersize=3,label=r"a="+str(round(i,2)))
    j+=1

sym = np.loadtxt("sym_5.0.txt",comments="#",delimiter=";")
plt.plot(sym[:,0],sym[:,1],marker=marker[j],color=colors[j],markersize=3,label=r"a=5.0")
plt.legend(ncol=2,frameon=False)

plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=-2,xmax=2,colors="black",linewidth=1)
plt.vlines(x=0,ymin=-750,ymax=400,colors="black",linewidth=1)
plt.vlines(x=0,ymin=700,ymax=750,colors="black",linewidth=1)
plt.xlim([-2,2])
plt.ylim([-750,750])
plt.savefig("discrete_symhook_results_a.pdf")
plt.show()

j=0
inhook = np.loadtxt("inhook.txt",comments="#", delimiter=";")
above = np.loadtxt("abovehook.txt",comments="#", delimiter=";")

plt.plot(inhook[:,0],inhook[:,1],marker=marker[j],color=colors[j],label=r"In the hook")
j+=1
plt.plot(above[:,0],above[:,1],marker=marker[j],color=colors[j],label=r"Out the hook")

plt.legend(ncol=2,frameon=False)
plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
plt.xlim([0,2])
plt.ylim([-150,350])
plt.savefig("initial_J_for_different_init.pdf")
plt.show()

a = np.loadtxt("a=inf.txt",comments="#", delimiter=";")
c = np.loadtxt("c=0.txt",comments="#", delimiter=";")
