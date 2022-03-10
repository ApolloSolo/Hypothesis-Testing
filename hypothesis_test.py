from hypothesis_testing_methods import Hypothesis

        # Hypothesis(Ho_mu, Ho_sd, H1-Samples, H1_mu, alpha)
results = Hypothesis(70, 4, 40, 71, .05)

results.hypo_upper_tail()

print(results)
