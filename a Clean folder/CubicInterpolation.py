from Utilities import *

# def GradfCubic(f,x1,x2):
#     # F.jacobian((x1, x2)).subs({x1 :1/sqrt(3),x2:1/sqrt(3)}
#     f=sp.Matrix([f])
#     J=f.jacobian((x1,x2))
    
#     return lambdify((x1,x2), J, modules='numpy')

def OFLambda(s,xi):
    Lambda=Symbol('Lambda')
    xi=sp.Matrix(xi)
    s=sp.Matrix(s)
    Xi_1=xi+Lambda*s
    f=objFunction(Xi_1[0],Xi_1[1])
    return lambdify((Lambda), f, modules='numpy')

    

def ObjFunctionGradient(Lambda,s,xi):
    # s=np.asarray(s).reshape(2,1)
    # s=s/np.linalg.norm(s,ord=1)
    gradf=Gradient(s,xi)
    s=np.asarray(s).reshape(2,1)
    s=s/np.linalg.norm(s,ord=1)
    gradient=s.T*gradf(Lambda)
    return gradient
    # return gradf(Lambda)

def generateCubic(s,xi,t):
    OF=OFLambda(s,xi)
    gradOF=Gradient(s,xi)
    A=0
    B=t
    f_A=OF(A)
    f_Aprime=gradOF(A)
    f_B=OF(t)
    f_Bprime=gradOF(t)
    Z=((3*(f_A-f_B))/B)+f_Aprime+f_Bprime
    Q=np.sqrt(Z**2-f_Aprime*f_Bprime)
    a=f_A
    b=f_Aprime
    c=-(1/B)*(Z+f_Aprime)
    d=(1/(3*(B**2)))*(2*Z+f_Aprime+f_Bprime)
    Lambdas1=B*((f_Aprime+Z-Q)/(f_Aprime+f_Bprime+2*Z))
    Lambdas2=B*((f_Aprime+Z+Q)/(f_Aprime+f_Bprime+2*Z))

    if OF(Lambdas1)<OF(Lambdas2):
        return Lambdas1,OF(Lambdas1),gradOF(Lambdas1)
    else:
        return Lambdas2,OF(Lambdas2),gradOF(Lambdas2)
    # return a,b,c,d,f_A,f_Aprime,f_B,f_Bprime,Lambdas1,Lambdas2,OF(Lambdas1),OF(Lambdas2)



#s=[[4],[0]]
#xi=[[-1],[1]]
#t=0.01
#OFF=Gradient(s,xi)
#print(ObjFunctionGradient(0.001307223,s,xi))

#print(OFF(0.001307223))

#print(generateCubic(s,xi,t))

########################################################################################################################################################################
# The algorithm
########################################################################################################################################################################
# Firstly, normalize the direction

########################################################################################################################################################################
# Function to normalize right here
s=np.array([[4],[0]] )

xi=np.array([[-1],[1]])
########################################################################################################################################################################


# Get the objective function as a function of lambda only given an initial point and direction:

########################################################################################################################################################################
# Secondly get the df/dlambda aka gradient 
def Gradient(s,xi):
    Lambda=Symbol('Lambda')
    xi=sp.Matrix(xi)
    s=sp.Matrix(s)
    Xi_1=xi+Lambda*s
    f=objFunction(Xi_1[0],Xi_1[1])
    f=sp.Matrix([f])
    Lambda=sp.Matrix([Lambda])
    J=f.jacobian(Lambda)
    # print(J)
    return lambdify((Lambda), J, modules='numpy')

########################################################################################################################################################################

# then search for two points where the gradient changed its direction
# First point is A =0 and it'll be positive
# gradient=Gradient(s,xi)
# set t and increment in the while loop
t=0.1
# grad=gradient(t)
# if gradient(0)<0:
#     while gradient(t)<0:
#         t=2*t
#         grad=gradient(t)
#         # print(grad)
# else:
#     while gradient(t)<0:
#         t=2*t
#         grad=gradient(t)
#         # print(grad)
# # Awesomee Now I can get an interval 
# B=t #This is the second point ISA

# print(gradient(0),gradient(t),t)
# ########################################################################################################################################################################


# #In this step is to generate the cubic model and get the lambda
# print(generateCubic(s,xi,t))


def CubicInterpolation(t,s,xi):
    gradient=Gradient(s,xi)
    if gradient(0)<0:
        while gradient(t)<0:
            t=2*t
            # print(grad)
    elif gradient(0)>0:
        while gradient(t)>0:
            t=2*t
    return generateCubic(s,xi,t)

# print(CubicInterpolation(t,s,xi))

# There is a defficiency here that if the minimum in the negative portion, so I need to check right and left.?????