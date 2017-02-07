import matplotlib.pyplot as plt
import numpy as np
from parameters import *

def time_plot(T,h,axes=None):
    if axes == None:
        fig,axes=plt.subplots(2,1,sharex=True)
    axes[0].plot(2*dt*np.arange(len(T)),7.5*T,color='r')
    axes[0].set_title('T (K)',fontsize=10)
    axes[0].get_xaxis().set_visible(False)
    axes[1].plot(2*dt*np.arange(len(h)),150.*h,color='b')
    axes[1].set_title('h (m)',fontsize=10)
    plt.ymax=10
    plt.ymin=-10.
    plt.xlabel('Time (months)')
    

def phase_plot(T,h,ax=None):
    if ax==None:
        fig,ax=plt.subplots()
    ax.plot(7.5*T,150.*h)
    plt.xlabel('T (K)')
    plt.ylabel('h (m)')

def time_and_phase(T,h):
    fig=plt.figure()
    
    ax1=plt.subplot(121)
    phase_plot(T,h,ax1)
    
    ax2=plt.subplot(222)
    ax3=plt.subplot(224,sharex=ax2)
    time_plot(T,h,axes=[ax2,ax3])
    fig.set_size_inches(6,2.5)
    plt.show()



