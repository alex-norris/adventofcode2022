
with open('4.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

count=0

for i in lines:
    a = i.split(',')[0]
    b = i.split(',')[1]
    a1 = int(a.split('-')[0])
    a2 = int(a.split('-')[1])
    b1 = int(b.split('-')[0])
    b2 = int(b.split('-')[1])
    if (a1 >= b1 and a2 <= b2) \
            or (a1 <= b1 and a2 >= b2):
        count += 1

print(count)
