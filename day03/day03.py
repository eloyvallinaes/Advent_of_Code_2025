import numpy as np


# input
input = [l.strip() for l in open('input.txt', 'r').readlines()]

examples = [
    '987654321111111',
    '811111111111119',
    '234234234234278',
    '818181911112111',
]


# part 1 - largest 2-digit number from digits in bank without rearranging
s = 0
for bank in input:
    bank = list(int(n) for n in bank)
    imax = np.argmax(bank[:-1])  # highest excluding last
    left = bank[imax]
    right = np.max(bank[imax+1:])

    s += int(''.join(str(p) for p in [left, right]))

print(s)


# part 2 - largest 12-digit number from digits in bank without rearranging
def grow_number(result, digits):
    if len(result) == 12:
        return result
    
    next_digit = max(digits)
    remainder = digits[digits.index(next_digit)+1:]
    n = len(digits)
    while len(remainder) + len(result) < 11:
        next_digit = max(digits[:n])
        remainder = digits[digits.index(next_digit)+1:]
        n -= 1
    
    return grow_number(result + next_digit, remainder)


ss = 0
for example in examples:
    ss += int(grow_number('', example))


input = [l.strip() for l in open('input.txt', 'r').readlines()]
ss = 0
for bank in input:
    ss += int(grow_number('', bank))

print(ss)