import pandas as pd
import statistics
import math
import numpy as np
from t_test_2_methods import T_Test_Two_Sample


# Determine Hypothesis
# H_0: mu_1 - mu_2 = 0
# H_a: mu_1 - mu_2 != 0

db = pd.read_excel('Statistics.xlsx')

#db.dropna(axis=0, how="any", inplace=True)

germ_2017 = db[2017]
germ_2018 = db[2018]

alpha = .01

germ_2017_mean = germ_2017.mean()
germ_2017_sd = germ_2017.std()
n1 = 197

germ_2018_mean = germ_2018.mean()
germ_2018_sd = germ_2018.std()
n2 = germ_2018.size

t_test = T_Test_Two_Sample(germ_2017_mean, germ_2017_sd, n1, germ_2018_mean, germ_2018_sd, n2, alpha)

t_test.t_test_2_sample()

germ_2018_interval = t_test.confidence_interval(germ_2018_mean, germ_2018_sd, 55.2, 44)
germ_2017_interval = t_test.confidence_interval(germ_2017_mean, germ_2017_sd, 52.6707, 38.2125)

germ_17_interval = t_test.inv_norm(.975, germ_2017_mean, germ_2017_sd)
germ_17_interval = t_test.inv_norm(.025, germ_2017_mean, germ_2017_sd)

germ_18_interval = t_test.inv_norm(.975, germ_2018_mean, germ_2018_sd)
germ_18_interval = t_test.inv_norm(.025, germ_2018_mean, germ_2018_sd)

