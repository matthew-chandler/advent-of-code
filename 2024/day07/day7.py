def part1():
    with open("input.in") as file:
        eqs = file.read().split("\n")
    for i, eq in enumerate(eqs):
        eq = eq.split(" ")
        eqs[i] = (int(eq[0][:-1]),[int(i) for i in eq[1:]])

    final_sum = 0
    for target, expression in eqs:
        seed = 0
        while seed < 2 ** len(expression[1:]):
            run = expression[0]
            for i, term in enumerate(expression[1:]):
                operator = (seed >> i) & 1
                if operator == 1: run *= term
                else: run += term
            if run == target:
                final_sum += target
                break
            seed += 1
    print(final_sum)

def part2():
    with open("input.in") as file:
        eqs = file.read().split("\n")
    for i, eq in enumerate(eqs):
        eq = eq.split(" ")
        eqs[i] = (int(eq[0][:-1]),[int(i) for i in eq[1:]])

    final_sum = 0
    for target, expression in eqs:
        seed2 = 0
        while seed2 < 2 ** len(expression[1:]):
            seed1 = 0
            while seed1 < 2 ** len(expression[1:]):
                run = expression[0]
                for i, term in enumerate(expression[1:]):
                    operator = (seed1 >> i) & 1
                    concat = (seed2 >> i) & 1
                    if concat == 1: run = int(str(run) + str(term))
                    else:
                        if operator == 1: run *= term
                        else: run += term
                if run == target:
                    final_sum += target
                    break
                seed1 += 1
            else:
                seed2 += 1
                continue
            break          
    print(final_sum)




part1()
part2()





