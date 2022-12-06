input = open("6.txt").read().splitlines()[0]

result = 0
for index, char in enumerate(input):
    chars = [char, input[index+1], input[index+2], input[index+3]]
    if len(set(chars)) == len(chars):
        result = index+4
        break
print(result)
