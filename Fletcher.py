import sympy as sp
import numpy as np
from sympy import *
import math 
from Utilities import *
import sys
import os
# sys.path.append(os.path.abspath(sys.path[0] + '/..'))
# sys.path.append( '/../1-D-minimization-Problem')
sys.path.insert(1, '../1-D-minimization-Problem')
from CubicInterpolation import *

def objFunction(x1,x2):
    return 100*np.power((x2-x1**2),2)+(1-x1)**2
    # return x1-x2+2*x1**2+2*x1*x2+x2**2

def lambdaStar(gradient,s,A):
    s=s
    gradient=gradient
    num=np.linalg.norm(gradient,ord=1)
    
    # print(s)
    den=s.T@A@s
    # print(num,den,A)
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


# # First iteration
xnought=np.array([[0],[0]])
# xv=(x1,x2)
Jnought=J(xnought[0,0],xnought[1,0]).reshape(2,1)
HesNought=H(xnought[0,0],xnought[1,0])
lambdastar=lambdaStar(Jnought,-Jnought,HesNought)
# print(lambdastar)
xold=xnought
s=-Jnought
# print(s)
xnew=(xold+lambdastar*s)
# print(J(x[0,0],x[1,0]).reshape(2,1))
epsilon=0.00001
# print(Jnought)
# # # print(J(xnew[0],xnew[1]))
i=0
while np.linalg.norm( J(xnew[0],xnew[1]).reshape(2,1),ord=2)>epsilon:
    i=i+1
    # print(xnew.shape)
    Jnew=J(xnew[0,0],xnew[1,0]).reshape(2,1)
    Jold=J(xold[0,0],xold[1,0]).reshape(2,1)
    beta=np.linalg.norm(Jnew, np.inf)/np.linalg.norm(Jold, np.inf)
    # print(beta)
    # # print("s ",J(xold[0],xold[1]))
    # # print("Gradient",J(xnew[0],xnew[1]))
    s=-Jnew+beta*s
    # lambdastar=lambdaStar(Jnew,s,H(xnew[0,0],xnew[1,0]))
    lambdastar,OF,gradOF=CubicInterpolation(0.001,s,xnew)
    #lambdastar=0.001
    # print(lambdastar)

    xold=xnew
    xnew=xold+lambdastar*s
    # print("New ",xnew)
    print(J(xnew[0],xnew[1]))
    print(xnew)
    # print(i)
    # print(lambdastar)
    
 
