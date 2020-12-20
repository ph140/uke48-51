import numpy as np
from matplotlib import pyplot as plt

k = 0.1
t_0 = 0  # startverdi for t (initialbetingelse)
f_0 = 1000  # startverdi for f (initialbetingelse)
t_slutt = 20  # sluttverdi for t

N = 10000  # antall steg
h = (t_slutt-t_0)/(N-1)  # regner ut steglengden

f = np.zeros(N)
f[0] = 1000


def f_derivert(ft):
    return k*ft


t = np.linspace(t_0, t_slutt, N)

for i in range(N-1):
    # bruker formel for å regne ut "neste steg"
    f[i+1] = f[i] + f_derivert(f[i])*h

plt.plot(t, f)
plt.show()
