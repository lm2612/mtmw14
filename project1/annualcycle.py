import numpy as np
from parameters import *

def annualcycle(mu0,mu_ann,it):    
    mu = mu0*(1+mu_ann*np.cos(2*np.pi*it*dt/tau - 5*np.pi/6) )

    return mu
