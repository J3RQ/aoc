import functools
lines = [eval(x) for x in open("13.txt").read().splitlines() if x != '']
lines.extend([eval('[[2]]'), eval('[[6]]')])

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return (right-left > 0) - (right-left < 0)
    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            if compare(left[i], right[i]) != 0:
                return compare(left[i], right[i])
        return (len(right) - len(left) > 0) - (len(right) - len(left) < 0)
    if isinstance(left, list):
        return compare(left, [right])
    else:
        return compare([left], right)

sortedlines = sorted(lines, key=functools.cmp_to_key(compare))
sortedlines.reverse()
print((sortedlines.index([[2]])+1) * (sortedlines.index([[6]])+1))
