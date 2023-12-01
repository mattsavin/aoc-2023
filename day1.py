data = open("day1.txt", "r").read().split("\n")

fullArray = []
smallArray = []

for s in data:
    for t in s:
        if t.isdigit():
            smallArray.append(t)
    fullArray.append(smallArray)
    smallArray = []

print(sum(int(i[0] + i[len(i)-1]) for i in fullArray))