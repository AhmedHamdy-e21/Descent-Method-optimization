from math import *
from Utilities import *
'''


h(Lambda)=a+b*Lambda+c*Lambda**2 ; c>0 to be minimum
Lambda=-b/(2*c)

We have the function value at X1, and lambda is zero, so we need to make use of this piece of info.
Then we'll generate two other quadratic equations:
A=0
B=T
C=2T
f=A+bA+xA^2
where T is up to the problem if there are quick flacuations T is small otherwise for a smooth gradually increasing function it could be large number.
'''

def lambdastar(f_A, f_B, f_C, t):
    return ((4 * f_B - 3 * f_A - f_C) / (4 * f_B - 2 * f_C - 2 * f_A)) * t


def GenerateQuadratic(t,x0,Lambda,s):
    ObjectiveFunction=OFLambda(s,x0)
    A = 0
    B = t
    C = 2 * t
    f_1 = ObjectiveFunction(A)
    f_2 = ObjectiveFunction(B)
    f_3 = ObjectiveFunction(C)

    f_A =  ObjectiveFunction(A)
    f_B = ObjectiveFunction(B)
    f_C = ObjectiveFunction(C)

    if (f_1 > f_A):
        f_C = f_1
        f_B = ObjectiveFunction(t / 2)
        Lambda_star = lambdastar(f_A, f_B, f_C, t)
    elif (f_1 < f_A):
        f_C = f_1
        f_B = ObjectiveFunction(t / 2)
        Lambda_star = lambdastar(f_A, f_B, f_C, t )
    a = f_A
    b = (4 * f_B - 3 * f_A - f_C) / 2 * t
    c = (f_C + f_A - (2 * f_B)) / (2 * (t**2))

    Lambda_star = ((4 * f_B - 3 * f_A - f_C) /
                   (4 * f_B - 2 * f_C - 2 * f_A)) * t

                   


    h=a+b*Lambda_star+c*(Lambda_star**2)
    Epsilon=0.0001

    while ((h-ObjectiveFunction(Lambda_star))/ObjectiveFunction(Lambda_star))>Epsilon:
        if ObjectiveFunction(Lambda_star)<f_A and ObjectiveFunction(Lambda_star)>f_B:
            f_A=ObjectiveFunction(Lambda_star)

        elif ObjectiveFunction(Lambda_star)<f_C and ObjectiveFunction(Lambda_star)>f_B:
            f_C=ObjectiveFunction(Lambda_star)
        elif ObjectiveFunction(Lambda_star)<f_B:
            f_B=ObjectiveFunction(Lambda_star)
        Lambda_star = ((4 * f_B - 3 * f_A - f_C) /
                   (4 * f_B - 2 * f_C - 2 * f_A)) * t
        
        a = f_A
        b = (4 * f_B - 3 * f_A - f_C) / 2 * t
        c = (f_C + f_A - (2 * f_B)) / (2 * (t**2))
        h=a+b*Lambda_star+c*(Lambda_star**2)
        print(a,b,c,Lambda_star," FF",f_A,f_B,f_C,ObjectiveFunction(Lambda_star),h)
                   


    h=a+b*Lambda_star+c*(Lambda_star**2)

   
    pass

s=[[4],[0]]
xi=[[-1],[1]]
t=0.001