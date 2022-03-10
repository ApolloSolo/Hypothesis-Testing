import math
import scipy.stats as st
from scipy.stats import norm


class T_Test_Two_Sample:

    def __init__(self, sample1_mean, sample1_std, n1, sample2_mean, sample2_std, n2, alpha):
        self.sample1_mean = sample1_mean
        self.sample1_std = sample1_std
        self.n1 = n1
        self.sample2_mean = sample2_mean
        self.sample2_std = sample2_std
        self.n2 = n2
        self.alpha = alpha

    def t_test_2_sample(self):
        # Construct t-distribution
        dof = self.n1 + self.n2 - 2
        t_dist = st.t(dof)

        # Calc t and S pooled
        sp = math.sqrt((((self.n1 - 1) * self.sample1_std ** 2) + ((self.n2 - 1) * self.sample2_std ** 2))
                       / dof)
        t = (self.sample1_mean - self.sample2_mean) / (sp * (math.sqrt((1 / self.n1) + (1 / self.n2))))

        # p_value
        p_value = 2 * t_dist.sf(abs(t))

        print(t, p_value)
        if p_value < self.alpha:
            print('We can reject the null and accept the alt hypothesis: (p = {} < alpha = {})'.format(p_value,
                                                                                                       self.alpha))
        else:
            print(
                'We cannot reject the null. More data may be needed. (p = {} > alpha = {})'.format(p_value, self.alpha))

    def confidence_interval(self, mean, sd, upper_limit, lower_limit):
        cdf_upper = norm(loc=mean, scale=sd).cdf(upper_limit)
        cdf_lower = norm(loc=mean, scale=sd).cdf(lower_limit)
        interval = cdf_upper - cdf_lower
        print(interval)
        return interval
    def inv_norm(self, percent, mean, sd):
        inv_norm = norm.ppf(percent, loc=mean, scale=sd)
        print(inv_norm)
        return inv_norm

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

#inv_norm = norm.ppf(0.1, loc=48.472, scale=3.473)
