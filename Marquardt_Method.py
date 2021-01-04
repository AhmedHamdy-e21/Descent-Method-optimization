from Utilities import *
import sys
import os
# sys.path.append(os.path.abspath(sys.path[0] + '/..'))
# sys.path.append( '/../1-D-minimization-Problem')
sys.path.insert(1, '../1-D-minimization-Problem')
from CubicInterpolation import *

def objFunction(x1,x2):
    return 100*((x2-(x1**2))**2)+(1-x1)**2
    

def HessianUpdate(Hess,x1,x2,alpha):
    
    return np.linalg.inv(Hess(x1,x2) + alpha * np.eye(Hess(x1,x2).shape[0]))


# def Jacobian(f,x1,x2):
#     # F.jacobian((x1, x2)).subs({x1 :1/sqrt(3),x2:1/sqrt(3)}
#     f=sp.Matrix([f])
#     J=f.jacobian((x1,x2))
#     return lambdify((x1,x2), J, modules='numpy')

def MarquardtDirection(Hess,grad,x1,x2,alpha):
    HessUpdate=HessianUpdate(Hess,x1,x2,alpha)
    # print(grad(x1,x2))
    return - HessUpdate@(grad(x1,x2).reshape(2,1))





x1,x2=symbols('x1 x2')  
grad=Jacobian(objFunction(x1,x2),x1,x2)
# epsilon=0.001

Hess=Hessian(objFunction(x1,x2))
alpha=10000
x0=np.array([[-1.2],[1]])
# Hess=Hessian(objFunction)
# print(grad(x0[0,0],x0[1,0]))
# print(grad(x0[0,0],x0[1,0]))
# print(Hess(x0[0,0],x0[1,0]))

# Initial direction.
# ############## ############## ############## ############## ############## #############
s0=-(1/alpha)*np.eye(Hess(x0[0,0],x0[1,0]).shape[1])@(grad(x0[0,0],x0[1,0]).reshape(2,1))
# ############## ############## ############## ############## ############## ############## 

# s=MarquardtDirection(objFunction,x1,x2,alpha)
# print(s)
# print(Jacobian(objFunction(x1,x2),x1,x2)(x0[0,0],x0[1,0]))
print(s0,MarquardtDirection( Hess ,grad,x0[0,0],x0[1,0],alpha))

# print(s0)

# Lambda,fun,grad=CubicInterpolation(0.1,s0,x0)
x1=x0
c1=0.25
c2=3
epsilon=0.00001
flag=0
while np.linalg.norm(grad(x1[0,0],x1[1,0]).reshape(2,1),ord=2)>epsilon:
    s=MarquardtDirection( Hess ,grad,x1[0,0],x1[1,0],alpha)
    Lambda,OF,gradOF=CubicInterpolation(0.001,s,x1)
    fprev=objFunction(x1[0,0],x1[1,0])
    x1=x1+Lambda*s
    fnext=objFunction(x1[0,0],x1[1,0])
    if fnext<fprev:
        alpha=c1*alpha
    else:
        if(flag==0):
            flag+=1
            alpha=10000
        
        alpha=c2*alpha
    print(x1,Lambda,fnext,fprev,grad(x1[0,0],x1[1,0]))


