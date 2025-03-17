
#Original Cipher Key
#cipher_key = "7b3b9c318a82c5b2751540162c46566e"
cipher_key =  "37893f6c4a127baf5d563c278a2261be"
# cipher_key = input("What is the cipher Key: ")

s_box = [
    ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
    ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
    ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
    ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
    ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
    ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],
    ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
    ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
    ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
    ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
    ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
    ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
    ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
    ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],
    ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],
    ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
]

hex_mapping = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

##7b3b9c31 # column 1
##8a82c5b2 # column 2
##75154016 # column 3
##2c46566e # column 4






#STEP 1: CREATE THE ROUND KEY

#7b3b9c318a82c5b2751540162c46566e example

#SPLITTING THE KEY INTO 4 COLUMNS

# Column 1
first_column = cipher_key[:8] # '7b3b9c31'
#stores second_column string into pairs
first_column_pairs = []
for i in range(0, len(first_column), 2):
    x = int(first_column[i], 16) if first_column[i].isdigit() else hex_mapping.get(first_column[i].lower(), None)
    y = int(first_column[i + 1], 16) if first_column[i + 1].isdigit() else hex_mapping.get(first_column[i + 1].lower(), None)
    first_column_pairs.append(str(x) + str(y))
    

# Column 2
second_column = cipher_key[8:16] # '8a82c5b2'
#stores second_column string into pairs
second_column_pairs = []
for i in range(0, len(second_column), 2):
    x = int(second_column[i], 16) if second_column[i].isdigit() else hex_mapping.get(second_column[i].lower(), None)
    y = int(second_column[i + 1], 16) if second_column[i + 1].isdigit() else hex_mapping.get(second_column[i + 1].lower(), None)
    second_column_pairs.append(str(x) + str(y))

# Column 3
third_column = cipher_key[16:24] # '75154016'
#stores third_column string into pairs 
third_column_pairs = []

#sorting the values into pairs within a list
for i in range(0, len(third_column), 2):
    x = int(third_column[i], 16) if third_column[i].isdigit() else hex_mapping.get(third_column[i].lower(), None)
    y = int(third_column[i + 1], 16) if third_column[i + 1].isdigit() else hex_mapping.get(third_column[i + 1].lower(), None)
    third_column_pairs.append(str(x) + str(y))

# Column 4 changed properly
fourth_column = cipher_key[24:] # '2c46566e'

fourth_column_rotated = fourth_column[2:] + fourth_column[:2] # '46566e2c'

fourth_column_pairs = [] #Where to store the fourth_column_pairs

#the below for loop goes through the fourth_column_pairs and 
# looks for digits and then maps the digits if they go outside of 9 in the s_box
for i in range(0, len(fourth_column_rotated), 2):
    x = int(fourth_column_rotated[i], 16) if fourth_column_rotated[i].isdigit() else hex_mapping.get(fourth_column_rotated[i].lower(), None)
    y = int(fourth_column_rotated[i + 1], 16) if fourth_column_rotated[i + 1].isdigit() else hex_mapping.get(fourth_column_rotated[i + 1].lower(), None)
    fourth_column_pairs.append(str(x) + str(y))



# print(first_column_pairs)
# print(second_column_pairs)
# print(third_column_pairs)
# print(fourth_column_pairs)
#RETURNS
# ['711', '311', '912', '31'] 7b 3b 9c 31
# ['810', '82', '125', '112'] 8a 82 c5 b2
# ['75', '15', '40', '16']    75 15 40 16
# ['46', '56', '614', '212']  2c 46 56 6e



#  SPLITTING THE COLUMNS INTO PAIRS FOR X AND Y COORDINATES IN THE S_BOX

#1ST COLUMN
# ['711', '311', '912', '31']
first_column_split_pairs = []

for item in first_column_pairs:
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
                #print("x and y are equal to:",x,y)
            #else:
                #print("x and y are equal to:",x,y)
        elif len(item) == 4:
            x, y = int(item[0:2]), int(item[1:])
        #print(x,y)
        else:
            raise ValueError(f"Invalid input: {item}")

        first_column_split_pairs.append((x,y))

# print("first column pairs: ",first_column_pairs)
# print("first column split pairs:",first_column_split_pairs)

#2nd COLUMN
# ['810', '82', '125', '112']
second_column_split_pairs = []


for item in second_column_pairs:
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
                #print("x and y are equal to:",x,y)
            #else:
                #print("x and y are equal to:",x,y)
        elif len(item) == 4:
            x, y = int(item[0:2]), int(item[1:])
        #print(x,y)
        else:
            raise ValueError(f"Invalid input: {item}")

        second_column_split_pairs.append((x,y))

# print("second column pairs: ",second_column_pairs)
# print("second column split pairs:",second_column_split_pairs)

#3RD COLUMN
# ['46', '56', '614', '212']
third_column_split_pairs = []


for item in fourth_column_pairs:
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
                #print("x and y are equal to:",x,y)
            #else:
                #print("x and y are equal to:",x,y)
        elif len(item) == 4:
            x, y = int(item[0:2]), int(item[1:])
        #print(x,y)
        else:
            raise ValueError(f"Invalid input: {item}")

        third_column_split_pairs.append((x,y))

#print("third column pairs: ",third_column_pairs)
#print("third column split pairs:",third_column_split_pairs)

#4TH COLUMN
#['75', '15', '40', '16']
fourth_column_split_pairs = []


for item in fourth_column_pairs:
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
                #print("x and y are equal to:",x,y)
            #else:
                #print("x and y are equal to:",x,y)
        elif len(item) == 4:
            x, y = int(item[0:2]), int(item[1:])
        #print(x,y)
        else:
            raise ValueError(f"Invalid input: {item}")

        fourth_column_split_pairs.append((x,y))

#print("fourth column pairs: ",fourth_column_pairs)
#print("fourth column split pairs:",fourth_column_split_pairs)

# print("first column split pairs:",first_column_split_pairs)
# print("second column split pairs:",second_column_split_pairs)
# print("third column split pairs:",third_column_split_pairs)
# print("fourth column split pairs:",fourth_column_split_pairs)


# XOR WITH RCON


rcon_values = ['01', '00', '00', '00']


columns = [first_column_split_pairs, second_column_pairs, third_column_pairs, fourth_column_pairs]


def xor_lists(list1, list2):
    result = []
    for a, b in zip(list1, list2):
        # Convert hex strings to integers for XOR operation
        a_int, b_int = int(a, 16), int(b, 16)
        # Perform XOR and format the result as a hex string
        xor_result = format(a_int ^ b_int, '02x')
        result.append(xor_result)
    return result


# Xoring first column against the fourth column against rcon list

#first column xored against the fourth column
#print(first_column_split_pairs)
#print(fourth_column_split_pairs)
print(xor_lists(first_column_pairs, fourth_column_pairs))
