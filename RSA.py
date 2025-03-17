#!/usr/bin/python3

p = int(input("What is your p value: "))

q = int(input("What is your q value: "))

n = p*q 

tn = (p-1)*(q-1)

e = int(input("What is your Public Key Coefficient of e: "))

d = e**-1 % tn

C = p**e % n

P = C**d % n


count = 1

tn_set = []

e_set = []

matching_values = []

TNN = 1

EE = 0

while True:
    TNN += tn
    tn_set.append(TNN)
    EE += e
    e_set.append(EE)
    count += 1
    for item in tn_set:
        if item in e_set:
            matching_values.append(item)

    matching_indices = []

    for value in matching_values:
        index1 = tn_set.index(value) # TNN 
        index2 = e_set.index(value) # EE
        matching_indices.append((value, int(index1 +1), int(index2+1))) #Matching section in the list |  it will always be this value for RSA

    if matching_indices:
        for x in matching_indices:
            print("Matching tn value: ", x[0])
            print("matching location on tn in count: ", x[1])
            print("d value (The answer you're looking for): ", x[2])
        
        print("Method 2 returns:", matching_indices)
        break
    else:
        continue





