import time

p = int(input("What is your p value: ")) #3
q = int(input("What is your q value: ")) #85
n = p*q # 255
tn = (p-1)*(q-1)
e = int(input("What is your Public Key Coefficient of e: ")) #6
# e < n such that gcd(e,t)=1
# d = e**-1 % tn #168 times 6**-1 #Why is it not 91?
d = int(input("What is you Private Key Coefficient of d: ")) #91 
d_equation = e**-1 % tn
P = int(input("What is you capitalized P Value: ")) #14
C = P**e % n #14 ** 6 % 255




print("C Value is equal to: ", C)
