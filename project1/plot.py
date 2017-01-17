import matplotlib.pyplot as plt
import numpy as np

def plot(T,h):
    
    f,axes=plt.subplots(2,1,sharex=True)
    axes[0].plot(2*np.arange(len(T)),7.5*T,color='r')
    axes[0].set_title('E.Pacific SST anomaly (K)')
    axes[1].plot(2*np.arange(len(T)),150*h,color='b')
    axes[1].set_title('W.Pacific thermocline depth (m)')
    plt.xlabel('Time (months)')
    plt.show()

