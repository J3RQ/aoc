monkeys = open("11.txt").read().split("\n\n")
monkeyRows = [x.split("\n") for x in monkeys]

items = [x[1].split(": ")[1] for x in monkeyRows]
monkeyItems = [x.split(", ") for x in items]
for index, monkey in enumerate(monkeyItems):
    intlist = [int(x) for x in monkey]
    monkeyItems[index] = [intlist[i] for i in range(len(intlist) - 1, -1, -1)]
operations = [x[2].split("= ")[1].strip() for x in monkeyRows]
test = [int(x[3].split("by ")[1]) for x in monkeyRows]
trueCondition = [int(x[4].strip()[-1]) for x in monkeyRows]
falseCondition = [int(x[5].strip()[-1]) for x in monkeyRows]
inspectCount = [0 for x in range(len(monkeys))]

testMultiplied = 1
for x in test:
    testMultiplied *= x

for round in range(10000):
    for monkey in range(len(monkeyItems)):
        for k in range(len(monkeyItems[monkey])):
            if len(monkeyItems[monkey]) == 0:
                continue
            item = monkeyItems[monkey].pop()
            inspectCount[monkey] += 1
            worry = eval(operations[monkey].replace('old', str(item))) % testMultiplied
            if worry % test[monkey] == 0:
                monkeyItems[trueCondition[monkey]].insert(0, worry)
            else:
                monkeyItems[falseCondition[monkey]].insert(0, worry)

inspectCount.sort()
print(inspectCount[-1] * inspectCount[-2])
