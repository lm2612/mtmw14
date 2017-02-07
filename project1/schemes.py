import numpy as np
import matplotlib.pyplot as plt
from parameters import *
from derived_parameters import *

def f(q,R,b,epsilon,xi):
    """Calculates the RHS of equations for dT/dt and dh/dt for recharge oscillator
    Returns fT,fh which are RHS of dT/dt and dh/dt respectively
    Arguments:
        T: temperature anomaly, float
        h: thermocline depth, float
        R:
        b:
        epsilon:
        xi:
    """
    M=np.array([ [R,gamma],[-1*alpha*b,-1*r] ])
    N= [-1*epsilon*((q[1]+b*q[0])**3) + gamma*xi, -1*alpha*xi]
    f=M.dot(q)+N
    return f

def rk4_step(T,h,epsilon,f_ann,f_ran,mu0,mu_ann,W,it):
    """ Moves forward one step in time"""
    
    q = np.array([T,h])
    R,b,xi,W = R_b_xi(f_ann,f_ran,mu0,mu_ann,W,it)
    k1 = f(q, R, b,epsilon,xi)
    
    R,b,xi,W = R_b_xi(f_ann,f_ran,mu0,mu_ann,W,it+0.5)
    k2 = f( q+k1*dt/2., R,b,epsilon,xi)
    
    R,b,xi,W = R_b_xi(f_ann,f_ran,mu0,mu_ann,W,it+0.5)
    k3 = f( q+k2*dt/2. , R,b,epsilon,xi)

    R,b,xi,W = R_b_xi(f_ann,f_ran,mu0,mu_ann,W,it+1)
    k4 = f( q+k3*dt ,R,b,epsilon,xi)
    
    q += (k1+2*k2+2*k3+k4)*dt/6.
    return q[0],q[1],W


def rk4(T0,h0,mu0,n_cycles=1.,f_ann=0.,f_ran=0.,epsilon=0., mu_ann=0.):
    """Uses Runge-Kutta 4th order method to calculate non-dimensionalised
    temperature anomaly and thermocline depth for each iteration, up to nt timesteps
    Returns T,h: numpy arrays of length nt
    Arguments:
        T0: initial condition for temperature anomaly, float
        h0: initial condition for thermocline depth, float
        nt: number of iterations, integer (Default = 250)
        mu: float or np array of length nt from annual cycle function
        xi: float
        epsilon: float
        mu_ann: set to 0. to turn annual cycle off (Default) or 0.2 to turn on
    """
    nt= int(round(n_cycles*42/(2*dt)))
    # Initialise arrays:
    T = np.zeros(nt)
    h = np.zeros(nt)
    T[0] = T0
    h[0] = h0
    # Need initial W for wind forcing:
    W = (np.random.randint(-1e5,1e5))/(1e5)

    
    for it in range(1,nt):
        T[it],h[it],W = rk4_step(T[it-1],h[it-1],epsilon,f_ann,f_ran,mu0,mu_ann,W,it)
        
    return T,h


    
    
