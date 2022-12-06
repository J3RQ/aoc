assignments = open("4.txt").read().splitlines()
sum = 0

for assignment in assignments:
    ranges = assignment.split(",")
    numbers = [x.split("-") for x in ranges]
    if int(numbers[0][0]) <= int(numbers[1][0]) and int(numbers[0][1]) >= int(numbers[1][1]):
        sum += 1
    elif int(numbers[0][0]) >= int(numbers[1][0]) and int(numbers[0][1]) <= int(numbers[1][1]):
        sum += 1
print(sum)
