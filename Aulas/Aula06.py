n1 = int(input('Type the first number: '))
n2 = int(input('Type the second number: '))
s = n1 + n2
print('The sum of {} and {} results in {}.'.format(n1, n2, s))

n3 = bool(input('Type a number: '))
# If the user don't type anything, the result will be 'False'.
print(n3)

n4 = input('Type any character: ')
print(n4.isnumeric())
