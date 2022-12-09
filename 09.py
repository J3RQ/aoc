def tailMoveCounter(moveCount):
    lines = open("09.txt").read().splitlines()

    movements = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}

    x = [0 for x in range(moveCount)]
    y = [0 for x in range(moveCount)]
    visitedCoordinates = [(x[moveCount-1], y[moveCount-1])]
    for line in lines:
        for move in range(int(line.split(" ")[1])):
            direction = line.split(" ")[0]
            x[0] += movements[direction][0]
            y[0] += movements[direction][1]
            
            for tail in range(1, moveCount):        
                if abs(x[tail - 1] - x[tail]) <= 1 and abs(y[tail - 1] - y[tail]) <= 1:
                    continue
                if x[tail - 1] == x[tail]:
                    xOffset = 0
                    yOffset = (y[tail - 1] - y[tail]) / 2
                elif y[tail - 1] == y[tail]:
                    xOffset = (x[tail - 1] - x[tail]) / 2
                    yOffset = 0
                elif abs(x[tail - 1] - x[tail]) == 1:
                    xOffset = x[tail - 1] - x[tail]
                    yOffset = (y[tail - 1] - y[tail]) / 2
                elif abs(y[tail - 1] - y[tail]) == 1:
                    xOffset = (x[tail - 1] - x[tail]) / 2
                    yOffset = y[tail - 1] - y[tail]

                x[tail] += xOffset
                y[tail] += yOffset
            if ((x[moveCount-1], y[moveCount-1])) not in visitedCoordinates:
                visitedCoordinates.append((x[moveCount-1], y[moveCount-1]))
    return len(visitedCoordinates)

#part 1
print(tailMoveCounter(2))

#part 2 
print(tailMoveCounter(10))
