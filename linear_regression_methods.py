import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


class Linear_regress:
    def __init__(self,file_path):
        self.file_path = file_path

    def get_data(self):
        pd.read_csv(self.file_path, index_col=False)
