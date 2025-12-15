from abc import abstractmethod
import re
import statistics


example = [
    '[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}',
    '[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}',
    '[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}',
]

def parse_example_row(row):
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
parsed_examples = [parse_example_row(row) for row in example]

class Indicator():
    def __init__(self, target:str, moves:list[tuple]):
        self.state = '.' * len(target)
        self.target = target
        self.moves = moves

    def press(self, button:int):
        move = self.moves[button]
        new = ''
        for i, s in enumerate(self.state):
            if i in move:
                new += self.toggle(s)
            else:
                new += s
        self.state = new

    @staticmethod
    def toggle(s:str):
        if s == '.':
            return '#'
        elif s == '#':
            return '.'
        
    def search(self):
        c = 0
        if self.state == self.target:
            return c
        
        
