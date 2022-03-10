from normal_distribution_methods import Normal_dist

             # Normal_dist(mu, sigma, samples)
distribution = Normal_dist(48.5, 3.47, 500)

          # .plot_norm(number of bins)
distribution.plot_norm(50)
