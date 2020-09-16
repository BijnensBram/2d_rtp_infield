import numpy as np
import matplotlib.pyplot as plt

marker = [".","v","^","s","D"]

# j=0
# for i in np.linspace(0.2,1,5):
#     left = np.loadtxt("left_"+str(round(i,2))+".txt",comments="#",delimiter=";")
#     # right = np.loadtxt("right_"+str(round(i,2))+".txt",comments="#",delimiter=";")
#     # sym = np.loadtxt("sym_"+str(round(i,2))+".txt",comments="#",delimiter=";")

#     plt.rc('text', usetex=True)
#     plt.rc('font', family='serif',size=14)
    
#     plt.plot(left[:,0],left[:,1],marker=marker[j],label=r"Hook on the left, a="+str(round(i,2)))
#     # plt.plot(right[:,0],right[:,1],marker=".",label=r"Hook at the right, a="+str(round(i,2)))
#     # plt.plot(sym[:,0],sym[:,1],marker=".",label=r"Hook is symmetric, a="+str(round(i,2)))
#     j+=1

# plt.subplots_adjust(top=0.75)
# plt.legend(ncol=2,loc="upper center",bbox_to_anchor=(0.5, 1.4))


# plt.xlabel(r"$\epsilon$")
# plt.ylabel("j")
# plt.hlines(y=0,xmin=-2,xmax=1,colors="black",linewidth=1)
# plt.xlim([-2,0])
# plt.ylim([-30,15])
# plt.savefig("lefthook_results_a.pdf")
# plt.show()

# j=0
# for i in np.linspace(0.2,1,5):
#     # left = np.loadtxt("left_"+str(round(i,2))+".txt",comments="#",delimiter=";")
#     right = np.loadtxt("right_"+str(round(i,2))+".txt",comments="#",delimiter=";")
#     # sym = np.loadtxt("sym_"+str(round(i,2))+".txt",comments="#",delimiter=";")

#     plt.rc('text', usetex=True)
#     plt.rc('font', family='serif',size=14)
    
#     # plt.plot(left[:,0],left[:,1],marker=".",label=r"Hook at the left, a="+str(round(i,2)))
#     plt.plot(right[:,0],right[:,1],marker=marker[j],label=r"Hook on the right, a="+str(round(i,2)))
#     # plt.plot(sym[:,0],sym[:,1],marker=".",label=r"Hook is symmetric, a="+str(round(i,2)))
#     j+=1
# plt.subplots_adjust(top=0.75)
# plt.legend(ncol=2,loc="upper center",bbox_to_anchor=(0.5, 1.4))

# plt.xlabel(r"$\epsilon$")
# plt.ylabel("j")
# plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
# plt.xlim([0,2])
# plt.ylim([-15,30])
# plt.savefig("righthook_results_a.pdf")
# plt.show()

j=0
for i in np.linspace(0.2,1,5):
    # left = np.loadtxt("left_"+str(round(i,2))+".txt",comments="#",delimiter=";")
    # right = np.loadtxt("right_"+str(round(i,2))+".txt",comments="#",delimiter=";")
    sym = np.loadtxt("sym_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    # plt.plot(left[:,0],left[:,1],marker=".",label=r"Hook at the left, a="+str(round(i,2)))
    # plt.plot(right[:,0],right[:,1],marker=".",label=r"Hook at the right, a="+str(round(i,2)))
    plt.plot(sym[:,0],sym[:,1],marker=marker[j],label=r"Symmetric hook, a="+str(round(i,2)))
    j+=1

plt.subplots_adjust(top=0.75)
plt.legend(ncol=2,loc="upper center",bbox_to_anchor=(0.5, 1.4))

plt.xlabel(r"$\epsilon$")
plt.ylabel("j")
plt.hlines(y=0,xmin=-2,xmax=2,colors="black",linewidth=1)
plt.vlines(x=0,ymin=-60,ymax=60,colors="black",linewidth=1)
plt.xlim([-2,2])
plt.ylim([-200,200])
plt.savefig("symhook_results_a.pdf")
plt.show()
