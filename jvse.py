import numpy as np
import matplotlib.pyplot as plt

marker = [".","v","^","s","D"]

j=0
for i in np.linspace(0.4,0.8,3):
    left = np.loadtxt("left_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(left[:,0],left[:,1],marker=marker[j],label=r"Hook on the left, a="+str(round(i,2)))
    j+=1

plt.subplots_adjust(top=0.75)
plt.legend(ncol=2,loc="upper center",bbox_to_anchor=(0.5, 1.4))


plt.xlabel(r"$\epsilon$")
plt.ylabel("j")
plt.hlines(y=0,xmin=-2,xmax=1,colors="black",linewidth=1)
plt.xlim([-2,0])
plt.ylim([-350,100])
plt.savefig("discrete_lefthook_results_a.pdf")
plt.show()

j=0
for i in np.linspace(0.4,0.8,3):
    right = np.loadtxt("right_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],label=r"Hook on the right, a="+str(round(i,2)))
    j+=1
plt.subplots_adjust(top=0.75)
plt.legend(ncol=2,loc="upper center",bbox_to_anchor=(0.5, 1.4))

plt.xlabel(r"$\epsilon$")
plt.ylabel("j")
plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
plt.xlim([0,2])
plt.ylim([-100,350])
plt.savefig("discrete_righthook_results_a.pdf")
plt.show()

j=0
for i in np.linspace(0.4,0.8,3):
    sym = np.loadtxt("sym_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(sym[:,0],sym[:,1],marker=marker[j],label=r"Symmetric hook, a="+str(round(i,2)))
    j+=1

plt.subplots_adjust(top=0.75)
plt.legend(ncol=2,loc="upper center",bbox_to_anchor=(0.5, 1.4))

plt.xlabel(r"$\epsilon$")
plt.ylabel("j")
plt.hlines(y=0,xmin=-2,xmax=2,colors="black",linewidth=1)
plt.vlines(x=0,ymin=-750,ymax=750,colors="black",linewidth=1)
plt.xlim([-2,2])
plt.ylim([-750,750])
plt.savefig("discrete_symhook_results_a.pdf")
plt.show()

inhook = np.loadtxt("inhook.txt",comments="#", delimiter=";")
above = np.loadtxt("abovehook.txt",comments="#", delimiter=";")

plt.plot(inhook[:,0],inhook[:,1],marker=marker[j],label=r"Hook on the right starting in the hook, a=0.4")
plt.plot(above[:,0],above[:,1],marker=marker[j],label=r"Hook on the right starting out the hook, a=0.4")

plt.subplots_adjust(top=0.75)
plt.legend(ncol=1,loc="upper center",bbox_to_anchor=(0.5, 1.4))

plt.xlabel(r"$\epsilon$")
plt.ylabel("j")
plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
plt.xlim([0,2])
plt.ylim([-150,350])
plt.savefig("initial_J_for_different_init.pdf")
plt.show()
