import numpy as np
from parameters import *

def windstress(f_ann,f_ran,it,W):
    """ Returns xi and W (so that W can be re-used in future xi """
    # Update W every tau_cor timesteps (i.e. when time mod tau_cor is zero)

    if ((it*dt)%(tau_cor)<=(10**(-7))):    # need some tolerance to avoid round-off errors
        W = (np.random.randint(-1e5,1e5))/(1e5)

    xi = f_ann*np.cos(2*np.pi*it*dt/tau) + f_ran*W*tau_cor/delta_t
    
    return xi,W

def annualcycle(mu0,mu_ann,it):
    t=it*dt
    mu = mu0* ( 1 + mu_ann * np.cos( (2.*np.pi*t)/tau - (5.*np.pi)/6.) )

    return mu

def R_b_xi(f_ann,f_ran,mu0,mu_ann,W,it):
    """Calculates parameters R, b and xi at this timestep """
    xi,W = windstress(f_ann,f_ran,it,W)
    mu = annualcycle(mu0,mu_ann,it)

    b = b0*mu
    R = gamma*b - c

    return R,b,xi,W
