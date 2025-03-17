# Define the Permuted Choice 1 (PC-1) table
pc1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# Function to convert ASCII to binary
def ascii_to_binary(key):
    binary_key = ''.join(format(ord(char), '08b') for char in key)
    return binary_key

# Function to apply PC-1 permutation
def apply_pc1(binary_key):
    pc1_key = [binary_key[i - 1] for i in pc1]
    return ''.join(pc1_key)

# Input ASCII key
ascii_key = "MoreKey"

# Convert ASCII key to binary
binary_key = ascii_to_binary(ascii_key)

# Apply PC-1 permutation
pc1_result = apply_pc1(binary_key)

# Convert the 56-bit result to hex
pc1_hex_key = '-'.join([hex(int(pc1_result[i:i + 8], 2))[2:].upper() for i in range(0, len(pc1_result), 8)])

print(pc1_hex_key)


pc1_result = apply_pc1(binary_key)

# Convert the 56-bit result to hex
pc1_hex_key = '-'.join([hex(int(pc1_result[i:i + 8], 2))[2:].upper() for i in range(0, len(pc1_result), 8)])

print(pc1_hex_key)
