import numpy
import tqdm
import numpy.random
from matplotlib import pyplot as plt

def post(x):
    return 1 / (2 * numpy.pi) ** 0.5 * numpy.exp(-1/2 * x ** 2.0)
   
#def post2(x):
#    return 1 / (2 * numpy.pi) ** 0.5 * numpy.exp(-1/2 * x ** 2.0) * numpy.sin(3 * x) ** 2.0

def proposal(x):
    return numpy.random.normal() + x

#def proposal2(x):
#    return numpy.random.uniform(-1, 1) + x
    
def mcmc(initial, post, prop, iterations):
    x = [initial]
    p = [post(x[-1])]
    for i in tqdm.tqdm(range(iterations)):
        x_test = prop(x[-1])
        p_test = post(x_test)

        acc = p_test / p[-1]
        u = numpy.random.uniform(0, 1)
        if u <= acc:
            x.append(x_test)
            p.append(p_test)
    return x, p
    
chain, prob = mcmc(10, post, proposal, 1000000)

plt.figure()
plt.title("Evolution of the walker")
plt.plot(chain)
plt.ylabel('x-value')
plt.xlabel('Iteration')

plt.figure()
plt.title("Evolution of the walker")
plt.plot(chain)
plt.xlim(0, 100)
plt.ylabel('x-value')
plt.xlabel('Iteration')

plt.figure()
plt.title("Posterior samples")
_ = plt.hist(chain[100::100], bins=100)

plt.show()
