import matplotlib.pyplot as plt
import dataset1
import numpy as np

x = np.linspace(-1, 1, 100)
y = dataset1.true_function(x)

df = dataset1.create_datasets()

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, color="blue", label="y = sin(pi * x * 0.8) * 10")
plt.scatter(df["観測値"], df["真値"], color="red", label="samples")

plt.legend()
plt.show()

