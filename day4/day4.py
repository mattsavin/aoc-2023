lines = [x for x in open("input.txt", "r").read().strip().split("\n")]

def part1(lines):
    total = 0
    for line in lines:
        winning = set(map(int, list(filter(None, line.split(":")[1].split("|")[0].split(' ')))))
        have = set(map(int, list(filter(None, line.split(":")[1].split("|")[1].split(' ')))))

        matched = winning.intersection(have)
        total += ((2 ** (len(matched) - 1)) if len(matched) > 0 else 0)

    return total
    

print(part1(lines))
#part1(lines)