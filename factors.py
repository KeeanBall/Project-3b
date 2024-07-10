print('Please enter a positive integer:')
number = int(input())
print(f'The factors of {number} are:')
factor = 1
while factor <= number:
    quotient = number / factor
    if int(quotient) == quotient:
        print(factor)
    factor += 1