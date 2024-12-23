
import re

def part1():
    with open("input.in") as file:
        line = file.read()
    matches = re.findall("mul\([0-9]+[0-9]?[0-9]?,[0-9]+[0-9]?[0-9]?\)",line)
    sum = 0
    for match in matches:
        sum += int(match[4:match.find(",")]) * int(match[match.find(",") + 1 : match.find(")")])
    print(sum)

def part2():
    with open("input.in") as file:
        line = file.read()
    matches = re.findall("(mul\([0-9]+[0-9]?[0-9]?,[0-9]+[0-9]?[0-9]?\))|(do\(\))|(don't\(\))",line)
    sum = 0
    enabled = True
    for match in matches:
        if match[0] != "" and enabled is True:
            match = match[0]
            sum += int(match[4:match.find(",")]) * int(match[match.find(",") + 1 : match.find(")")])
        elif match[1] != "":
            enabled = True
        elif match[2] != "":
            enabled = False
    print(sum)


part1()
part2()