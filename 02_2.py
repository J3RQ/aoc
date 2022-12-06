plays = open("2.txt").read().split('\n')
    
rps = [["A", "B", "C"],["X", "Y", "Z"]]
points = 0
for play in plays:
    arr = [x.split(" ") for x in play.split('\n') if x != '\n'][0]
    if len(arr) == 2:
        aIndex = rps[0].index(arr[0])
        bIndex = rps[1].index(arr[1])
        if bIndex == 0:
            if aIndex != 0:
                points += aIndex
            else:
                points += 3
        elif bIndex == 1:
            points += aIndex + 1 + 3
        elif bIndex == 2:
            points += 6
            if aIndex < 2:
                points += aIndex + 2
            else:
                points += 1


print(points)
