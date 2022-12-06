plays = open("2.txt").read().split('\n')
    
rps = [["A", "B", "C"],["X", "Y", "Z"]]
points = 0
test = 0
for play in plays:
    arr = [x.split(" ") for x in play.split('\n') if x != '\n'][0]
    if len(arr) == 2:
        points += rps[1].index(arr[1])+1
        aIndex = rps[0].index(arr[0])
        bIndex = rps[1].index(arr[1])
        if aIndex == bIndex:
            points += 3
        elif (bIndex > aIndex and bIndex - aIndex != 2) or bIndex - aIndex == -2:
            points += 6

print(points)
