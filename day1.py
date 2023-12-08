def partOne(data):
    fullArray = []
    smallArray = []

    for line in data:
        for character in line:
            if character.isdigit():
                smallArray.append(character)
        fullArray.append(smallArray)
        smallArray = []

    print("Part one: ", sum(int(i[0] + i[-1]) for i in fullArray))


def partTwo(data):
    # Numbers can only be a part of another with the first or last letters
    translation = {'zero': 'z0o', 'one': 'o1e', 'two': 't2o', 'three': 't3e',
               'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n',
               'eight': 'e8t', 'nine': 'n9e'}

    total = 0
    for line in data:
        for key, value in translation.items():
            line = line.replace(key, value)
        numbers = [j for j in line if j.isdigit()]
        total  += int(numbers[0] + numbers[-1])
    print("Part two: ", total)

data = open("day1.txt", "r").read().split("\n")
partOne(data)
partTwo(data)
