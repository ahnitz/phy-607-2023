import h5py
import numpy

f = h5py.File('./data.hdf', 'r')
x = f['data/xpos'][:]
y = f['data/ypos'][:]

def f(x, params):
    (a, b, c, d, e, f, g, h) = params
    return a *  (x - b) * (x - c) * (x - d) * (x - e) * (x - f) * (x - g) * (x - h)
    

def logposterior(parameters):
    return loglikelihood(parameters) + logprior(parameters)
    
# assume unit variance normal distributions
def likelihood(parameters):
    return - 0.5 * (y - model(x, parameters)) ** 2.0
    
def logprior(parameters):
    # Assume unormalized uniform prior
    a = parameters[0]
    r = parameters[1:]
    
    if a > 1000 or a < 0:
        return - numpy.inf
    for p in parameters:
        if p > 2 or p < 0:
            return - numpy.inf
    return 0
    

