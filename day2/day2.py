from collections import defaultdict


lines = [x for x in open("day2.txt", "r").read().strip().split("\n")]

def part1(lines):
    total = 0
    for lines in lines:
        game_id = lines.split(":")[0].split(" ")[1]
        lines = lines.split(":")[1]
        possible = True
        for draw in lines.split(";"):
            d = defaultdict(int)
            for result in draw.split(", "):
                result = result.strip()
                d[result.split(" ")[1]] += int(result.split(" ")[0])
            if d["red"] > 12 or d["green"] > 13 or d["blue"] > 14:
                possible = False

        if possible:
            total += int(game_id)

    return total

print(part1(lines))