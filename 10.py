lines = open("10.txt").read().splitlines()

cycle = 1
register = 1
signalSum = 0

def cycleIncr():
    global cycle, signalSum
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        signalSum += cycle * register 

for line in lines:
    if line != "noop":
        cycleIncr()
        register += int(line.split(" ")[1])
        cycleIncr()
    else:
        cycleIncr()

print(signalSum)
