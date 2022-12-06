assignments = open("4.txt").read().splitlines()

sum = 0

for assignment in assignments:
    ranges = assignment.split(",")
    numbers = [x.split("-") for x in ranges]
    range1 = range(int(numbers[0][0]), int(numbers[0][1])+1)
    range2= range(int(numbers[1][0]), int(numbers[1][1])+1)
    rset = set(range1)
    if len(rset.intersection(range2)) != 0:
        sum += 1
    
    
print(sum)
