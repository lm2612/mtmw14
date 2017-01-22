import numpy as np
from parameters import *

def windstress(f_ran,f_ann,it):

    W = (np.random.randint(-1e5,1e5))/(1e5)

    xi = f_ann*np.cos(2*np.pi*it*dt/tau) + f_ran*W*tau_cor/delta_t
    return xi
