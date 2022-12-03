
with open('3.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

prioritySum = 0
for i in lines:
    #print(i)
    a = i[0:(int((len(i)/2)))]
    b = i[int((len(i)/2)):]
    for j in a:
        if j in b:
            if (ord(j)-96) > 0:
                prioritySum += ord(j)-96 # ascii to one-based
                #print(j,ord(j)-96)
            else:
                prioritySum += ord(j)-38 # ascii to 27 based
                #print(j,ord(j)-38)
            break
print(prioritySum)
