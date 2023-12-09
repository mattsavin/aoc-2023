from collections import defaultdict

lines = [x for x in open("input.txt", "r").read().strip().split("\n")]

def get_matching(line):
    winning = set(map(int, list(filter(None, line.split(":")[1].split("|")[0].split(' ')))))
    have = set(map(int, list(filter(None, line.split(":")[1].split("|")[1].split(' ')))))

    return winning.intersection(have)


def part1(lines):
    total = 0
    for line in lines:
        matched = get_matching(line)
        total += ((2 ** (len(matched) - 1)) if len(matched) > 0 else 0)

    return total


def part2(lines):
    card_number_count = defaultdict(int)
    for i, line in enumerate(lines):
        card_number_count[i] += 1
        matched = get_matching(line)

        for j in range (len(matched)):
            card_number_count[i+j+1] += card_number_count[i]

    return sum(card_number_count.values())

print(part2(lines))
