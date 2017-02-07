import numpy as np
from parameters import *

def annualcycle(mu0,mu_ann,it):
    t=it*dt
    mu = mu0* ( 1 + mu_ann * np.cos( (2.*np.pi*t)/tau - (5.*np.pi)/6.) )

    return mu

import matplotlib.pyplot as plt
def plot_annualcycle(mu0,mu_ann,nt):
    mu=np.zeros(nt)
    mu[0]=mu0
    for it in range(1,nt):
        mu[it]=annualcycle(mu0,mu_ann,it)
    plt.plot(2*dt*np.arange(nt),mu)
    plt.xlabel("Time(months)")
    plt.ylabel("Coupling parameter")
    plt.show()
        
#plot_annualcycle(0.75,0.2,800)
