from Utilities import *
# import sys
# import os
# # sys.path.append(os.path.abspath(sys.path[0] + '/..'))
# # sys.path.append( '/../1-D-minimization-Problem')
# sys.path.insert(1, '../1-D-minimization-Problem')
from CubicInterpolation import *

def objFunction(x1,x2):
    return 100*((x2-(x1**2))**2)+(1-x1)**2
    

def HessianUpdate(objFunction,x1,x2,alpha):
    
    Bi=Hessian(objFunction)
    
    return np.linalg.inv(Bi(x1,x2) + alpha * np.eye(Bi.shape))

# def Jacobian(f,x1,x2):
#     # F.jacobian((x1, x2)).subs({x1 :1/sqrt(3),x2:1/sqrt(3)}
#     f=sp.Matrix([f])
#     J=f.jacobian((x1,x2))
#     return lambdify((x1,x2), J, modules='numpy')

def MarquardtDirection(objFunction,x1,x2,alpha):
    grad=Jacobian(objFunction,x1,x2)
    HessUpdate=HessianUpdate(objFunction,x1,x2,alpha)
    return - HessUpdate(x1,x2)@grad





x1,x2=symbols('x1 x2')  
# grad=Jacobian(objFunction(x1,x2))
# epsilon=0.001

Hess=Hessian(objFunction(x1,x2))
alpha=10000
x0=np.array([[-1.2],[1]])
# Hess=Hessian(objFunction)
# print(grad(x0[0,0],x0[1,0]))
print(Hess(x0[0,0],x0[1,0]))
# s0=-(1/alpha)*np.eye(Hess(x0[0,0],x0[1,0]).shape[1])@(grad(x0[0,0],x0[1,0]))

# Lambda,fun,grad=CubicInterpolation(0.1,s0,x0)
# print(Hess(x0[0,0],x0[1,0]))
# print(Hess(x0[0,0],x0[1,0]).shape)


# while np.linalg.norm(grad(x1,x2))>epsilon:


