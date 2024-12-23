
with open("input.in") as file:
    lines = file.readlines()

# part 1

l1 = []
l2 = []
for line in lines:
    line = line.strip("\n")
    line = line.split(" ")
    l1.append(int(line[0]))
    l2.append(int(line[3]))

l1.sort()
l2.sort()

distance = 0
for n1, n2 in zip(l1,l2):
    distance += abs(n1-n2)

print(distance)

# part 2

score = 0

freq2 = {id : l2.count(id) for id in l2}

for id in l1:
    if id not in freq2:
        val2 = 0
    else:
        val2 = freq2[id]
    score += id * val2

print(score)