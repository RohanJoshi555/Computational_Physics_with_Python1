import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(r,t):
    theta = r[0]; omega = r[1]
    ftheta = omega; fomega = -(g/l)*np.sin(theta) + C*np.cos(theta)*np.sin(Omega*t)
    return np.array([ftheta,fomega])

def odeSystemRK4(f,rinit,tinit,tfinal,nt):
    nr = len(rinit)
    h = (tfinal - tinit)/(nt-1)
    r = np.zeros((nt,nr))
    t = np.linspace(tinit,tfinal,nt)
    r[0,:] = rinit
    for i in range(nt-1):
        k1 = h*f(r[i,:],t[i])
        k2 = h*f(r[i,:] + k1/2,t[i] + h/2)
        k3 = h*f(r[i,:] + k2/2,t[i] + h/2)
        k4 = h*f(r[i,:] + k3,t[i])
        r[i+1,:] = r[i,:] + (k1 + 2*k2 + 2*k3 + k4)/6
    return r,t

g = 980 ## in cm/sec
l = 10  ## in cm
C = 10  ## in 1/sec^2
Omega = 9.899 ## in 1/sec
thetainit = 0  ## in degrees
omegainit = 0  ## in rad/sec
## time in sec
tinit = 0
tfinal = 100

thetainitrad = np.pi*thetainit/180  ## convert angle to radians
rinit = np.array([thetainitrad,omegainit])
dt = (tfinal - tinit)/(1000)
r,t = odeSystemRK4(f,rinit,tinit,tfinal,10001)
theta = r[:,0]; omega = r[:,1]

fig1 = plt.figure(1)
ax1 = plt.gca()
ax1.plot(t,theta*180/np.pi,label = 'theta')
ax1.plot(t,omega,label = 'omega')
ax1.grid();ax1.legend()

fig2 = plt.figure(2)
ax2 = plt.gca()
arm, = ax2.plot([],[],color = 'black',lw = 0.5)
bob, = ax2.plot([],[],'o')
ax2.set_xlim(-15,15); ax2.set_ylim(-15,15)

def update(frame):
    x_current = l*np.sin(theta[frame])
    y_current = -l*np.cos(theta[frame])
    arm.set_data([0,x_current],[0,y_current])
    bob.set_data([x_current],[y_current])
    return arm,bob
anim = animation.FuncAnimation(fig = fig2, func = update, frames = len(t), interval = 10,blit = True)
plt.show()