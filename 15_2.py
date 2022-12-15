lines, values = open("15.txt").read().splitlines(), list()
lines = [x.split() for x in lines]
for line in lines:
    values.append([int(x.replace(":", "").replace(",", "").split("=")[1]) for i, x in enumerate(line) if i in [2, 3, 8, 9]])

for i in range(4000000):
    def findTuning():
        y = 0
        while y <= 4000000:
            for value in values:
                distance = abs(y - value[0]) + abs(i - value[1])
                if distance <= abs(value[2] - value[0]) + abs(value[3] - value[1]):
                    y += abs(value[2] - value[0]) + abs(value[3] - value[1]) - distance
                    break
            else:
                return y * 4000000 + i
            y += 1
    find = findTuning()
    if find is not None:
        print(find)
        break

