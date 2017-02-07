from parameters import *
from schemes import *
import numpy as np
import matplotlib.pyplot as plt

def ensemble(Tmid, hmid, dT, dh, mu0, n_cycles=5,f_ann=0.,f_ran=0.,epsilon=0., mu_ann=0.):
    """ Perturbs T and h at start of each forecast in increments of dT and dh
around Tmid and hmid"""
    T = np.arange(Tmid-2*dT, Tmid+2*dT, dT)
    h = np.arange(hmid-2*dh, hmid+2*dh, dh)
    fig=plt.figure()
    ax1=plt.subplot(121)
    plt.xlabel('T (K)')
    plt.ylabel('h (m)')
    ax2=plt.subplot(222)
    plt.ylabel('T (K)')
    ax3=plt.subplot(224,sharex=ax2)
    plt.xlabel('Time (months)')
    plt.ylabel('h (m)')


    for iT in range(len(T)):
        for ih in range(len(h)):
            T0 = T[iT]
            h0 = h[ih]

            # Calculate T and h for this particular ensemble
            Tens,hens=rk4(T0,h0,mu0,n_cycles,f_ann,f_ran,epsilon,mu_ann)
            nt= int(round(n_cycles*42/(2*dt)))

            # Add this SST to plot
            ax1.plot(7.5*Tens,150*hens)
            ax2.plot(2.*dt*np.arange(nt),7.5*Tens)
            ax3.plot(2.*dt*np.arange(nt),150*hens)

            
    ax2.get_xaxis().set_visible(False)
    fig.set_size_inches(8,3)
    plt.show()
    




