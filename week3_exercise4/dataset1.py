import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import unittest
import japanize_matplotlib


def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

def random_x():
    np.random.seed(0)
    return np.random.uniform(-1, 1, 20)

def create_datasets():
    x = random_x()
    y = true_function(x)

    df = pd.DataFrame({
        "観測点" : x,
        "真値" : y,
    })
    return df

class TestTrueFunction(unittest.TestCase):
    def test_x_0(self):
        y = true_function(0)
        self.assertAlmostEqual(y, 0)

if __name__ == "__main__":

    # 演習1.1

    # テスト
    unittest.main(exit=False)

    x = np.linspace(-1, 1, 100)
    y = true_function(x)

    plt.figure(figsize=(8,5))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, color="blue", label=r"$y = \sin(0.8 \pi x) \times 10$")
    plt.legend(loc="best")
    plt.savefig("week3_exercise4/ex1.1.png")

    plt.show()


    # 演習1.2
    x = np.linspace(-1, 1, 100)
    y = true_function(x)

    df = create_datasets()

    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, color="blue", label=r"$y = \sin(0.8 \pi x) \times 10$")
    plt.scatter(df["観測点"], df["真値"], color="red", label="samples")
    plt.legend()
    plt.savefig("week3_exercise4/ex1.2.png")

    plt.show()

    # 演習1.3

    x = np.linspace(-1, 1, 100)
    y = true_function(x)

    df = create_datasets()

    noise = np.random.normal(loc=0.0, scale=np.sqrt(2.0), size=20)
    noise_half = noise * 0.5

    df["観測値"] = df["真値"] + noise_half

    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, color="blue", label=r"$y = \sin(0.8 \pi x) \times 10$")
    plt.scatter(df["観測点"], df["真値"], color="red", label="samples")
    plt.scatter(df["観測点"], df["観測値"], color="green", label="観測値")
    plt.legend()
    plt.savefig("week3_exercise4/ex1.3.png")

    plt.show()