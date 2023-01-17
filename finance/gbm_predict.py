import numpy as np


def GBM_predict(s0, mu, sigma, paths, days):
	dt = 1 #will change this in later iterations
	# make all the randoms first (simple GBM so we can do this in one step)
	# also multiply each by the dt and the drift and sigma factors 
	randoms = np.random.normal(0,1, size=(paths, days))*dt*(mu - 0.5*sigma**2)
	prices = np.zeros((paths, days+1))
	prices[:,0] = s0
	prices[:,1:] = np.exp(np.cumsum(randoms, axis=1))*s0
	return prices
