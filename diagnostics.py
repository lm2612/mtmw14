### Copy out most of this code. Code commented with 3#s (like this) ###
### is here to help you to learn python and need not be copied      ###

# Various function for plotting results and for calculating error measures

### The numpy package for numerical functions and pi                ###
import numpy as np

### The matplotlib package contains plotting functions              ###
import matplotlib.pyplot as plt

def plotSolution(x, phi):
    "Plot the solution during a simulation"
    font = {'size'   : 14}
    plt.rc('font', **font)
    plt.figure(2)
    plt.clf()
    plt.plot(x, phi)
    plt.ylim([-0.2,1.2])
    plt.xlabel('x')
    plt.ylabel('$\phi$')
    plt.axhline(0, linestyle=':', color='black')
    plt.axvline(0, linestyle=':', color='black')
    plt.draw()

def plotFinal(x, phi, phiExact, label, outFile):
    "Plot a final solution in comparison to the exact solution"
    # plot options (large fonts)
    font = {'size'   : 14}
    plt.rc('font', **font)
    
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(x, phiExact,'k', label='Exact')
    plt.plot(x, phi,     'r', label=label)
    plt.legend(loc='best')
    plt.xlabel('x')
    plt.ylabel('$\phi$')
    plt.axhline(0, linestyle=':', color='black')
    plt.savefig(outFile)

class errorDiagnostics(object):
    "Class for calculating various error diagnositcs from numerical"
    "and analytic solution over a grid"
    def __init__(self, grid, phi, phiExact):
        self.grid = grid
        self.phi = phi
        self.phiExact = phiExact
        self.phiError = phi - phiExact
        self.linf = np.max(np.abs(self.phiError))/np.max(np.abs(phiExact))

    def mean(self,phi):
        "Method to calculate the mean over the grid"
        return np.sum(phi*self.grid.dxs)/self.grid.length
    
    def stdDev(self,phi):
        "Method to calculate the standard deviation over the grid"
        return np.sqrt(np.sum((phi-self.mean(phi))**2 * self.grid.dxs)\
                      /self.grid.length)
        
    def l2(self):
       "Method to calculate the l2 error norm (RMS error)"
       return self.stdDev(self.phiError)/self.stdDev(self.phiExact)

    def write(self, name):
        "Method to write out the error diagnostics for this scheme"
        print "Scheme ", name
        print "l2 ", self.l2()
        print "linf ", self.linf
        print "mean ", self.mean(self.phi)
        print "stdDev ", self.stdDev(self.phi)

