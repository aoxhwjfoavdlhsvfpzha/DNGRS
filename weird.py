print("Input Hex: ")
hexi = input()
parities = [[], [], [], []]
print()

try:
    #Convert from hex
    number = hexi
    number = number.replace(" ", "")
    decinum = int(number, 16)
    binanum = bin(decinum)[2:]
except Exception as e:
    print("Error! Maybe not Hexidecimal?")
    exit()

x = 0;
i = 0;
while (i < 4):
    while (x < len(binanum)):
        parities[i].append(binanum[x])
        x = x + 4
    i += 1
    x = 0 + i

pvals = []
for z in range(4):
    val = 0;
    for y in range(len(parities[z])):
        val += int(parities[z][y])
    pvals.append(val)

pbin = ""

print("Parity bit #1: ", end="")
if int(pvals[0]) % 2 == 0:
    print("1")
    pbin += "1"
else:
    print(0)
    pbin += "0"

print("Parity bit #2: ", end="")
if int(pvals[1]) % 2 == 0:
    print("0")
    pbin += "0"
else:
    print("1")
    pbin += "1"

print("Parity bit #3: ", end="")
if int(pvals[2]) % 2 == 0:
    print("0")
    pbin += "0"
else:
    print("1")
    pbin += "1"

print("Parity bit #4: ", end="")
if int(pvals[3]) % 2 == 0:
    print("0")
    pbin += "0"
else:
    print("1")
    pbin += "1"

number = pbin
decinum = int(str(number), 2)
hexinum = hex(decinum)[2:]

print()
print("Parity Hex: " + hexinum.upper())
