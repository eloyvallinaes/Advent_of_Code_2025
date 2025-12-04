
# input
input = open('example.txt', 'r').read()
input = open('input.txt', 'r').read()

# part 1 - sum invalid in range. Invalid if left half mirrors right half.
def check_valid(number):
    number = str(number)
    if len(number) % 2 != 0:  # odd number of digits
        return True
    
    n = len(number) // 2
    if str(number)[:n] == number[n:]:  # mirrror condition
        return False
    
    return True

ss = 0
for pair in input.split(','):
    left, right = pair.split('-')
    for number in range(int(left), int(right) + 1):
        if check_valid(number) is False:
            ss += number

print(ss)


# part 2 - invalid are made of repeating sets of any size.

def check_valid(number):
    number = str(number)
    if len(number) == 1:  # single digit numbers
        return True
    
    if len(set(number)) == 1:  # single digit repetition
        return False
    
    # try splits until half size
    for div in range(2, len(number)//2 + 1):  
        if len(number) % div == 0:
            parts = [number[i:i+div] for i in range(0, len(number), div)]
            if len(set(parts)) == 1:  # part repetition condition
                return False
    return True

ss = 0
for pair in input.split(','):
    left, right = pair.split('-')
    for number in range(int(left), int(right) + 1):
        if check_valid(number) is False:
            ss += number

print(ss)