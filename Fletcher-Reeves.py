import sympy as sp
import numpy as np
from sympy import *
import math 

def objFunction(x1,x2):
    return 100*np.power((x2-x1**2),2)+(1-x1)**2

def lambdaStar(gradient,s,A):
    s=s.T
    gradient=gradient.T
    num=np.linalg.norm(gradient)
    print(s.shape,A.shape)

    den=s.T@A@s

    return(num/den)

def Hessian(f,x1,x2):
    # H.subs({x1 :1/sqrt(3),x2:1/sqrt(3)}
    H=hessian(f ,(x1,x2))
    return lambdify((x1,x2), H, modules='numpy')

def Jacobian(f,x1,x2):
    # F.jacobian((x1, x2)).subs({x1 :1/sqrt(3),x2:1/sqrt(3)}
    f=sp.Matrix([f])
    J=f.jacobian((x1,x2))
    return lambdify((x1,x2), J, modules='numpy')

sp.init_printing(use_latex=True)

x1,x2=symbols('x1 x2')


H=Hessian(objFunction(x1,x2),x1,x2)
J=Jacobian(objFunction(x1,x2),x1,x2)

# First iteration
x=np.array([-1.2,1])
xv=(x1,x2)
# grad1=J.evalf(subs={x1 : x[0],x2: x[1]})
# Hessian1=H.evalf(subs={x1 : x[0],x2: x[1]})

# g_func = lambdify(xv, Hessian1, modules='numpy')
# print(J(x))
# print(type(J(x[0],x[1]).shape))
lambdastar_=lambdaStar(J(x[0],x[1]),-J(x[0],x[1]),H(x[0],x[1]))
# xold=x
# xnew=xold
