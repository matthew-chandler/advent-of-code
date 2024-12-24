FILE, FREE = (0,1)

class Unit:
    def __init__(self,id,type):
        self.id = id
        self.type = type

    def __str__(self):
        if self.id == -1:
            return "_"
        return str(self.id)

def part1():
    with open("input.in") as file:
        line = [int(c) for c in list(file.read())]
    disk = []
    file_indices = []
    free_indices = []
    index = 0
    for i, space in enumerate(line):
        # file
        if i % 2 == 0:
            disk += [Unit(i//2,FILE) for p in range(space)]
            file_indices.append(index)
        # buffer
        else:
            disk += [Unit(-1,FREE) for p in range(space)]
            free_indices.append(index)
        index += space

    free_index = 0
    file_index = len(disk) - 1

    while free_index < file_index:
        if disk[free_index].type == FREE and disk[file_index].type == FILE:
            temp = disk[free_index]
            disk[free_index] = disk[file_index]
            disk[file_index] = temp
            free_index += 1
            file_index -= 1
        elif disk[free_index].type != FREE:
            free_index += 1
        elif disk[file_index].type != FILE:
            file_index -= 1
        else:
            print("should never print")

    sum = 0
    for i, unit in enumerate(disk):
        if unit.id == -1:
            break
        
        sum += i * unit.id

    print(sum)

def part2():
    with open("input.in") as file:
        line = [int(c) for c in list(file.read())]
    disk = []
    file_indices = []
    free_indices = []
    index = 0
    for i, space in enumerate(line):
        # file
        if i % 2 == 0:
            disk += [int(i//2) for p in range(space)]
            file_indices.append(index)
        # buffer
        else:
            disk += [-1 for p in range(space)]
            free_indices.append(index)
        index += space

    file_ptr = len(disk) - 1
    start_cache = {}

    while file_ptr > 0:
        current_id = disk[file_ptr]

        # skip over free space
        if current_id == -1:
            file_ptr -= 1
            continue

        # count how much needs to be moved
        diff = 0
        while (disk[file_ptr-diff] == current_id):
            diff += 1
        # diff gotten

        # figure out where I can find the space
        if diff in start_cache:
            free_ptr = start_cache[diff]
        else:
            free_ptr = 0
        target = [-1] * diff
        while (free_ptr < file_ptr):
            if disk[free_ptr:free_ptr+diff] == target:
                start_cache[diff] = free_ptr
                break
            free_ptr += 1

        # don't do the swap if no space found
        if free_ptr >= file_ptr:
            file_ptr -= diff
            continue

        # perform the swap
        for i in range(diff):
            disk[free_ptr+i] = current_id
            disk[file_ptr-i] = -1

        file_ptr -= diff

    sum = 0
    for i, id in enumerate(disk):
        if id != -1:
            sum += id * i
    
    print(sum)

debug = False
part1()
part2()