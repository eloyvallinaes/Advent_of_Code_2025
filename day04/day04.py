def frame(rolls):
    """
    Surround input grid with frame
    """
    H = len(rolls)
    W = len(rolls[0])
    framed = []
    for row in rolls:
        framed.append('.' + row + '.')
    return ['.' * W] + framed +  ['.' * W]


def check_adjacent(i, j, matrix):
    """
    Reachable '@' criterion
    """
    c = ''.join([row[j-1 : j+2] for row in matrix[i-1:i+2]]).count('@')
    if matrix[i][j] == '@':
        c = c - 1

    return c

def solve_grid(rolls):
    """
    Solve part 1 - count reachable '@' and return updated grid.
    """
    part1 = 0
    vis = []
    for i, row in enumerate(rolls):
        new = ''
        for j, item in enumerate(row):
            if item == '@':
                if check_adjacent(i, j, rolls) < 4:
                    new += 'x'
                    part1 += 1
                else:
                    new += '@'
            else:
                new += item
        vis.append(new)
    
    return vis, part1


# example input
rolls = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]


# input
rolls = frame([l.strip() for l in open('input.txt').readlines()])

# part 1 - count reachable '@', having fewer than 4 adjacent '@'
# part 2 - removing reachable '@', repeat until no more removals can be made

part2 = 0
while True:
    rolls, part1 = solve_grid(rolls)  # update grid and track changes
    if part1 > 0:  # no more changes
        part2 += part1
    else:
        break
