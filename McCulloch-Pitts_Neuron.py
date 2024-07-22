def mcCulloch_pitts_nor(x1, x2, x3, weights, threshold):
    # Compute the weighted sum
    weighted_sum = x1 * weights[0] + x2 * weights[1] + x3 * weights[2]

    # Apply the threshold to determine the output
    if weighted_sum <= threshold:
        return 1
    else:
        return 0


# Weights for the inputs
weights = [1, 1, -1]

# Determine the threshold
# Since the maximum sum for x1, x2, x3 when inputs are 0 is 0,
# and for any other combination should give a negative result,
# the threshold can be set to 0.

threshold = 0

# Test the NOR gate with all possible inputs
test_inputs = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]

# Print the results
print("NOR Gate Output:")
for inputs in test_inputs:
    x1, x2, x3 = inputs
    output = mcCulloch_pitts_nor(x1, x2, x3, weights, threshold)
    print(f"Input: ({x1}, {x2}, {x3}) -> Output: {output}")
