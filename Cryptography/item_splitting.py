




item = '1016'

if len(item) == 2:
        x = int(item[0])
        y = int(item[1])
        #print(x,y)
elif len(item) == 3:
        x  = int(item[0:2])
        y  = int(item[2:])
        if x > 16:
            x = int(item[0:1])
            y = int(item[1:])
            print("x and y are equal to:",x,y)
        else:
            print("x and y are equal to:",x,y)
elif len(item) == 4:
        x, y = int(item[0:2]), int(item[1:])
        print("x and y are equal to:",x,y)
        #print(x,y)
else:
    raise ValueError(f"Invalid input: {item}")


#pseudo code

#if x is greater than 16, then give the right hand value to y
#if y is greater than 16,then given the left hand value to x
#exit
