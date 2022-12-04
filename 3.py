import string

rucksacks = open("3.txt").read().splitlines()

sum = 0
letters = string.ascii_letters
for sack in rucksacks:
    first = sack[:(int(len(sack)/2))]
    second = sack.replace(first, "")
    common = "".join(set(first).intersection(second))
    sum += letters.index(common) + 1 

print(sum)
