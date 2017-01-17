import numpy as np

def scheme(T0,h0,nt,dt,R,alpha,b,r,gamma):
    """Forward in time for T and backward in time for h. Returns arrays
    of length nt of T,h for each timestep
    Arguments:
        T: initial condition for T
        h: initial condition for h
        nt: number of iterations
        dt:
        R:
        alpha:
        b:
        r:
        gamma:
        """
    # Initialise arrays:
    T = np.zeros(nt)
    h = np.zeros(nt)
    T[0] = T0
    h[0] = h0
    
    for it in range(1,nt):
        T[it] = (1+R*dt)*T[it-1] + dt*gamma*h[it-1]
        h[it] = (h[it-1] - dt*alpha*b*T[it])/(1+r*dt)

    return T,h
