 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import sympy as sp
import numpy as np
from sympy import *
import math 

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
    return 100*((x2-(x1**2))**2)+(1-x1)**2
    

def Hessian(f):
    # H.subs({x1 :1/sqrt(3),x2:1/sqrt(3)}
    x1,x2=symbols('x1 x2')
    # print(f)
    f=sp.Matrix([f])
    H=hessian(f ,(x1,x2))
    return lambdify((x1,x2), H, modules='numpy')

def Jacobian(f,x1,x2):
    # F.jacobian((x1, x2)).subs({x1 :1/sqrt(3),x2:1/sqrt(3)}
    f=sp.Matrix([f])
    J=f.jacobian((x1,x2))
    return lambdify((x1,x2), J, modules='numpy')

