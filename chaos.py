import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp



def F(t, Y):
    x=Y[0]
    y=Y[1]
    z=Y[2]
    #return [10*(y-x), 28*x-y-x*z, x*y-8/3*z]
    return [10*(y-x), 27*x-y-x*z, 2*x*y-8/3*z]

tf=20
t_eval = np.arange(0, tf, 0.01)
sol = solve_ivp(F, [0, tf], [10,10,10], t_eval=t_eval)

#plt.plot(sol.y[0], sol.y[1], linewidth=0.4)
plt.plot(t_eval, sol.y[2])
plt.show()


