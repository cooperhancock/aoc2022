input = []
INPUTFILE = "in1.txt"
with open(INPUTFILE, 'r') as f:
    input = f.readlines()

localCount = 0
carryList = []
for n in input:
    if n == '' or n == '\n':
        carryList.append(localCount)
        localCount = 0
    else:
        localCount += int(n)

print(max(carryList))
print(sum(sorted(carryList, reverse=True)[:3]))




