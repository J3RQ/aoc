lines = open("08.txt").read().splitlines()
trees = []
for line in lines:
    trees.append([int(tree) for tree in line])


viewAreas = []
moveDirections = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for line in range(len(trees)):
  for tree in range(len(trees[0])):
    area = 1
    for x, y in moveDirections:
        line2 = 0
        x2 = line + x
        y2 = tree + y
        while 0 <= x2 < len(trees) and 0 <= y2 < len(trees[0]):
            line2 += 1
            if not trees[x2][y2] >= trees[line][tree]:
                x2 += x
                y2 += y
            else:
                break
        area = area * line2
    viewAreas.append(area)
print(max(viewAreas))
