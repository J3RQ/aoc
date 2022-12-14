lines = open("14.txt").read().splitlines()

sandSource = (500, 0)
cave = {}

for line in (line.strip() for line in lines):
    parts = [x for x in line.split(" -> ")]
    parts = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in parts]
    first = parts[0]
    for part in parts:
        if part[1] > first[1]:
            direction = (0, 1)
        elif part[1] < first[1]:
            direction = (0, -1)
        elif part[0] > first[0]:
            direction = (1, 0)
        elif part[0] < first[0]:
            direction = (-1, 0)
        cave[first] = '.'
        while first != part:
            first = (first[0] + direction[0], first[1] + direction[1])
            cave[first] = '.'
        first = part 

def drop(sand):
    for dir in ((0,1),(-1,1),(1,1)):
        fall = (sand[0] + dir[0], sand[1] + dir[1])
        if fall not in cave:
            return fall
    return sand
    
sandCount = 0
ymax = max(x[1] for x in cave)
while True:
    sand = sandSource
    def pile(sand):
        global sandCount
        while True:
            if sand[1] > ymax:
                return sandCount
            old = sand
            sand = drop(sand)
            if sand == old:
                sandCount += 1
                cave[sand] = 'o'
                break
    pil = pile(sand)
    if pil != 1 and pil is not None:
        print(pil)
        break
    