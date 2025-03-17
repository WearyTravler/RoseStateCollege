#Pseudo Code

#1) Computer asks for Multiplier (W)
#2) Computer asks for Modulus (N)

#Method 1
# M1 = W^(N-2)%N

#Method 2
# M2 = Comparison

#Method 3
# M3 = W^W%N


#Sample Runthrough

#What is the Multiplier:
#What is the Modulus:

#Method 1 returns:
#Method 2 returns:
#Method 3 returns: 
#Another one? [y/n]:

import time

multiplier = int(input("What is the Multiplier (W): "))
modulus = int(input("What is the Modulus (N): "))
C = 1


# with open('multipliers.txt', 'r') as multipliers:
#     multiplier = multipliers.read().split()
#     multiplier = [int(x) for x in multiplier]
    
# with open('moduluses.txt', 'r') as moduluses:
#     modulus = moduluses.read().split()
#     modulus = [int(x) for x in modulus]


# results = [] 

#Method 1
method_1 = pow(multiplier,modulus-2,modulus)
print("Method 1 returns:", method_1)

#Method 2
modulus_set = []
multiplier_set = []
matching_values = []
NN = 1 
WW  = 0

while True:
    NN += modulus
    modulus_set.append(NN)
    WW += multiplier
    multiplier_set.append(WW)
    C += 1
    for item in modulus_set:
        if item in multiplier_set:
            matching_values.append(item)

    matching_indices = []

    for value in matching_values:
        index1 = modulus_set.index(value) # N
        index2 = multiplier_set.index(value) # W
        matching_indices.append((value, int(index1 +1), int(index2+1)))
    
    if matching_indices:
        print("Method 2 returns:", matching_indices)
        break
    else:
        continue


#Method 3 
method_3 = multiplier**multiplier % modulus
print("Method 3 returns:",method_3)
