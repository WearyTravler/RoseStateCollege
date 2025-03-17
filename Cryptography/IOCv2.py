
#Ask for the text to find the letter count and IOC
text = input("input the text you'd like to find the IOC for: ")

text = text.upper()

numAs = 0
numBs = 0
numCs = 0
numDs = 0
numEs = 0
numFs = 0
numGs = 0
numHs = 0
numIs = 0
numJs = 0
numKs = 0
numLs = 0
numMs = 0
numNs = 0
numOs = 0
numPs = 0
numQs = 0
numRs = 0
numSs = 0
numTs = 0
numUs = 0
numVs = 0
numWs = 0
numXs = 0
numYs = 0
numZs = 0


for x in range(len(text)):
    if text[x] == 'A':
        numAs = numAs +1
    if text[x] == 'B':
        numBs = numBs +1
    if text[x] == 'C':
        numCs = numCs +1
    if text[x] == 'D':
        numDs = numDs +1
    if text[x] == 'E':
        numEs = numEs +1
    if text[x] == 'F':
        numFs = numFs +1
    if text[x] == 'G':
        numGs = numGs +1
    if text[x] == 'H':
        numHs = numHs +1
    if text[x] == 'I':
        numIs = numIs +17
    if text[x] == 'J':
        numJs = numJs +1
    if text[x] == 'K':
        numKs = numKs +1
    if text[x] == 'L':
        numLs = numLs +1
    if text[x] == 'M':
        numMs = numMs +1
    if text[x] == 'N':
        numNs = numNs +1
    if text[x] == 'O':
        numOs = numOs +1
    if text[x] == 'P':
        numPs = numPs +1
    if text[x] == 'Q':
        numQs = numQs +1
    if text[x] == 'R':
        numRs = numRs +1
    if text[x] == 'S':
        numSs = numSs +1
    if text[x] == 'T':
        numTs = numTs +1
    if text[x] == 'U':
        numUs = numUs +1
    if text[x] == 'V':
        numVs = numVs +1
    if text[x] == 'W':
        numWs = numWs +1
    if text[x] == 'X':
        numXs = numXs +1
    if text[x] == 'Y':
        numYs = numYs +1
    if text[x] == 'Z':
        numZs = numZs +1



Totalnum = numAs + numBs + numCs + numDs + numEs + numFs + numGs + numHs + numIs + numJs + numKs + numLs + numMs + numNs + numOs + numPs + numQs + numRs + numSs + numTs + numUs + numVs + numWs + numXs + numYs + numZs
Numerator = numAs*(numAs-1) + numBs*(numBs-1) + numCs*(numCs-1) + numDs*(numDs-1) + numEs*(numEs-1) + numFs*(numFs-1) + numGs*(numGs-1) + numHs*(numHs-1) + numIs*(numIs-1) + numJs*(numJs-1) + numKs*(numKs-1) + numLs*(numLs-1) + numMs*(numMs-1) + numNs*(numNs-1) + numOs*(numOs-1) + numPs*(numPs-1) + numQs*(numQs-1) + numRs*(numRs-1) + numSs*(numSs-1) + numTs*(numTs-1) + numUs*(numUs-1) + numVs*(numVs-1) + numWs*(numWs-1) + numXs*(numXs-1) + numYs*(numYs-1) + numZs*(numZs-1)

Denominator = Totalnum*(Totalnum-1)
IOC = Numerator/Denominator

# print("As:",numAs)
# print("Bs:",numBs)
# print("Cs:",numCs)
# print("Ds:",numDs)
# print("Es:",numEs)
# print("Fs:",numFs)
# print("Gs:",numGs)
# print("Hs:",numHs)
# print("Is:",numIs)
# print("Js:",numJs)
# print("Ks:",numKs)
# print("Ls:",numLs)
# print("Ms:",numMs)
# print("Ns:",numNs)
# print("Os:",numOs)
# print("Ps:",numPs)
# print("Qs:",numQs)
# print("Rs:",numRs)
# print("Ss:",numSs)
# print("Ts:",numTs)
# print("Us:",numUs)
# print("Vs:",numVs)
# print("Ws:",numWs)
# print("Xs:",numXs)
# print("Ys:",numYs)
# print("Zs:",numZs)


#Sum of the Letters

text_cleaned = text.replace('.', '').replace(' ', '').replace('"', '').replace("'", '').replace(":",'').replace(";",'')

# Convert all letters to lowercase
text_cleaned = text_cleaned.lower()

# Count the occurrences of each letter
letter_count = {}
for char in text_cleaned:
    if char.isalpha():  # Check if the character is a letter
        letter_count[char] = letter_count.get(char, 0) + 1


# Print the letter count
for letter, count in sorted(letter_count.items()):
    print(f'{letter}: {count}')

total_letters = sum(letter_count.values())
print("Total count of letters:", total_letters)



print("IOC: ",IOC)

