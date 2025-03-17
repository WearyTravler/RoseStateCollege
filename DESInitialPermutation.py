hexResult = []
binResult = []
def convertToHex(myString):
    for ch in myString:
        hexResult.append(hex(ord(ch)).replace("0x",'').upper().zfill(2))
    return hexResult


def convertToBin(myString):
    for ch in myString:
        binResult.append(bin(ord(ch)).replace("0b",'').upper().zfill(8))
    return binResult

def convertBinaryToHex(inArr):
    temp=''
    outArr=[]
    x=0
    for y in range (0,8):
        temp=''
        for x in range (x,x+8):
            temp=temp+inArr[x]
            x=x+1
        outArr.append(hex(int(temp,2)).replace('0x','').upper().zfill(2))
    return outArr

def initialPermutation(binArray):
    print("Bin Array: ", binArray)
    initialScheme=[58,50,42,34,26,18,10,2,
                   60,52,44,36,28,20,12,4,
                   62,54,46,38,30,22,14,6,
                   64,56,48,40,32,24,16,8,
                   57,49,41,33,25,17,9,1,
                   59,51,43,35,27,19,11,3,
                   61,53,45,37,29,21,13,5,
                   63,55,47,39,31,23,15,7]
    outArray=list(range(64))
    for x in range (0,len(binArray)):
        outArray[x]=binArray[initialScheme[x]-1]
    tempStr=''
    for x in range (0,len(outArray)):
        tempStr=tempStr+outArray[x]
    return tempStr




def expansionPermutation(inBin):
    expansionScheme=["2:48","3","4","5:7","6:8","9","10","11:13",
                "12:14","15","16","17:19","18:20","21","22","23:25",
                "24:26","27","28","29:31","30:32","33","34","35:37",
                "36:38","39","40","41:43","42:44","45","46","47:1"]
    left = []
    right = []
    left = inBin[:32]
    right = inBin[32:]


    output = list(range(48))

    for x in range(len(expansionScheme)):
        val1 = int(expansionScheme[x].split(":")[0])
        output[val1-1] = inBin[x]
        if len(expansionScheme[x].split(":"))>1:
            val2 = int(expansionScheme[x].split(":")[1])
            output[val2-1] = inBin[x]


myString=input("What is the String for Initial Permutation/Expansion Permutation: ")
print("Initial: ", myString)
print("Converted to Hex: ", * convertToHex(myString), sep='')
print("Convert to Binary: ",* convertToBin(myString),sep='')
tempStr=''
for x in range(0,8):
    for y in range(0,8):
        tempStr=tempStr+binResult[x][y]

permutedArray=initialPermutation(tempStr)
permutedHexArray=convertBinaryToHex(permutedArray)
permutedexpArray=expansionPermutation(tempStr)
print(permutedexpArray)
#print("Converted", *permutedHexArray)
