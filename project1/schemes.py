import numpy as np
from parameters import *

def scheme_euler(T0,h0,nt,dt,R,alpha,b,r,gamma):
    """Forward in time for T and backward in time for h. Returns arrays
    of length nt of T,h for each timestep
    Arguments:
        T: initial condition for T
        h: initial condition for h
        nt: number of iterations
        dt:
        R:
        alpha:
        b:
        r:
        gamma:
        """
    # Initialise arrays:
    T = np.zeros(nt)
    h = np.zeros(nt)
    T[0] = T0
    h[0] = h0
    
    for it in range(1,nt):
        T[it] = (1+R*dt)*T[it-1] + dt*gamma*h[it-1]
        h[it] = (h[it-1] - dt*alpha*b*T[it])/(1+r*dt)

    return T,h

def next_step(T,h,dt):
    """Returns Tnew and hnew at next step so this can be used for any method
    Arguments:
    T: current step
    h: current step """
    Tnew=(1+R*dt)*T + dt*gamma*h
    hnew= (h- dt*alpha*b*Tnew)/(1+r*dt)
    return Tnew,hnew

def f(T,h):
    """f = RHS of equation for dT/dt and dh/dt
    returns tuple """
    fT=R*T+gamma*h
    fh=(-r*h -alpha*b*T)

    return fT,fh

def rk4(T0,h0):
    """
"""
    # Initialise arrays:
    T = np.zeros(nt)
    h = np.zeros(nt)
    T[0] = T0
    h[0] = h0
    
    for it in range(1,nt):
        Tk1,hk1 = f(T[it-1],h[it-1])
        Tk2,hk2 = f( (T[it-1]+Tk1*dt/2),(h[it-1]+hk1*dt/2) )
        Tk3,hk3 = f( (T[it-1]+Tk2*dt/2),(h[it-1]+hk2*dt/2) )
        Tk4,hk4 = f( (T[it-1]+Tk3*dt),(h[it-1]+hk3*dt) )
        
        T[it]= T[it-1] + (dt/6)*(Tk1+2*Tk2+2*Tk3+Tk4)
        h[it]= h[it-1] + (dt/6)*(hk1+2*hk2+2*hk3+hk4)

    return T,h
