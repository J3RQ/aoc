input = open("6.txt").read().splitlines()[0]

result = 0
for index, char in enumerate(input):
    chars = [char]
    for offset in range(1,14):
        chars.append(input[index+offset])
    if len(set(chars)) == len(chars):
        result = index+14
        break
print(result)
