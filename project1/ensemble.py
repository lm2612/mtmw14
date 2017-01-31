from parameters import *
from schemes import *
import numpy as np
import matplotlib.pyplot as plt

def ensemble(Tmid, hmid, dT, dh, mu0, nt=1000,f_ann=0.,f_ran=0.,epsilon=0., mu_ann=0.):
    """ Perturbs T and h at start of each forecast in increments of dT and dh
around Tmid and hmid"""
    T = np.arange(Tmid-2*dT, Tmid+2*dT, dT)
    h = np.arange(hmid-2*dh, hmid+2*dh, dh)

    fig1 = plt.figure(1)
    plt.xlabel('time (months)')
    plt.ylabel('SST anomaly (K)')
    fig2 = plt.figure(2)
    plt.xlabel('SST anomaly (K)')
    plt.ylabel('thermocline height (m)')

    for iT in range(len(T)):
        for ih in range(len(h)):
            T0 = T[iT]
            h0 = h[ih]

            # Calculate T and h for this particular ensemble
            Tens,hens=rk4(T0,h0,mu0,nt,f_ann,f_ran,epsilon,mu_ann)

            # Add this SST to plot
            plt.figure(1)
            plt.plot(2.*dt*np.arange(nt),7.5*Tens)
            plt.figure(2)
            plt.plot(7.5*Tens,150*hens)
            

    
    plt.show()

ensemble(0.15,0.0,0.01,0.01,0.75,nt=120,f_ann=0.02,f_ran=0.2,epsilon=0.1,mu_ann=0.2)



