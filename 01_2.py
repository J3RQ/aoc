elves = open("1.txt").read().split('\n\n')

sumlist = []
for numbers in elves:
    sumlist.append(sum([int(x) for x in numbers.split('\n') if x != '']))
sumlist.sort(reverse=True)
print(sum([int(x) for x in sumlist if sumlist.index(x) <= 2]))
