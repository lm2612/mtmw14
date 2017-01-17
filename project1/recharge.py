import numpy as np
import matplotlib.pyplot as plt
from schemes import *

def main():
    # Initial Conditions
    TOld = 1.125
    hOld = 0.
    
    # Parameters
    forcing = 0
    epsilon = 0
    b0 = 2.5
    mu = 2./3.
    gamma = 0.75
    c = 1.
    r = 0.25
    alpha = 0.125
    dt = 0.5
    nt = 100


    # Derived Parameters
    b = b0*mu
    R = gamma*b - c

    T,h=scheme(TOld,hOld,nt,dt,R,alpha,b,r,gamma)
    
    f,axes=plt.subplots(2,1,sharex=True)
    axes[0].plot(2*np.arange(nt),7.5*T,color='r')
    axes[0].set_title('E.Pacific SST anomaly (K)')
    axes[1].plot(2*np.arange(nt),150*h,color='b')
    axes[1].set_title('W.Pacific thermocline depth (m)')
    plt.xlabel('Time (months)')
    plt.show()
main()
