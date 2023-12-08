data = open("day1.txt", "r").read().split("\n")

fullArray = []
smallArray = []

for s in data:
    s = s.replace("one", "1")
    s = s.replace("two", "2")
    s = s.replace("three", "3")
    s = s.replace("four", "4")
    s = s.replace("five", "5")
    s = s.replace("six", "6")
    s = s.replace("seven", "7")
    s = s.replace("eight", "8")
    s = s.replace("nine", "9")
    for t in s:
        if t.isdigit():
            smallArray.append(t)
    fullArray.append(smallArray)
    smallArray = []

print(sum(int(i[0] + i[len(i)-1]) for i in fullArray))