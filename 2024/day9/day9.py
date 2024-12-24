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
            disk += [Unit(i//2,FILE) for p in range(space)]
            file_indices.append(index)
        # buffer
        else:
            disk += [Unit(-1,FREE) for p in range(space)]
            free_indices.append(index)
        index += space


    free_index = 0
    file_index = len(disk) - 1

    def disk_string():
        r = ""
        for p in disk:
            if p.id == -1:
                r += "_"
            else:
                r += str(p.id % 10)
        return r
    
    search_starts = {}

    def find_space(space,file_index):
        if space in search_starts:
            i = search_starts[space]
        else:
            i = 0
        current_run = 0
        while i <= file_index - space:
            if current_run == space:
                search_starts[space] = i
                return i - current_run
            if disk[i].type == FREE:
                current_run += 1
            else:
                current_run = 0
            i += 1
        return -1
    
    # grabs length of next file block
    def get_length(index):
        length = 0
        if disk[index].type == FREE:
            return length
        id = disk[index].id
        while index < len(disk) and id == disk[index].id:
            index += 1
            length += 1
        return length

    file_key = len(file_indices) - 1
    file_index = file_indices[file_key]
    file_cap = get_length(file_index)
    free_index = find_space(file_cap,file_index)

    if debug: print(disk_string())
    # print()

    def verify_index(id):
        return disk[file_indices[id]].id == id
    
    while file_key != 0:
        if free_index != -1:
            for i in range(file_cap):
                # swap out all of them
                temp = disk[free_index+i]
                assert(temp.id == -1)
                assert(temp.type == FREE)
                disk[free_index+i] = disk[file_index+i]
                disk[file_index+i] = temp
                assert(disk[free_index+i].id != -1)
        file_key -= 1
        file_index = file_indices[file_key]
        if verify_index(file_key):
            file_cap = get_length(file_index)
        else:
            print("YOO")
            file_cap = 0
        free_index = find_space(file_cap,file_index)
            
    sum = 0
    i = 0
    for unit in disk:
        if unit.id != -1:
            # print(i, unit.id)
            sum += i * unit.id
        i += 1

    # for unit in disk:
    #     if unit.id == -1:
    #         print("_",end="")
    #     else:
    #         print(str(unit.id % 10),end="")
    
    # print()
    if debug: print(disk_string())
    print(sum)

debug = False
part1()
part2()

# 10172096513548