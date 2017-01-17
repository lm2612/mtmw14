import numpy as np
import matplotlib.pyplot as plt
from schemes import *
from parameters import *
from plot import *

def main():
    # Initial Conditions
    TOld = 1.125
    hOld = 0.
    
    
    T,h=rk4(TOld,hOld)
    
    plot(T,h)
main()
