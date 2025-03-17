

state_key = input("Give me the State Key: ")
#state_key = "851d527716b6a392d06f197d459b6206"
cipher_key = input("Give me the Cipher Key: ")
#cipher_key = "37893f6c4a127baf5d563c278a2261be"
# Convert hexadecimal strings to integers
state_int = int(state_key, 16)
cipher_int = int(cipher_key, 16)

# Perform XOR operation on 2 by 2 pairs
result_int = state_int ^ cipher_int

# Convert the result back to hexadecimal string
result_hex = format(result_int, '032x')

# Print the result
print(result_hex)