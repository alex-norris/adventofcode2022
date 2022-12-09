with open('5.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

rows, cols = (9, 1)
stacks = [[0 for i in range(cols)] for j in range(rows)]

for i in range(7,-1,-1):
    for j in range(1,len(lines[i]),4):
        # for 5a:
        if lines[i][j] != ' ':
            stacks[int((j-1)/4)].append(lines[i][j])
        # for 5b:
        #for j in range(-move,0):
            #stacks[end].append(stacks[start][j])
            #stacks[start].pop(j)

for i in range(10,len(lines)):
    move = int(lines[i].split(' ')[1])
    start = int(lines[i].split(' ')[3])-1
    end = int(lines[i].split(' ')[5])-1

    for j in range(move):
        stacks[end].append(stacks[start].pop())

for i in range(9):
    print(stacks[i][-1], end = '')
