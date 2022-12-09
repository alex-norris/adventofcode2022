from collections import Counter

with open('6.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

input = lines[0]
# 4 for 6a, 14 for 6b:
testLength = 4


for i in range(testLength-1,len(input)):
    test = ''
    for j in range(testLength):
        test += input[i-j]

    wc = Counter(test)
    testFail = 0
    for letter, count in wc.items():
        if count > 1:
            testFail += 1
            
    if testFail == 0:
        print(i+1)
        break
