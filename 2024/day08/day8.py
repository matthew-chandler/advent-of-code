class loc:
    def __init__(self):
        self.antennas = []
        self.antinodes = []

def part1():
    with open("input.in") as file:
        lines = file.read().split("\n")
    map = [[c for c in line] for line in lines]

    antennas = {}
    antinodes = set()
    for i in range(len(map)):
        for j in range(len(map[0])):
            antenna = map[i][j]
            if antenna != ".":
                if antenna in antennas:
                    antennas[antenna].append((i,j))
                else:
                    antennas[antenna] = [(i,j)]
    
    for (a_type,locs) in antennas.items():
        for i, l1 in enumerate(locs):
            for l2 in locs[i+1:]:
                if l1 is l2:
                    continue
                # place antennas
                i1, j1 = l1
                i2, j2 = l2
                idiff = i1 - i2
                jdiff = j1 - j2
                antinode1 = (i1 + idiff, j1 + jdiff)
                antinode2 = (i2 - idiff, j2 - jdiff)
                for (x, y) in [antinode1,antinode2]:
                    if 0 <= x and x < len(map) and 0 <= y and y < len(map[0]):
                        antinodes.add((x,y))
    
    print(len(antinodes))

def part2():
    with open("input.in") as file:
        lines = file.read().split("\n")
    map = [[c for c in line] for line in lines]

    antennas = {}
    antinodes = set()
    for i in range(len(map)):
        for j in range(len(map[0])):
            antenna = map[i][j]
            if antenna != ".":
                if antenna in antennas:
                    antennas[antenna].append((i,j))
                else:
                    antennas[antenna] = [(i,j)]
    
    for (a_type,locs) in antennas.items():
        for i, l1 in enumerate(locs):
            for l2 in locs[i+1:]:
                if l1 is l2:
                    continue
                # place antennas
                i1, j1 = l1
                i2, j2 = l2
                idiff = i1 - i2
                jdiff = j1 - j2
                while True:
                    if 0 <= i1 and i1 < len(map) and 0 <= j1 and j1 < len(map[0]):
                        antinodes.add((i1,j1))
                        i1 += idiff
                        j1 += jdiff
                    else:
                        break
                while True:
                    if 0 <= i2 and i2 < len(map) and 0 <= j2 and j2 < len(map[0]):
                        antinodes.add((i2,j2))
                        i2 -= idiff
                        j2 -= jdiff
                    else:
                        break
    
    print(len(antinodes))
    




part1()
part2()





