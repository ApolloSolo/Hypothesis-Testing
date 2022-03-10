import math
import pandas as pd
import numpy as np
import scipy.stats as st
from t_test_methods import T_Test

t_test = T_Test(70, 72, 5, 20, .05)
t_test.t_test()

flights = pd.read_csv('flights.csv', index_col=False)

flights_by_month = flights.groupby('MONTH')
#print(flights_by_month['DISTANCE'].aggregate(np.sum))

first_half = flights[flights['MONTH'] <= 6]
second_half = flights[flights['MONTH'] > 6]

first_half_dist = first_half['DISTANCE'].sum()
second_half_dist = second_half['DISTANCE'].sum()
print(first_half_dist, second_half_dist)
