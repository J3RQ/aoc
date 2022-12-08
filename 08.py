lines = open("08.txt").read().splitlines()

trees = []
for line in lines:
    trees.append([int(tree) for tree in line])

counter = 0
for line in range(len(trees)):
    for tree in range(len(trees[line])):
        if all(trees[line][x] < trees[line][tree] for x in range(tree)):
            counter += 1
        elif all(trees[line][x] < trees[line][tree] for x in range(tree+1, len(trees[line]))):
            counter += 1
        elif all(trees[x][tree] < trees[line][tree] for x in range(line)):
            counter += 1
        elif all(trees[x][tree] < trees[line][tree] for x in range(line+1, len(trees))):
            counter += 1
            
print(counter)
