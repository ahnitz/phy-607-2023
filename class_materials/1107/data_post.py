import h5py
import emcee
import corner
from matplotlib import pyplot as plt

import numpy
from numpy.random import uniform


f = h5py.File('./data.hdf', 'r')
x = f['data/xpos'][:]
y = f['data/ypos'][:]

order = 8
def model(x, params):
    return sum([c * x ** i for i, c in enumerate(params)])

def logposterior(parameters):
    return loglikelihood(parameters) + logprior(parameters)
    
# assume unit variance normal distributions
def loglikelihood(parameters):
    return - 0.5 * ((y - model(x, parameters)) ** 2.0).sum()
    
def logprior(parameters):
    # Assume unormalized uniform prior
    for p in parameters:
        if p > 20000 or p < -20000:
            return - numpy.inf
    return 0

# Creat the emcee sampler
sampler = emcee.EnsembleSampler(500, order, logposterior)

# Set the initial walker positions
initial_state = numpy.zeros((500, order))
initial_state += uniform(-10000, 10000, size=(500, order))

# Run the mcmc for 1000 iterations and get the resulting chain
state = sampler.run_mcmc(initial_state, 1000)
chain = sampler.get_chain()
logp = sampler.get_log_prob()

# Get the maximum posterior values from the final iteration of the mcmc chain
i = logp[-1,:].argmax()
maxp = chain[-1,i,:]
print(maxp)

plt.figure()
xref = numpy.arange(0, 1, .01)
plt.scatter(x, y, label='data')
plt.plot(xref, model(xref, maxp), label='max posterior fit',
         linewidth=4.0, color='orange')
plt.legend()

_ = corner.corner(chain[-1,:,:])
plt.show()
