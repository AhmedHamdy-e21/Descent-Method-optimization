 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def Plot3D(X,Y,Z):
    fig = plt.figure(2)
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
                       # Customize the z axis.
    # ax.set_zlim(-1.01, 1.01)
    # ax.zaxis.set_major_locator(LinearLocator(10))
    # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.scatter3D(-1.2, 1, objFunction(-1.2,1), c=objFunction(-1.2,1), cmap='Greens')


    fig = plt.figure(1)
    ax1 = plt.axes(projection='3d')
    ax1.contour3D(X, Y, Z, 50, cmap='binary')

    plt.show()


def objFunction(x1,x2):
    return 100*np.power((x2-x1**2),2)+(1-x1)**2


X1=np.linspace(-100,100,2000)
X2=np.linspace(-100,100,2000)
X1, X2 = np.meshgrid(X1, X2)
Z=objFunction(X1,X2)
Plot3D(X1,X2,Z)
