import matplotlib.pyplot as plt
import numpy as np

sigma,move = np.loadtxt("sigma_and_move.txt",comments="#",delimiter=";",unpack=True)

plt.hist(sigma)
plt.title(r"$\sigma$")
plt.savefig("hist_sigma.png",dpi=190)
plt.show()

plt.hist(move)
plt.title(r"move direction")
plt.savefig("hist_move.png",dpi=190)
plt.show()
