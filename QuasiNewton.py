from Utilities import * 
import sys
import os
# sys.path.append(os.path.abspath(sys.path[0] + '/..'))
# sys.path.append( '/../1-D-minimization-Problem')
sys.path.insert(1, '../1-D-minimization-Problem')
from CubicInterpolation import *
def DFP(grad,x1,x2,s,H,Lambda):
    # print(x1,x2)
    # print(grad(x1[0,0],x1[1,0]))
    # print(grad(x2[0,0],x2[1,0]))
    y=(grad(x2[0,0],x2[1,0])-grad(x1[0,0],x1[1,0])).reshape(2,1)

    # print("y is ",y)
    s=x2-x1
    M=-(H@y@y.T@H)/(y.T@H@y)
    N=Lambda*(s@s.T)/(y.T@s)
    Hi=H+M+N
    return Hi

def QuasiNewtonDirection(grad,x1,x2,s,H,Lambda):
    Hi=DFP(grad,x1,x2,s,H,Lambda)
    return -Hi@((grad(x1[0,0],x1[1,0]).reshape(2,1)))
x1,x2=symbols('x1 x2')  
x0=np.array([[-1.2],[1]])
grad=Jacobian(objFunction(x1,x2),x1,x2)
Hi=np.eye(x0.shape[0])

# print(Hi)
s=-Hi@(grad(x0[0,0],x0[1,0]).reshape(2,1))
Lambda,OF,gradOF=CubicInterpolation(0.001,s,x0)
xi_1=x0
xi=x0+Lambda*s
# print(xi,xi_1)
# If not the optimum 
# print(grad(x0[0,0],x0[1,0]))
Hi=DFP(grad,xi_1,xi,s,Hi,Lambda)
# print(xi,Lambda,grad(xi[0,0],xi[1,0]),Hi)

epsilon=0.00001
while np.linalg.norm(grad(xi[0,0],xi[1,0]).reshape(2,1),ord=2)>epsilon:
    # print("X is ",xi)
    s=QuasiNewtonDirection(grad,xi_1,xi,s,Hi,Lambda)
    # print("s",s)
    Lambda,OF,gradOF=CubicInterpolation(0.001,s,xi)
    fprev=objFunction(xi[0,0],xi[1,0])
    xi_1=xi
    xi=xi+Lambda*s
    # print(xi,Lambda,fprev,grad(xi[0,0],xi[1,0]))
    print(xi,fprev)

