from itertools import permutations
from pdb import lasti2lineno
import re


example = [
    '[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}',
    '[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}',
    '[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}',
]

full = [r.strip() for r in open('input.txt', 'r').readlines()]

def parse_row(row):
    # Split by brackets and parentheses
    parts = row.split('] ')
    target = parts[0][1:]  # Remove leading '['
    
    # Extract moves (all the parentheses parts)
    moves_and_joltage = parts[1]
    moves_start = 0
    moves_end = moves_and_joltage.rfind(')') + 1
    moves_str = moves_and_joltage[moves_start:moves_end]
    
    # Parse moves
    moves = []
    for match in re.finditer(r'\(([^)]+)\)', moves_str):
        indices = [int(x) for x in match.group(1).split(',')]
        moves.append(indices)
    
    # Extract joltage
    joltage_str = moves_and_joltage[moves_end:].strip()
    joltage = [int(x) for x in joltage_str.strip('{}').split(',')]
    
    return target, moves, joltage

# Parse all examples
parsed_examples = [parse_row(row) for row in example]
parsed_full = [parse_row(row) for row in full]

def toggle(s:str):
    if s == '.':
        return '#'
    elif s == '#':
        return '.'

def press(state:str, move:tuple[int]):
    new = ''
    for i, s in enumerate(state):
        if i in move:
            new += toggle(s)
        else:
            new += s
    return new

def solve(state, target, moves, memo=None, path=None):
    if memo is None:
        memo = {}
    if path is None:
        path = []
    # end cases
    if state == target: return []
    if state in memo: return memo[state]
    if state in path: return None

    best = None
    path.append(state)
    for move in moves:
        result = solve(press(state, move), target, moves, memo=memo, path=path.copy()) 
        if result is not None:
            result = [move] + result
            if best is None or len(result) < len(best):
                best = result

    memo.update({state: best})
    return best

part1 = 0
for target, moves, _ in parsed_examples:
    state = '.' * len(target)
    part1 += len(solve(state, target, moves))

print(f'{part1 = }')

part1 = 0
for target, moves, _ in parsed_full:
    state = '.' * len(target)
    part1 += len(solve(state, target, moves))

print(f'{part1 = }')
