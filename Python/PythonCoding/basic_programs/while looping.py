
""" while looping"""
#natural number

'''num = int(input('enter a number'))

value = 1
while value <= num:
    print(value)
    value = value + 1'''

#while
num = input('enter a number')
count = len(num)

som = 0
numint = int(num)
comp = numint

while numint > 0:
    rem = numint % 10
    som = som + rem ** count
    numint = numint // 10

if comp == som:
    print('Armstrong')
else:
    print('NA')