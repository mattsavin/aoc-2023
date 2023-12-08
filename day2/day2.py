from collections import defaultdict
def part_one(data):
    for i, j in enumerate(data):
        data[i] = j.split(": ")
        for k, l in enumerate(data[i]):
            data[i][k] = l.split("; ")
            for m, n in enumerate(data[i][k]):
                data[i][k][m] = n.split(", ")

    dictionary = defaultdict(lambda: defaultdict(data))

    return dictionary

data = open("day2.txt", "r").read().split("\n")
print(part_one(data))