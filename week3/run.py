import datasets
import regression
import importlib

X ,Y = datasets.load_linear_example1()
print(X)
print(X[0])
print(Y)

# regression ver1
model = regression.LinearRegression()
print(model.x)

# regression ver2
importlib.reload(regression)
model.fit(X, Y)
print(model.theta)

# regression ver3
print(model.predict(X))

# regression ver4
print(model.score(X, Y))