lines, values = open("15.txt").read().splitlines(), list()
lines = [x.split() for x in lines]
for line in lines:
    values.append([int(x.replace(":", "").replace(",", "").split("=")[1]) for i, x in enumerate(line) if i in [2, 3, 8, 9]])

beacons, safe = set(), set()
for value in values:
    distance = abs(value[2] - value[0]) + abs(value[3] - value[1])
    y_distance = abs(value[1] - 2000000)
    if distance - y_distance > 0:
        for x in range(value[0] - (distance - y_distance), value[0] + distance - y_distance + 1):
            safe.add(x)
    if value[3] == 2000000: beacons.add(value[2])    

print(len(safe) - len(beacons))
