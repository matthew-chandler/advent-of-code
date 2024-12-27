def evaluate(report):
    # valid if only one number
    if len(report) == 1:
        return 1
    
    increasing = report[1] > report[0]
    for i in range(1, len(report)):
        if (report[i] > report[i-1]) != increasing:
            return 0
        diff = abs(report[i] - report[i-1])
        if diff < 1 or diff > 3:
            return 0
    return 1

with open("input.in") as f:
    reports = f.readlines()

safe = 0
for report in reports:
    report = report.strip("\n").split(" ")
    report = [int(x) for x in report]

    score = evaluate(report)
    if score == 1:
        safe += 1
        continue
    else:
        for i, _ in enumerate(report):
            temp = report[:i] + report[(i+1):]
            if evaluate(temp) == 1:
                safe += 1
                break
print(safe)