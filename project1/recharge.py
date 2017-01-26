import numpy as np
import matplotlib.pyplot as plt
from schemes import *
from parameters import *
from plot import *
from annualcycle import *

def taskA():
    # Initial Conditions
    TOld = 1.125
    hOld = 0.
    mu0 = 2./3.
    
    
    T,h=rk4(TOld,hOld,mu0,nt=1000)
    
    tg = time_plot(T,h)
    pg = phase_plot(T,h)

    print(type(tg))
    print(type(pg))
    plt.show()
taskA()
def taskC():
    # Initial Conditions
    TOld = 1.125
    hOld = 0.
    mu0 = 2./3.
    
    
    T,h=rk4(TOld,hOld,mu0,nt=1000,epsilon=0.1)
    
    time_plot(T,h)
    phase_plot(T,h)


def taskD():
    # Initial Conditions
    TOld = 1.125
    hOld = 0
    nt = 1000
    mu0 = 0.75

    
    
    T,h=rk4(TOld,hOld,mu0=0.75,nt=nt,epsilon=0.1,mu_ann=0.2)
    
    time_plot(T,h)
    phase_plot(T,h)


def taskE():
    # Initial Conditions
    TOld = 1.125
    hOld = 0
    nt = 1000
    mu0 = 0.75

    
    
    T,h=rk4(TOld,hOld,mu0=0.75,nt=nt,epsilon=0.1,mu_ann=0.2,f_ann=0.02,f_ran=0.2)
    
    time_plot(T,h)
    phase_plot(T,h)
