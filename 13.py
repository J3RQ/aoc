lines = open("13.txt").read().split("\n\n")
lines = [x.strip().split("\n") for x in lines]
correctOrder = []

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return (right-left > 0) - (right-left < 0)
    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            if compare(left[i], right[i]) != 0:
                return compare(left[i], right[i])
        return (len(right) - len(left) > 0) - (len(right) - len(left) < 0)
    if isinstance(left, list):
        return compare(left, [right])
    else:
        return compare([left], right)

for index, line in enumerate(lines):
    left = eval(line[0])
    right = eval(line[1])
    if compare(left, right) > 0:
        correctOrder.append(index+1)

print(sum(correctOrder))
