import math, re

board = list(open('input.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '0123456789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p) for p in chars.values()))
print(sum(math.prod(p) for p in chars.values() if len(p)==2))