import numpy as np
import matplotlib.pyplot as plt
from parameters import *
from annualcycle import *
from windstress import *

def f_matrix(T,h,R,b,epsilon,xi):
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
    M=np.array([[R,gamma],[-alpha*b,-r]])
    b= [epsilon*(h+b*T)**3+gamma*xi, -alpha*xi]
    w=[T,h]
    fw=np.dot(M,w)+b
    return fw[0],fw[1]
    
def f(T,h,R,b,epsilon,xi):
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
    fT=R*T+gamma*h - epsilon*(h+b*T)**3 + gamma*xi
    fh=-r*h -alpha*b*T -alpha*xi

    return fT,fh

def rk4_step(T,h,R,b,epsilon,xi):
    """ Moves forward one step in time"""
    Tk1,hk1 = f(T,h, R,b,epsilon,xi)
    Tk2,hk2 = f( (T+Tk1*dt/2),(h+hk1*dt/2) ,R,b,epsilon,xi)
    Tk3,hk3 = f( (T+Tk2*dt/2),(h+hk2*dt/2) , R,b,epsilon,xi)
    Tk4,hk4 = f( (T+Tk3*dt),(h+hk3*dt) ,R,b,epsilon,xi)
        
    T_next= T + (dt/6)*(Tk1+2*Tk2+2*Tk3+Tk4)
    h_next= h + (dt/6)*(hk1+2*hk2+2*hk3+hk4)

    return T_next,h_next

def rk4(T0,h0,mu0,nt=250,f_ann=0.,f_ran=0.,epsilon=0., mu_ann=0.):
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
    
    
    # Initialise arrays:
    T = np.zeros(nt)
    h = np.zeros(nt)
    T[0] = T0
    h[0] = h0
    
    for it in range(1,nt):
        xi = windstress(f_ann,f_ran,it)
        
        mu = annualcycle(mu0,mu_ann,it)
        
        # Derived Parameters:
        b = b0*mu
        R = gamma*b - c

        
        T[it],h[it] = rk4_step(T[it-1],h[it-1],R,b,epsilon,xi)

    return T,h


    
    
