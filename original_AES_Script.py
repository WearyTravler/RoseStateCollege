

original_string = "qdLo82nYTsi490zW"

hexed_ascii_string = []

for x in original_string:
    hexed_ascii_string += hex(ord(x))[2:]




current_char = ""
condensed_list = []
for char in hexed_ascii_string:
    current_char += char
    condensed_list.append(current_char)



my_hexed_ascii_string = condensed_list[-1]


cipher_key = "7b3b9c318a82c5b2751540162c46566e"

last_8_values = cipher_key[-8:]

moved_string = last_8_values[2:] + last_8_values[:2]

first_4_values = cipher_key[:8]

first_4_values_list = []

first_4_values_list_pairs = []

second_4_values = cipher_key[8:16]

second_4_value_list = []
second_4_value_list_pairs = []


for x in second_4_values:
    second_4_value_list.append(x)


for i in range(0, len(second_4_value_list), 2):
    x = second_4_value_list[i]
    y = second_4_value_list[i + 1]
    second_4_value_list_pairs.append(str(x) + str(y))



for x in first_4_values:
    first_4_values_list.append(x)



for i in range(0, len(first_4_values_list), 2):
    x = first_4_values_list[i]
    y = first_4_values_list[i + 1]
    first_4_values_list_pairs.append(str(x) + str(y))





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


#goal:
#place 46 56 6E 2C and return 5A B1 9F 71 

pairs = []

for i in range(0, len(moved_string), 2):
    x = int(moved_string[i], 16) if moved_string[i].isdigit() else hex_mapping.get(moved_string[i].lower(), None)
    y = int(moved_string[i + 1], 16) if moved_string[i + 1].isdigit() else hex_mapping.get(moved_string[i + 1].lower(), None)
    pairs.append(str(x) + str(y))


#print(pairs)

split_pairs = []

for item in pairs:
        if len(item) == 2:
            x, y = int(item[0], 16), int(item[1], 16)
        elif len(item) == 3:
            x, y = int(item[0], 16), int(item[1:], 16)
        elif len(item) == 4:
            x1, y1 = int(item[0], 16), int(item[1], 16)
            x2, y2 = int(item[2], 16), int(item[3], 16)
        else:
            raise ValueError(f"Invalid input: {item}")

        split_pairs.append((x,y))


#print(split_pairs)

s_box_values = []

for x, y in split_pairs:
    s_box_values.append(s_box[x][y-6]) #why am i having to subtract 6?


#print(s_box_values)

rcon_values = ['01', '00', '00', '00']


# print(first_4_values_list_pairs)
# print(s_box_values)
# print(rcon_values)



#Xoring the first 8 values of our cipher_keywith our s_box_values against our RCON


#xoring the first column
def xor_lists(list1, list2):
    result = []
    for a, b in zip(list1, list2):
        # Convert hex strings to integers for XOR operation
        a_int, b_int = int(a, 16), int(b, 16)
        # Perform XOR and format the result as a hex string
        xor_result = format(a_int ^ b_int, '02x')
        result.append(xor_result)
    return result


result1 = xor_lists(first_4_values_list_pairs, s_box_values)
first_column = xor_lists(result1, rcon_values)

print(first_column)


#xoring the second column:

second_column = second_4_value_list_pairs

second_column = xor_lists(first_column, second_column)

# print(second_4_value_list_pairs)
# print(second_column)

#third column:

third_value_set = ['75', '15', '40', '16']
fourth_value_set = ['2c', '46', '56', '6e']

third_column = xor_lists(second_column, third_value_set)


# print(third_column)


#fourth_column

fourth_column = xor_lists(third_column, fourth_value_set)
# print(fourth_column)