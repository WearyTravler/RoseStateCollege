print('Simple Super Increasing Knapsack Generator')
total = input('Enter the 1st value: ')
inNum = int(total)
simple=[]
simple.append(inNum)
while inNum != 'z':
inNum = input('Enter the next value, greater than ' + str(total) + ' , z to
quit: ')
if inNum == 'z':
break
if int(inNum) <= int(total):
print('Must be greater than ' + str(total) +'.')
else:
simple.append(inNum)
total = (int(total)+int(inNum))
print('Simple Knapsack:',simple)
