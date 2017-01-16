# Numerical schemes for simulating linear advection for outer code
# linearAdvect.py 

from __future__ import absolute_import, division, print_function

import numpy as np
import numpy.linalg as la

def FTCS(phiOld, c, nt):
    "Linear advection of profile in phiOld using FTCS, Courant number c"
    "for nt time-steps"

    nx= len(phiOld)

    # new time-step array for phi
    phi = phiOld.copy()

    # FTCS for each timestep
    for it in range(nt):
        for j in range(nx):
            # calculate phi at j
            # use modolo % for periodic BC
            phi[j] = phiOld[j] - 0.5*c*(phiOld[(j+1)%nx] - phiOld[(j-1)%nx])

        # update array:
        phiOld = phi.copy()
    return phi
            
def FTBS(phiOld, c, nt):
    """ Linear advection  of phi using FTBS (forward time, backward space) """
    """ for Courant number c, for nt time-steps """
    nx= len(phiOld)

    # new time-step array for phi
    phi = phiOld.copy()

    # FTBS for each timestep:
    for it in range(nt):
        for j in range(nx):
            # calculate phi at j
            # use modolo % for periodic BC
            phi[j] = phiOld[j] - c*(phiOld[j]-phiOld[(j-1)%nx])

        # update array
        phiOld = phi.copy()

    return phi
                                        
def CTCS(phiOld, c, nt,phi2=None, d=0):
    """ Linear advection of phi using CTCS (central time, central space) """
    """ for Courant number c, for nt time-steps , d is artificial diffusion coeff"""

    # First find number of spatial steps from the initial phi given:
    nx = len(phiOld)
    # If nt = 0, need to return phiOld
    if nt == 0:
        return phiOld
    else:
        if phi2 is not None:
            phi = phi2.copy()
            time = nt
        elif phi2 is None:
            # Calculate the first value of phi using FTCS
            phi = FTCS(phiOld.copy(), c, 1)
            time = nt-1

        # Create new time-step array for phiNew
        phiNew=phi.copy()

        # Now we have two values of phi, can calculate future values with CTCS
        for it in range(time):
            for j in range(nx):
                # calculate phiNew at j using points phiOld[j] and phi[j+1] and phi[j-1]
                # use % for periodic BC
                phiNew[j] = phiOld[j] - c*(phi[(j+1)%nx]-phi[(j-1)%nx]) + 2*d*(phiOld[(j+1)%nx] -2*phiOld[j] +phiOld[(j-1)%nx])

            # Update arrays:
            phiOld = phi.copy()
            phi = phiNew.copy()

        return phi



def BTCS(phiOld, c, nt):
    """ Linear advection of phi using BTCS (backward time, central space) """
    """ for Courant number c, for nt time-steps """

    # First find number of spatial steps from initial phi:
    nx = len(phiOld)

    # BTCS is an IMPLICIT scheme, so we need to solve equation in form M phi = phiOld
    # First create array M which is an nx by nx matrix with all diagonals=1
    # upper diagonals = c/2 and lower diagonals = -c/2
    # periodic boundary conditions come from %nx (top right element=-c/2, bottom left = c/2)
    # all other terms remain 0


    M = np.zeros((nx,nx))
    for nxi in range(nx):
        M[nxi,nxi]=1. 
        M[nxi,(nxi+1)%nx]=c/2.
        M[(nxi+1)%nx,nxi]=-c/2.


    for it in range(nt):
        # doesn't require loop over j as this is done all in one step with matrix algebra
        # solution of M phi = phiOld
        phiOld = la.solve(M,phiOld)


    return phiOld



def LaxWendroff(phi_ahead, phi_behind, c):
    """Calculates phi in centre of grid box for phi_ahead being front edge of box """
    """ and phi_behind being back edge of box, courant number = c and nx is no. of spatial steps"""
    
    phi_centre = 0.5*(1+c)*phi_behind + 0.5*(1-c)*phi_ahead

    return phi_centre

def limiter(phi_behind,phi,phi_ahead):
    """Calculates limiter function phi at point using Van Leer limiter, required for TVD"""
    if phi_ahead-phi == 0.:
        return 2.                          # in this case psi will tend to 2
    r= (phi-phi_behind)/(phi_ahead-phi)    # ratio of upwind to local gradient
    psi=(r+abs(r))/(1+abs(r))
    return psi

    
def tvd(phiOld, c, nt):
    """ Linear Advection of phi using Lax Wendroff for smoothly varying parts of solution"""
    """ and upwind scheme for quickly varying parts for courant number c for nt timesteps"""
    
    # First find number of spatial steps from initial phi:
    nx = len(phiOld)

    # New timestep
    phi = phiOld.copy()

    
    #  for each timestep:
    for it in range(nt):
        for j in range(nx):
            # calculate phi at j
            # use modolo % for periodic BC

            # calculate limiter function psi at point j-1/2
            psi=limiter(phiOld[(j-2)%nx],phiOld[j-1],phiOld[(j)%nx])
            # calculate higher and lower order fluxes:
            if c>=0:
                phiL = phiOld[(j-1)%nx]
            else:
                phiL = phiOld[(j)%nx]
            
            phiH= LaxWendroff(phiOld[j],phiOld[(j-1)%nx],c)
            phi_jminushalf = psi*phiH + (1-psi)*phiL

            # calculate limiter function psi at point j+1/2
            psi=limiter(phiOld[(j-1)%nx],phiOld[j],phiOld[(j+1)%nx])
            # calculate higher and lower order fluxes:
            if c>=0:
                phiL = phiOld[(j)%nx]
            else:
                phiL = phiOld[(j+1)%nx]
            phiH= LaxWendroff(phiOld[(j+1)%nx], phiOld[j],c)
            phi_jplushalf = psi*phiH + (1-psi)*phiL

            # calculate phi at next timestep using phi at old timestep at points j, j+1/2 and j-1/2
            phi[j] = phiOld[j] - c*( phi_jplushalf - phi_jminushalf)

        # update array:
        phiOld = phi.copy()

    return phi
            
