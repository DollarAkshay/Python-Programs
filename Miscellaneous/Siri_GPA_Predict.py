import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = [8.92, 9.00, 8.43, 8.57, 8.27]
y = [1, 2, 3, 4, 5]
model = LinearRegression()
x_full = np.hstack([x, x**2])
model.fit(x_full, y)
print("Model Coefficients : ", model.coef_.flatten())
print("Model Interrcept : ", model.intercept_[0])
