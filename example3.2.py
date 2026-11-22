def relu(value):
    return max(0.0, value)

inputs = [2.0, 3.0]
weights = [0.5, 0.8]
bias = 0.2

weighted_sum = sum(
    x * w for x, w in zip(inputs, weights)
) + bias
output = relu(weighted_sum)

print(f"Weighted sum: {weighted_sum:.1f}")
print(f"Neuron output: {output:.1f}")

