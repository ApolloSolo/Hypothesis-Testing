import matplotlib.pyplot as plt
import math
from scipy import stats
import numpy as np

STANDARD_NORM = stats.norm(0, 1)
# H_o: mu = 70
# H_a: mu > 70

alpha = .05

mean = 70
std = 4
n = 40
x = 73
z = (x - mean) / (std/math.sqrt(n))

# Upper tailed test takes z up to infinity
p_value = STANDARD_NORM.sf(z)

# Lower tailed test: takes -infinity up to the z value
# p_value_l = STANDARD_NORM.cdf(z)

if p_value < alpha:
    print("We can reject the H_o and accept the H_a hypothesis: (p = {} < alfa = {})".format(round(p_value, 4), alfa))
else:
    print("We cannot reject the H_o. More data may be needed: (p = {} > alfa = {})".format(round(p_value, 4), alfa))