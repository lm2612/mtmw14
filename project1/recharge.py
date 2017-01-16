import numpy as np
import matplotlib.pyplot as plt


def main():
    # Initial Conditions
    TOld = 1.125
    hOld = 0.
    
    # Parameters
    forcing = 0
    epsilon = 0
    b0 = 2.5
    mu = 2./3.
    feedback = 0.75
    c = 1.
    r = 0.25
    alpha = 0.125
    dt = 0.5
    nt = 100


    # Derived Parameters
    b = b0*mu
    R = feedback*b - c

    # Initialise:
    T = np.zeros(nt)
    h = np.zeros(nt)
    T[0] = TOld
    h[0] = hOld
    
    # Iterate:
    for it in range(1,nt):
        T[it] = (1+R*dt)*T[it-1] + dt*feedback*h[it-1]
        h[it] = (h[it-1] - dt*alpha*b*T[it])/(1+r*dt)

    plt.plot(np.arange(nt),T)
    plt.plot(np.arange(nt),h)
    plt.show()
main()
