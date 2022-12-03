# a = rock
# b = paper
# c = scissors

# points:
# 1 rock, 2 paper, 3 scissors
# 0 loss, 3 draw, 6 win

with open('2.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

score = 0
for i in lines:
    #print(i[0]+i[-1])
    if i[-1] == 'X':  # lose
        score += 0
        if i[0] == "A":
            score += 3
        elif i[0] == "B":
            score += 1
        elif i[0] == "C":
            score += 2
    elif i[-1] == 'Y':  # draw
        score += 3
        if i[0] == "A":
            score += 1
        elif i[0] == "B":
            score += 2
        elif i[0] == "C":
            score += 3
    elif i[-1] == 'Z':  # win
        score += 6
        if i[0] == "A":
            score += 2
        elif i[0] == "B":
            score += 3
        elif i[0] == "C":
            score += 1
print(score)
