import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from math import *


def F(t, Y):
    x=Y[0]
    y=Y[1]
    xp=Y[2]
    yp=Y[3]

    if y>pi:
        y=2*pi-y
        x+=pi
    if y<0:
        y=-y
        x+=pi
    x=x%(2*pi)

    if abs(y)<0.00001:
        z3=-10
    else:
        z3=-2/tan(y)*xp*yp
    
    z4=sin(y)*cos(y)*xp**2
    

    return [xp, yp, z3, z4]

tf=2
t_eval = np.arange(0, tf, 0.01)
sol = solve_ivp(F, [0, tf], [0,pi/2-0.5,1,0], t_eval=t_eval)


U1=sol.y[0]
U2=sol.y[1]
result_x=[]
result_y=[]
for i in range(len(U1)):
    if U2[i]>=pi:
        y=2*pi-U2[i]
        x=U1[i]+pi
    elif U2[i]<0:
        y=-U2[i]
        x=U1[i]+pi
    else:
        y=U2[i]
        x=U1[i]
    x=x%(2*pi)
    y=pi/2-y
    x=x/pi*180
    y=y/pi*180
    result_x.append(x)
    result_y.append(y)


plt.scatter(result_x, result_y, s=2)
#plt.plot(t_eval, sol.y[2])
plt.show()


