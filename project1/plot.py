import matplotlib.pyplot as plt
import numpy as np
from parameters import *

def plot(T,h):
    
    f,axes=plt.subplots(2,1,sharex=True)
    axes[0].plot(2*dt*np.arange(nt),7.5*T,color='r')
    axes[0].set_title('E.Pacific SST anomaly (K)')
    axes[1].plot(2*dt*np.arange(nt),150*h,color='b')
    axes[1].set_title('W.Pacific thermocline depth (m)')
    plt.xlabel('Time (months)')
    plt.show()

