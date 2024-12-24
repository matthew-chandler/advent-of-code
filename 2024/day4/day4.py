def MAS(M,A,S):
    return M == "M" and A == "A" and S == "S"
    

def part1():
    with open("input.in") as file:
        ws = file.read().split("\n")
    
    sum = 0
    for i in range(len(ws)):
        for j in range(len(ws[0])):
            c = ws[i][j]
            if c != "X":
                continue
            # check all directions
            else:
                # up
                if (i>2):
                    # up -_
                    if MAS(ws[i-1][j],ws[i-2][j],ws[i-3][j]):
                        sum += 1
                    # up-left --
                    if (j>2) and MAS(ws[i-1][j-1],ws[i-2][j-2],ws[i-3][j-3]):
                        sum += 1
                    # up-right -+
                    if (j<(len(ws[0]))-3) and MAS(ws[i-1][j+1],ws[i-2][j+2],ws[i-3][j+3]):
                        sum += 1
                # left _-
                if (j>2) and MAS(ws[i][j-1],ws[i][j-2],ws[i][j-3]):
                    sum += 1
                # right _+
                if (j<(len(ws[0]))-3) and MAS(ws[i][j+1],ws[i][j+2],ws[i][j+3]):
                    sum += 1
                # down
                if (i<len(ws)-3):
                    # down +_
                    if MAS(ws[i+1][j],ws[i+2][j],ws[i+3][j]):
                        sum += 1
                    # down-left +-
                    if (j>2) and MAS(ws[i+1][j-1],ws[i+2][j-2],ws[i+3][j-3]):
                        sum += 1
                    # down-right ++
                    if (j<(len(ws[0]))-3) and MAS(ws[i+1][j+1],ws[i+2][j+2],ws[i+3][j+3]):
                        sum += 1

    print(sum)

def MS(pair1,pair2):
    p1, p2 = pair1
    if not ((p1 == "M" and p2 == "S") or (p1 == "S" and p2 == "M")):
        return 0
    p1, p2 = pair2
    if not ((p1 == "M" and p2 == "S") or (p1 == "S" and p2 == "M")):
        return 0
    return 1

def part2():
    with open("input.in") as file:
        ws = file.read().split("\n")
    
    sum = 0
    for i in range(1,len(ws)-1):
        for j in range(1,len(ws[0])-1):
            if ws[i][j] == "A":
                sum += MS((ws[i-1][j-1],ws[i+1][j+1]),(ws[i-1][j+1],ws[i+1][j-1]))
    print(sum)

part1()
part2()
    