import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation
import matplotlib
from matplotlib import animation
from mpl_toolkits import mplot3d

# Define Lorenz Differential Equations
def f(x,t):
    return np.array([sigma*(x[1] - x[0]), x[0]*(rho - x[2]) - x[1], x[0]*x[1] - beta*x[2]])

rho = 28;sigma = 10;beta = 8/3
t = np.linspace(0,20,1000)
xinit = np.array([7,10,25])
sol = odeint(func = f, y0 = xinit, t = t)
X = sol[:,0]; Y = sol[:,1]; Z = sol[:,2]

fig = plt.figure()
axis = plt.axes(projection = '3d')
lorenzCurve, = axis.plot3D([],[],[],color = 'red',linewidth = 0.5)
lorenzPoint, = axis.plot3D([],[],[],'o')
axis.set_xlabel('x');axis.set_ylabel('y');axis.set_zlabel('z');
axis.set_xlim(min(X),max(X))
axis.set_ylim(min(Y),max(Y))
axis.set_zlim(min(Z),max(Z))

def update(frame):
    x_current = X[:frame+1]
    y_current = Y[:frame+1]
    z_current = Z[:frame+1]
    # Uncomment for updating the field of view with time
    '''
    axis.set_xlim(min(x_current),max(x_current))
    axis.set_ylim(min(y_current),max(y_current))
    axis.set_zlim(min(z_current),max(z_current))
    '''
    lorenzCurve.set_data(x_current,y_current)
    lorenzCurve.set_3d_properties(z_current)

    lorenzPoint.set_data([X[frame]],[Y[frame]])
    lorenzPoint.set_3d_properties([Z[frame]])

    axis.view_init(azim=frame)
    return lorenzCurve, lorenzPoint

anim = FuncAnimation(fig = fig, func = update, frames = len(t), interval = 25, blit = False)
#matplotlib.rcParams['animation.ffmpeg_path'] = 'D:\\Python\\ffmpeg-7.1.1-essentials_build\\ffmpeg-7.1.1-essentials_build\\bin\\ffmpeg.exe'
#writer  = animation.FFMpegWriter(fps = 100 )
#anim.save('Lorenz_Attractor.mp4')
plt.show()