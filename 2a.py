# a,x = rock
# b,y = paper
# c,z = scissors

# points:
# 1 rock, 2 paper, 3 scissors
# 0 loss, 3 draw, 6 win

with open('2.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

score = 0
for i in lines:
    #print(i[0]+i[-1])
    if i[-1] == 'X':
        score += 1
        if i[0] == "A":
            score += 3
        elif i[0] == "B":
            score += 0
        elif i[0] == "C":
            score += 6
    elif i[-1] == 'Y':
        score += 2
        if i[0] == "A":
            score += 6
        elif i[0] == "B":
            score += 3
        elif i[0] == "C":
            score += 0
    elif i[-1] == 'Z':
        score += 3
        if i[0] == "A":
            score += 0
        elif i[0] == "B":
            score += 6
        elif i[0] == "C":
            score += 3
print(score)
