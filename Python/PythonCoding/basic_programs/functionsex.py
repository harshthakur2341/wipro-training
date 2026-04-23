
#fuctions
'''def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div():
    pass



#driver
num1=int(input("enter first number  "))
num2=int(input("enter second number  "))

res = add(num1, num2)
print('add : ',res )

res = add(num1, num2)
print('sub : ',res )

res = add(num1, num2)
print('mul : ',res )
'''

#Arbitary
'''def add(*nums):
    sum =0
    for n in nums:
        sum = sum+n
    return sum



numbers = list()
count = int(input('how many   '))

for _ in range(1,count+1):
    numbers.append(int(input('no... ')))

print(add( 6,7,8))
'''

#optional
'''
def add(n1,n2,n3=10):
    return n1 + n2 +n3

num1=int(input("enter first number  "))
num2=int(input("enter second number  "))

print(add(num1, num2))
print(add(num1,num2))'''

#lambda
'''
num1=int(input("enter first number  "))
num2=int(input("enter second number  "))

add = lambda n1,n2 : n1 + n2

print(add(num1,num2))
'''

numbers = [1,2,3,4,5]
sq = lambda nums : [num * num     for num in nums ]

print(sq(numbers))






