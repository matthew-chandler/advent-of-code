def evaluate(report):
    report = report.strip("\n").split(" ")
    report = [int(x) for x in report]
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
    safe += evaluate(report)
print(safe)