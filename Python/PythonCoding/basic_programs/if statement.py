"""
Date-22/04/2026
 Learning various if statement
"""
#biggest of 2
'''
number1 = int(input("Enter A number"))
number2 = int(input("Enter A number"))

if number1 == number2:
    print('both are same')
elif number1 > number2:
    print(number1,'is big')
else:
    print(number2,'is big')  '''


 #biggest of 3
'''number1 = int(input("Enter A number"))
number2 = int(input("Enter A number"))
number3 = int(input("Enter A number"))

if number1 == number2 and number2 == number3:
    print('all value are equal ')

elif number1 > number2 and number1 > number3:
    print(number1,'is biggest')
elif number2 > number1 and number2 > number3:
    print(number2,'is biggest')
elif number3 > number2 and number3 > number1:
    print(number3,'is biggest')'''

#weekday
choice = int(input("Enter A number btw 1-7"))

match choice:
    case 1:
        print('monday')
    case 2:
        print('Tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case 6:
        print('satday')
    case 7:
        print('sunday')
    case _:
        print('invalid')
        







