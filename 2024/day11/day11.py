def part1():
    with open("input.in","r") as file:
        stones = [int(c) for c in file.read().split(" ")]
    
    NUM_BLINKS = 25
    new_stones = []
    for i in range(NUM_BLINKS):
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            else:
                stone_str = str(stone)
                stone_len = len(stone_str)
                if stone_len % 2 == 0:
                    new_stones.append(int(stone_str[:stone_len//2]))
                    new_stones.append(int(stone_str[stone_len//2:]))
                else:
                    new_stones.append(stone*2024)
        stones = new_stones
        new_stones = []
    
    print(len(stones))

part1()

def part2():
    with open("input.in","r") as file:
        stones = {int(c) : 1 for c in file.read().split(" ")}

    NUM_BLINKS = 75

    new_stones = {}
    for i in range(NUM_BLINKS):
        for stone, count in stones.items():
            if stone == 0:
                if 1 in new_stones:
                    new_stones[1] += count
                else:
                    new_stones[1] = count
            else:
                stone_str = str(stone)
                stone_len = len(stone_str)
                if stone_len % 2 == 0:
                    num1, num2 = (int(stone_str[:stone_len//2]),int(stone_str[stone_len//2:]))
                    if num1 in new_stones:
                        new_stones[num1] += count
                    else:
                        new_stones[num1] = count
                    if num2 in new_stones:
                        new_stones[num2] += count
                    else:
                        new_stones[num2] = count
                else:
                    if stone*2024 in new_stones:
                        new_stones[stone*2024] += count
                    else:
                        new_stones[stone*2024] = count
        stones = new_stones
        new_stones = {}

    print(sum(list(stones.values())))

part2()