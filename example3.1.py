hours = [1, 2, 3, 4]
actual_scores = [50, 60, 70, 80]

weight = 9
bias = 42

predictions = [weight * x + bias for x in hours]
errors_squared = [
    (actual - predicted) ** 2
    for actual, predicted in zip(actual_scores, predictions)
]
mse = sum(errors_squared) / len(errors_squared)

print("Predictions:", predictions)
print(f"Mean squared error: {mse:.2f}")

