import string

rucksacks = open("3.txt").read().splitlines()

sum = 0
index = 0
letters = string.ascii_letters
while index < len(rucksacks):
    sacks = [rucksacks[index], rucksacks[index+1], rucksacks[index+2]]
    common = set[0].intersection(*[set(x) for x in sacks][1:])
    for letter in letters:
        if letter in sacks[0] and letter in sacks[1] and letter in sacks[2]:
            sum += letters.index(letter) + 1
    index += 3

print(sum)
