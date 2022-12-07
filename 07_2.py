lines = open("07.txt").read().splitlines()

dirs = {}
path = []
for line in lines:
    split = line.split(" ")
    if line[0] == '$':
        if split[1] == 'ls': continue
        if split[2] == '..':
            path.pop()
        else:
            path.append(split[2])
   
    elif line[0].isdigit():
        pathcopy = path.copy()
        while pathcopy:
            d = "/".join(pathcopy)
            dirs[d] = dirs.get(d, 0) + int(line.split(" ")[0])
            pathcopy.pop()

updateSpace = 30000000 - (70000000 - dirs["/"])

largeEnoughFolders = []
for dir in dirs:
    if dirs[dir] >= updateSpace:
        largeEnoughFolders.append(dirs[dir])

print(min(largeEnoughFolders))
