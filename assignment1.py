import numpy as np
import matplotlib.pyplot as plt
from advectionSchemes import *
from initialConditions import *
from diagnostics import *

def main():
    """ Advect pollutant"""

    # Parameters
    xmin = 0
    xmax = 25600
    nx = 100.
    u = 80.   # wind speed = 80km/hr
    dt = 2.   # look at 2 hr intervals
    nt = 160   # time T to travel full revolution (T=25600/80=320, nt=T/dt)
    k = 540
    
    # Derived parameters
    dx = (xmax - xmin)/nx
    c = (u*dt)/dx
    x = np.arange(xmin, xmax, dx)
    d = 0.5 * k / (dx**2)

    # Initial Conditions
    qOld = squareWave(x,0,5120)     # 1 between 0 and 5120km, 0 else

    # Advect
    q = CTCS(qOld, c, nt, d=d)

    # Calculate exact solution
    qExact = squareWave((x-u*nt*dt)%(xmax-xmin),0,5120)

    plotFinal(x, q, qExact, 'CTCS, 320hrs', '/Users/lm2612/Documents/mtmw14/diffusion160.pdf')
    

main()
