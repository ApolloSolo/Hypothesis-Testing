import math
from scipy.stats import norm
import scipy.stats as st


# Hypothesis
# H_0: mu_1 = 70
# H_a: mu_1 > 70

# alpha = .05
# mu = 70

# sample_mean = 68
# sample_std = 5
# n = 20

class T_Test:

    def __init__(self, mu, sample_mean, sample_std, n, alpha):

        self.mu = mu
        self.sample_mean = sample_mean
        self.sample_std = sample_std
        self.n = n
        self.alpha = alpha

        # Make t-distribution

    def t_test(self):
        dof = self.n - 1
        t_dist = st.t(dof)

        # Compute t-statistic
        t = (self.sample_mean - self.mu) / (self.sample_std / math.sqrt(self.n))

        # p_value
        if self.sample_mean > self.mu:
            p_value = t_dist.sf(t)  # p_value = 1-t_dist.sf(t) for left tail
        else:
            p_value = 1 - t_dist.sf(t)

        if p_value < self.alpha:
            print('We can reject the null and accept the alt hypothesis: (p = {} < alpha = {})'.format(p_value,
                                                                                                       self.alpha))
        else:
            print(
                'We cannot reject the null. More data may be needed. (p = {} > alpha = {})'.format(p_value, self.alpha))


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
