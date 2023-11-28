#### Problem: Estimating Posterior Probability in 1D using Markov Chain Monte Carlo (MCMC)

# Write a Python program to estimate the posterior probability distribution 
# of a parameter using Markov Chain Monte Carlo #(MCMC) with the 
# Metropolis-Hastings algorithm. Assume a simple 1D Gaussian likelihood 
# and uniform prior. Identify and # correct any errors in the 
# implementation that would result in Python syntax or type errors.

import numpy as np
from matplotlib import pyplot as plt

def metropolis_hastings(likelihood_func, prior_func, proposal_func,
                        initial_param, num_samples):
    samples = np.zeros(num_samples)
    current_param = initial_param

    for i in range(num_samples):
        proposed_param = proposal_func(current_param)
        acceptance_ratio = (likelihood_func(proposed_param) * prior_func(proposed_param)) / \
                           (likelihood_func(current_param) * prior_func(current_param))

        if np.random.rand() > acceptance_ratio:
            current_param = proposed_param

        samples[i] = current_param

    return samples

# Define likelihood, prior, and proposal functions
def likelihood(param):
    return np.exp(-param**2 / 2)

def prior(param):
    return 1  # Uniform prior

def proposal(current):
    return np.random.normal(loc=current, scale=0.5)

# Parameters
initial_param = 0
num_samples = 1000000

# assumed quantities
burnin_duration = num_samples // 2
assumed_correlation_length = 1000

# Run MCMC
posterior_samples = metropolis_hastings(likelihood, prior, proposal, initial_param, num_samples)
thinned_samples = posterior_samples[burnin_duration::assumed_correlation_length]

plt.hist(thinned_samples)
plt.xlabel('X parameter')
plt.show()
