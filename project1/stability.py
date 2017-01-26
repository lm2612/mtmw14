import cmath
import numpy as np
from parameters import *


def stability_rk4(mu):
    """ Checks stability of RK4 for this value of mu in absence of non-linearity
    and wind stress"""
    b = b0*mu
    R = gamma*b-c
    M = np.array([[R,gamma],[-alpha*b, -r]])
    print(M)

    eigenvalues,eigenvectors = np.linalg.eig(M)
    print(eigenvalues)


def analytical_stability(mu):
    """ Tests analytical stability of equations for mu in absence of non-linearity
    and wind stress """

    # Derived parameters
    b = b0*mu
    R = gamma*b-c

    
def analytic_stability(r=0.25, Y=0.75, b0=2.5, c=1, a=0.125, mu=2./3.):
    "Stability of the analytic solution for the linear recharge oscillator"

    b = b0*mu
    R = Y*b-c

    
    evals_pos = 0.5*((R-r) + cmath.sqrt((r-R)**2-4*(Y*a*b-R*r)))
    evals_neg = 0.5*((R-r) - cmath.sqrt((r-R)**2-4*(Y*a*b-R*r)))

    return evals_pos,evals_neg

analytic_stability()

def max_stable_timestep(r=0.25, Y=0.75, b0=2.5, c=1, a=0.125, mu=2./3.):

    evals_pos,evals_neg=analytic_stability(r, Y, b0, c, a, mu)
    



    
    
