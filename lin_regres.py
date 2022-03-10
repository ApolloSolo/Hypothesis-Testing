import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

flights = pd.read_csv('flights.csv', index_col=False)

# Get a sample of flights data with pandas sample()

flights_subsample = flights.sample(1000)
print(flights_subsample)
# Plot a scatter plot
# plt.scatter(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME'])
# plt.show()

# Do the regression
slope, intercept, r_value, _, _ = linregress(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME'])
print('y = {}x + {} r value: {}'.format(slope, intercept, r_value))

# Plot scatter plot
plt.scatter(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME'])

# Make x values to feed into linear equation
x = np.linspace(flights_subsample['DISTANCE'].min(), flights_subsample['DISTANCE'].max())
y = slope * x + intercept
plt.plot(x, y, 'r--')
plt.show()

# Example
distance = 5000
flight_time = slope * distance + intercept
print(flight_time)