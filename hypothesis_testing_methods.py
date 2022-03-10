import math
from scipy import stats
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox


class Hypothesis:

    def __init__(self, mean, std, n, x, alpha):
        self.mean = mean
        self.std = std
        self.n = n
        self.x = x
        self.alpha = alpha
        self.STANDARD_NORM = stats.norm(0, 1)

    def hypo_upper_tail(self):
        z = (self.x - self.mean) / (self.std / math.sqrt(self.n))
        # Upper tailed test takes z up to infinity
        p_value = self.STANDARD_NORM.sf(z)
        # Lower tailed test: takes -infinity up to the z value
        # p_value_l = STANDARD_NORM.cdf(z)
        if p_value < self.alpha:

            window = Tk()
            window.geometry("50x50")

            messagebox.askretrycancel(
                "Application", "We can reject the Null Hypothesis and accept the Alternative Hypothesis:"
                "\nH0: μ0 = μ1\nH1: μ0 < μ1\nμ0 = {}\nσ = {}\nμ1 = {}\n"
                "Sample Size = {}"
                "\n(p = {} < alpha = {})"
                .format(self.mean, self.std, self.x, self.n, round(p_value, 8), self.alpha,)
            )

            window.mainloop()
        else:

            window = Tk()
            window.geometry("50x50")
            messagebox.askretrycancel(
                "Application", "We cannot reject the Null Hypothesis. More data may be needed:"
                "\nH0: μ0 = μ1\nH1: μ0 < μ1\nμ0 = {}\nσ = {}\nμ1 = {}\n"
                "Sample Size = {}"
                "\n(p = {} < alpha = {})"
                .format(self.mean, self.std, self.x, self.n, round(p_value, 8), self.alpha, )
            )
            window.mainloop()

    def hypo_lower_tail(self):
        z = (self.x - self.mean) / (self.std / math.sqrt(self.n))
        # Upper tailed test takes z up to infinity
        p_value = 1 - self.STANDARD_NORM.sf(z)
        # Lower tailed test: takes -infinity up to the z value
        # p_value_l = STANDARD_NORM.cdf(z)
        if p_value < self.alpha:

            window = Tk()
            window.geometry("50x50")
            messagebox.askretrycancel(
                "Application", "We can reject the Null Hypothesis and accept the Alternative Hypothesis:"
                "\nH0: μ0 = μ1\nH1: μ0 > μ1\nμ0 = {}\nσ = {}\nμ1 = {}\n"
                "Sample Size = {}"
                "\n(p = {} < alpha = {})"
                .format(self.mean, self.std, self.x, self.n, round(p_value, 8), self.alpha, )
            )
            window.mainloop()

        else:
            window = Tk()
            window.geometry("50x50")
            messagebox.askretrycancel(
                "Application", "We cannot reject the Null Hypothesis. More data may be needed:"
                "\nH0: μ0 = μ1\nH1: μ0 > μ1\nμ0 = {}\nσ = {}\nμ1 = {}\n"
                "Sample Size = {}"
                "\n(p = {} < alpha = {})"
                .format(self.mean, self.std, self.x, self.n, round(p_value, 8), self.alpha, )
            )
            window.mainloop()

    def hypo_two_tail(self):
        z = (self.x - self.mean) / (self.std / math.sqrt(self.n))
        # Upper tailed test takes z up to infinity

        if self.x > self.mean:
            p_value = self.STANDARD_NORM.sf(z)*2
        else:
            p_value = abs((1 - self.STANDARD_NORM.sf(z))*2)

        # Lower tailed test: takes -infinity up to the z value
        # p_value_l = STANDARD_NORM.cdf(z)
        if p_value < self.alpha:

            window = Tk()
            window.geometry("50x50")
            messagebox.askretrycancel(
                "Application", "We can reject the Null Hypothesis and accept the Alternative Hypothesis:"
                "\nH0: μ0 = μ1\nH1: μ0 ≠ μ1\nμ0 = {}\nσ = {}\nμ1 = {}\n"
                "Sample Size = {}"
                "\n(p = {} < alpha = {})"
                .format(self.mean, self.std, self.x, self.n, round(p_value, 8), self.alpha, )
            )

            window.mainloop()

        else:
            window = Tk()
            window.geometry("50x50")
            messagebox.askretrycancel(
                "Application", "We cannot reject the Null Hypothesis. More data may be needed:"
                "\nH0: μ0 = μ1\nH1: μ0 ≠ μ1\nμ0 = {}\nσ = {}\nμ1 = {}\n"
                "Sample Size = {}"
                "\n(p = {} > alpha = {})"
                .format(self.mean, self.std, self.x, self.n, round(p_value, 8), self.alpha, )
            )
            window.mainloop()

    def plot(self):

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        section = ['Ho-Mean', 'SD', 'N', 'X-Bar', 'alpha']
        values = [self.mean, self.std, self.n, self.x, self.alpha]
        ax.bar(section, values)
        plt.show()
