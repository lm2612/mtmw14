### Copy out most of this code. Code commented with 3#s (like this) ###
### is here to help you to learn python and need not be copied      ###

### The numpy package for numerical functions and pi                ###
import numpy as np

# Various different initial conditions for linear advection

def cosBell(x):
    "Function defining a cosine bell as a function of position, x"
### The lambda keyword lets you define a function in one line       ###
    bell = lambda x: 0.5*(1 - np.cos(4*np.pi*x))
### chooses bell(x) where condition is true, else chooses zeros     ###
    return np.where((x<0.5) | (x>=1.0), bell(x), 0.)

def squareWave(x):
    "Function defining a square wave as a function of position, x"
    return np.where((x<0.5) | (x>=1.0), 1., 0.)

def mixed(x):
    "A flat peak in one location and a cosine bell in another"
    return np.where((x >= 0.2) & (x <= 0.3), 1, \
                    np.where((x >= 0.4) & (x <= 0.8), \
                    0.5*(1 + np.cos(5*np.pi*(x-0.6))),
                    np.where((x > 0.1) & (x < 0.2), 10*(x-0.1), 
                    np.where((x > 0.3) & (x < 0.35), 20*(0.35-x), 0))))

