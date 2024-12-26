import queue

def part1():
    with open("input.in") as file:
        map = [[(int(c),set()) for c in line] for line in file.read().split("\n")]

    q = queue.Queue()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j][0] == 9:
                q.put((i,j))
                map[i][j][1].add((i,j))

    while not q.empty():
        i,j = q.get()
        val = map[i][j][0]
        # check left
        if i > 0 and map[i-1][j][0] == val - 1:
            q.put((i-1,j))
            for peak in map[i][j][1]:
                map[i-1][j][1].add(peak)
        if i < len(map) - 1 and map[i+1][j][0] == val - 1:
            q.put((i+1,j))
            for peak in map[i][j][1]:
                map[i+1][j][1].add(peak)
        if j > 0 and map[i][j-1][0] == val - 1:
            q.put((i,j-1))
            for peak in map[i][j][1]:
                map[i][j-1][1].add(peak)
        if j < len(map[0]) - 1 and map[i][j+1][0] == val - 1:
            q.put((i,j+1))
            for peak in map[i][j][1]:
                map[i][j+1][1].add(peak)
    
    sum = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j][0] == 0:
                sum += len(map[i][j][1])
    print(sum)

def part2():
    with open("input.in") as file:
        map = [[[int(c),0] for c in line] for line in file.read().split("\n")]

    # add 9s to queue
    q = queue.Queue()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j][0] == 9:
                q.put((i,j))
                map[i][j][1] = 1

    visited = set()
    while not q.empty():
        i,j = q.get()
        if (i,j) in visited:
            continue
        else:
            visited.add((i,j))
        val = map[i][j][0]
        score = map[i][j][1]

        if i > 0 and map[i-1][j][0] == val - 1:
            q.put((i-1,j))
            map[i-1][j][1] += score
        if i < len(map) - 1 and map[i+1][j][0] == val - 1:
            q.put((i+1,j))
            map[i+1][j][1] += score
        if j > 0 and map[i][j-1][0] == val - 1:
            q.put((i,j-1))
            map[i][j-1][1] += score
        if j < len(map[0]) - 1 and map[i][j+1][0] == val - 1:
            q.put((i,j+1))
            map[i][j+1][1] += score
    
    # count up the number of paths per 0
    sum = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j][0] == 0:
                sum += map[i][j][1]
    print(sum)

part1()
part2()

def part2v2():
    with open("input.in") as file:
        map = [[int(c) for c in line] for line in file.read().split("\n")]

    q = queue.Queue()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 9:
                q.put((i,j))

    sum = 0
    while not q.empty():
        i,j = q.get()
        val = map[i][j]
        if val == 0:
            sum += 1
            continue
        if i > 0 and map[i-1][j] == val - 1:
            q.put((i-1,j))
        if i < len(map) - 1 and map[i+1][j] == val - 1:
            q.put((i+1,j))
        if j > 0 and map[i][j-1] == val - 1:
            q.put((i,j-1))
        if j < len(map[0]) - 1 and map[i][j+1] == val - 1:
            q.put((i,j+1))

    print(sum)

# part2v2()