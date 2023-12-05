grid = open("day3.txt").read().splitlines()
coords = set()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue
        for cr in [r-1, r, r+1]:
            for cc in [c-1, c, c+1]:
                if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(row) or not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc -= 1
                coords.add((cr, cc))

numbers = []

for r, c in coords:
    num_str = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        num_str += grid[r][c]
        c += 1
    numbers.append(int(num_str))

print(sum(numbers))
