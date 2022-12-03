
with open('3.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

prioritySum = 0

for i in range(2,len(lines),3):
    print(lines[i])
    a = lines[i-2]
    b = lines[i-1]
    c = lines[i]
    for j in a:
        if j in b and j in c:
            if (ord(j)-96) > 0:
                prioritySum += ord(j)-96 # ascii to one-based
                #print(j,ord(j)-96)
            else:
                prioritySum += ord(j)-38 # ascii to 27 based
                #print(j,ord(j)-38)
            break
print(prioritySum)
