elves = [0]
with open('1.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

for i in lines:
    if i == '':
        elves.append(0)
        continue
    elves[-1] = elves[-1] + int(i)

# part 1 answer:
print(max(elves))


top3total = 0
for i in range(3):
    top3total += elves.pop(elves.index(max(elves)))

# part 2 answer:
print(top3total)
