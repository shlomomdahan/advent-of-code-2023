grid = open("day3.txt").read().splitlines()
total = 0

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch != "*":
            continue

        coords = set()

        for cr in [r-1, r, r+1]:
            for cc in [c-1, c, c+1]:
                if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(row) or not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc -= 1
                coords.add((cr, cc))

        if len(coords) != 2:
            continue

        numbers = []

        for cr, cc in coords:
            num_str = ""
            while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                num_str += grid[cr][cc]
                cc += 1
            numbers.append(int(num_str))

        total += numbers[0] * numbers[1]

print(total)

