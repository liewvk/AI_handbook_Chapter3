from sklearn.linear_model import LinearRegression

hours = [[1], [2], [3], [4]]
scores = [50, 60, 70, 80]

model = LinearRegression()
model.fit(hours, scores)

prediction = model.predict([[5]])[0]

print(f"Slope: {model.coef_[0]:.1f}")
print(f"Intercept: {model.intercept_:.1f}")
print(f"Predicted score for 5 hours: {prediction:.1f}")

