def hard_knapsack(simple_knapsack, multiplier, modulus):
    # Calculate the Hadamard knapsack using the given multiplier and modulus
    hard_knapsack = [(multiplier * x) % modulus for x in simple_knapsack]
    return hard_knapsack

# Example values
simple_knapsack = [1, 2, 6]
multiplier = 11
modulus = 13

# Calculate the Hadamard knapsack
result = hard_knapsack(simple_knapsack, multiplier, modulus)

# Print the result
print("Original Knapsack:", simple_knapsack)
print("Multiplier:", multiplier)
print("Modulus:", modulus)
print("Hard Knapsack:", result)