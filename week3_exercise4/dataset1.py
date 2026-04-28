import numpy as np
import pandas as pd

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

def random_x():
    np.random.seed(0)
    return np.random.uniform(-1, 1, 20)

def create_datasets():
    x = random_x()
    y = true_function(x)

    df = pd.DataFrame({
        "観測値" : x,
        "真値" : y,
    })
    return df