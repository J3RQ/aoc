from collections import deque
import string

lines = open("12.txt").read().splitlines()
maze = [[*x] for x in lines]

end = None

openlist = []
closedlist = []

alphabet = string.ascii_lowercase
for i, row in enumerate(maze):
    if "S" in row:
        maze[i][row.index("S")] = "a"
    if "E" in row:
        end = (row.index("E"), maze.index(row))
        maze[i][row.index("E")] = "z"

answers = []
for index, row in enumerate(maze):
    for rowIndex, letter in enumerate(row):
        if letter == "a":
            vis = {}
            start = (rowIndex, index)
            vis[start] = 0

            Q = deque()
            Q.append(start)

            while Q:
                (x, y) = Q.popleft()
                current = vis[(x, y)]
                for x2, y2 in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    coordinates = (new_x, new_y) = x + x2, y + y2
                    if coordinates in vis or new_x in [-1, len(maze[0])]:
                        continue 
                    if new_y in [-1, len(maze)]: 
                        continue
                    if alphabet.index(maze[new_y][new_x]) - alphabet.index(maze[y][x]) <= 1:
                        vis[(new_x, new_y)] = current + 1
                        Q.append((new_x, new_y))
                        if (new_x, new_y) == end:
                            answers.append(current + 1)

answers.sort()
print(answers[0])
