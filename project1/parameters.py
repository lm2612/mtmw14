def parameters():
    """Initialises parameters"""
    # Parameters
    forcing = 0
    epsilon = 0
    b0 = 2.5
    mu = 2./3.
    gamma = 0.75
    c = 1.
    r = 0.25
    alpha = 0.125
    dt = 0.5
    nt = 100


    # Derived Parameters
    b = b0*mu
    R = gamma*b - c
