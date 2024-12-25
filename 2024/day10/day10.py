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
        map = [[(int(c),[]) for c in line] for line in file.read().split("\n")]

    q = queue.Queue()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j][0] == 9:
                q.put((i,j))
                map[i][j][1].append([])

    import time

    while not q.empty():
        i,j = q.get()
        val = map[i][j][0]
        print(i,j,map[i][j][0],map[i][j][1])
        print()
        time.sleep(0.5)
        # check left
        if i > 0 and map[i-1][j][0] == val - 1:
            q.put((i-1,j))
            for path in map[i][j][1]:
                map[i-1][j][1].append(path+[(i,j)])
        if i < len(map) - 1 and map[i+1][j][0] == val - 1:
            q.put((i+1,j))
            for path in map[i][j][1]:
                map[i+1][j][1].append(path+[(i,j)])
        if j > 0 and map[i][j-1][0] == val - 1:
            q.put((i,j-1))
            for path in map[i][j][1]:
                map[i][j-1][1].append(path+[(i,j)])
        if j < len(map[0]) - 1 and map[i][j+1][0] == val - 1:
            q.put((i,j+1))
            for path in map[i][j][1]:
                map[i][j+1][1].append(path+[(i,j)])
    
    sum = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j][0] == 0:
                sum += len(map[i][j][1])
    print(sum)

part1()
part2()
