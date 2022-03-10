import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np


class Normal_dist:

    def __init__(self, mu, sigma, n_observations):
        self.mu = mu
        self.sigma = sigma
        self.n_observations = n_observations
        self.s = np.random.normal(mu, sigma, n_observations)
        self.fig, self.ax = plt.subplots()

    def plot_norm(self, bins):
        self.bins = bins

        count, bins, ignored = plt.hist(self.s, self.bins, density=True)
        plt.plot(bins, 1 / (self.sigma * np.sqrt(2 * np.pi)) *
                 np.exp(- (bins - self.mu) ** 2 / (2 * self.sigma ** 2)),
                 linewidth=2, color='r')

        self.ax.set_xlabel('Germ Samples')
        self.ax.set_ylabel('Probability density')
        self.ax.set_title('Purity Distribution: mu={}, sigma={}'.format(self.mu, self.sigma))
        plt.show()


# Probability that rand observation will be less than a stated value
cdf_left_prob = norm(loc=48.472, scale=3.473).cdf(45)  # loc=mean, scale=sigma, cdf(stated value)
print("Probability below:", cdf_left_prob)

# Probability that rand observation will be greater than a stated value
cdf_right = norm(loc=48.472, scale=3.473).cdf(45)
cdf_right_prob = 1 - cdf_right
print("Probability above:", cdf_right_prob)

cdf_upper_limit = norm(loc=48.472, scale=3.473).cdf(55)
cdf_lower_limit = norm(loc=48.472, scale=3.473).cdf(44)
prob = cdf_upper_limit - cdf_lower_limit
print(prob)

inv_norm = norm.ppf(0.1, loc=48.472, scale=3.473)

