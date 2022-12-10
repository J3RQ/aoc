lines = open("10.txt").read().splitlines()

cycle = 0
register = 1
row = ["." for x in range(40)]
output = []

def cycleIncr():
    global cycle, row
    cycle += 1
    if cycle % 40 == 0:
        output.append("".join(row))
        row = ["." for x in range(40)]

for line in lines:
    if abs(cycle % 40 - register) <= 1:
        row[cycle % 40] = "#"
    if line != "noop":
        incr = int(line.split(" ")[1])
        cycleIncr()
        if abs(cycle % 40 - register) <= 1:
            row[cycle % 40] = "#"
        register += incr
        cycleIncr()
    else:
        cycleIncr()

[print(x) for x in output]
