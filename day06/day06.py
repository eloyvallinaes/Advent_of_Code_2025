def calculate(numbers: list, operator):
    print(f' {operator} '.join(numbers))
    if operator == '+':
        return sum(map(int, numbers))
    
    elif operator == '*':
        return eval(' * '.join(map(str, numbers)))
    

# input
# input = open('example.txt', 'r').readlines()
input = open('input.txt', 'r').readlines()


# part 1 - read top to bottom, left to rigth
operators = input[-1].split()
rows = input[:-1]

r = 0
for i, operator in enumerate(operators):
    r += calculate(list(row.split()[i] for row in rows), operator)
print(r)


# part 2 - read vertical numbers right to left
operators = input[-1].split()
rows = [r.strip('\n') for r in  input[:-1]]  # remove newline

r = 0
jmax = len(rows[0])-1
# operators right to left
for i in range(len(operators)-1, -1, -1):  
    numbers = []
    # columns right to left
    for j in range(jmax, -1, -1):
        # vertical number
        number = ''.join(list(row[j] for row in rows))
        # operation end condition
        if number.strip() == '':
            # will continue from next column
            jmax = j-1
            break
        else:
            numbers.append(number)

    # add up
    r += calculate(numbers, operators[i])

print(r)
