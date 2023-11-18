import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from math import *
global w
def force(k):
    return lambda x:-sin(k*x)

def F(t, Y):
    global w
    x=Y[0]
    xp=Y[1]

    return [xp, -x+force(w)(t)]

tf=100
t_eval = np.linspace(0, tf, 1000)

W=np.linspace(0.01, 5, 100)
M=[]
for i in range(len(W)):
    w=W[i]
    sol = solve_ivp(F, [0, tf], [1,0], t_eval=t_eval)
    M.append(max(sol.y[0][20:]))
plt.plot(W, M)
plt.savefig("Resonance.png", dpi=300)
plt.show()


