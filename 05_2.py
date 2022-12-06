import re
lines = open("5.txt").read().splitlines()

numbers = [str(x) for x in lines if re.search(r"([0-9]+\s+){3,}[0-9]+", x)][0]
cratecount = max([int(x) for x in numbers.split(" ") if x != ''])

crates = []
for index in range(lines.index(numbers)):
    crates.append([])

for index, row in enumerate(lines):
    if index == lines.index(numbers):
        break
    for number in range(cratecount):
        crates[index].append(row[numbers.find(str(number+1))])

verticalCrates = []
for index in range(cratecount):
    verticalCrates.append([])
    for crate in crates:
        if crate[index] != ' ':
            verticalCrates[index].append(crate[index])

start = lines.index(numbers) + 1 
for index, line in enumerate(lines):
    if index > start:
        numbers = re.findall(r"\d+", line)
        movelist = []
        for move in range(int(numbers[0])):
            movelist.append(verticalCrates[int(numbers[1])-1][0])
            verticalCrates[int(numbers[1])-1].pop(0)
        movelist.reverse()
        for move in movelist:
            verticalCrates[int(numbers[2])-1].insert(0, move)

answer = ""
for x in verticalCrates:
    answer += x[0]

print(answer)
