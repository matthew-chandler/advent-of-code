def part1():
    # parsing
    with open("input.in") as f:
        lines = f.read().split("\n")
    map = [list(line) for line in lines][:-1]
    
    # find start
    i,j = (0,0)
    for a in range(len(map)):
        for b in range(len(map[0])):
            if map[a][b] == "^":
                i,j = (a,b)

    UP, DOWN, LEFT, RIGHT = (0,1,2,3)
    dir = UP

    visited = {(i,j)}

    while i >= 0 and i < len(map) and j >= 0 and j < len(map[0]):
        if dir == UP:
            if i == 0: break
            elif map[i-1][j] == "#":
                dir = RIGHT
            else:
                i -= 1
        elif dir == RIGHT:
            if j == len(map[0]) - 1: break
            elif map[i][j+1] == "#":
                dir = DOWN
            else:
                j += 1
        elif dir == DOWN:
            if i == len(map) - 1: break
            elif map[i+1][j] == "#":
                dir = LEFT
            else:
                i += 1
        elif dir == LEFT:
            if j == 0: break
            elif map[i][j-1] == "#":
                dir = UP
            else:
                j -= 1
        visited.add((i,j))

    print(len(visited))

def part2():
    # parsing
    with open("input.in") as f:
        lines = f.read().split("\n")
    map = [list(line) for line in lines][:-1]
    
    # find start
    for a in range(len(map)):
        for b in range(len(map[0])):
            if map[a][b] == "^":
                start = (a,b)

    UP, DOWN, LEFT, RIGHT = (0,1,2,3)
    poss = 0
    count = 0

    for a in range(len(map)):
        for b in range(len(map[0])):
            dir = UP
            i,j = start
            
            if map[a][b] == ".":
                map[a][b] = "#"
                visited = set()
                # simulate
                steps = 0
                recent = False
                while True:
                    if (i,j,dir) in visited:
                        poss += 1
                        break
                    visited.add((i,j,dir))
                    if dir == UP:
                        if i == 0: break
                        elif map[i-1][j] == "#":
                            dir = RIGHT
                        else:
                            i -= 1
                            steps += 1
                    elif dir == RIGHT:
                        if j == len(map[0]) - 1: break
                        elif map[i][j+1] == "#":
                            dir = DOWN
                        else:
                            j += 1
                            steps += 1
                    elif dir == DOWN:
                        if i == len(map) - 1: break
                        elif map[i+1][j] == "#":
                            dir = LEFT
                        else:
                            i += 1
                            steps += 1
                    elif dir == LEFT:
                        if j == 0: break
                        elif map[i][j-1] == "#":
                            dir = UP
                        else:
                            j -= 1
                            steps += 1
                    
                map[a][b] = "."

    print(poss)

    

part1()
part2()