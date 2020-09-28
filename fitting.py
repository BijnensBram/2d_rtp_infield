import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as fit

def mu(a1,a2,a3,c,e):
    return a1*np.exp(-a2*(c+e)+a3)

def func(e,a1,a2,a3):
    C = 0.5
    return e*(mu(a1,a2,a3,C,e)+mu(a1,a2,a3,-C,e))

# def func(e,a1,a2,a3,a4):
#     C = 0.5
#     return 0.5*C*(mu(a1,a2,a3,a4,C,e)-mu(a1,a2,a3,a4,-C,e))+0.5*e*(mu(a1,a2,a3,a4,C,e)+mu(a1,a2,a3,a4,-C,e))

# x = np.linspace(0,2)
# y = func(x,1,4,0,1)

# plt.plot(x,y)
# plt.show()

a = []
b = []
c = []
d = []
f = []
A = [0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
for i in A:
    e,right = np.loadtxt("2new_right_"+str(i)+".txt",comments="#",delimiter=";",unpack=True)

    popt, pcov = fit.curve_fit(func,e[8:],right[8:])
    print(popt)
    print(pcov/popt)
    plt.plot(e[8:],func(e[8:],*popt))
    plt.scatter(e,right)
    a.append(popt[0])
    b.append(popt[1])
    c.append(popt[2])
    # d.append(popt[3])

plt.show()

def funca(x,a1,a2):
    return a1/(x-a2)

x = np.linspace(0,10)
y = funca(x,1,1)
plt.plot(x,y)
plt.show()

a = np.array(a)
c = np.array(c)

plt.scatter(A,a,label="c1")
# plt.show()
# plt.scatter(A,b,label="c2")
# plt.show()
plt.scatter(A,5*c-16,label="5*c3-16")
plt.legend()
plt.show()
