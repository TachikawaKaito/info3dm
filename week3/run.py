import datasets
import regression
import importlib

X ,Y = datasets.load_linear_example1()
print(X)
print(X[0])
print(Y)

model = regression.LinearRegression()
print(model.x)

importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X, Y)
print(model.theta)