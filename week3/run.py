import datasets
import regression

X ,Y = datasets.load_linear_example1()
print(X)
print(X[0])
print(Y)

model = regression.LinearRegression()
print(model.x)