elves = open("1.txt").read().split('\n\n')

largest = 0
for numbers in elves:
    calories = sum([int(x) for x in numbers.split('\n') if x != ''])
    if calories > largest:
        largest = calories
print(largest)
