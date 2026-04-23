Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
id(s1)
2569875699200
s2='hi'
id(s2)
140732402972088
s3=s1
id(s3)
2569875699200

s3
'hello'
s1
'hello'
s1='hi'
id(s1)
140732402972088
s1='india'
id(s1)
2569878380272


list1=[10,20,30,40]
list1
[10, 20, 30, 40]
type(list1)
<class 'list'>
<class 'list'>
SyntaxError: invalid syntax
list1[0]
10
list1[5]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list1[5]
IndexError: list index out of range
list1[-1]
40
list1[0:3]
[10, 20, 30]
list1[::2]
[10, 30]
list2=list('hi','hello')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list2=list('hi','hello')
TypeError: list expected at most 1 argument, got 2
list2=list('hi')
list2
['h', 'i']
s1
'india'
list2=list(s1)
list2
['i', 'n', 'd', 'i', 'a']
list3=list1
list3
[10, 20, 30, 40]
id(list1)
2569878390464
id(list3)
2569878390464
list4=[1000,'hello',1000,True,65.56]
list4
[1000, 'hello', 1000, True, 65.56]
list4[2]=40
list4
[1000, 'hello', 40, True, 65.56]
list4[5]='hi'
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list4[5]='hi'
IndexError: list assignment index out of range
list4[4]='hi'
list4
[1000, 'hello', 40, True, 'hi']
list4.append(45)
list4
[1000, 'hello', 40, True, 'hi', 45]
list4.remove('hi)
             
SyntaxError: unterminated string literal (detected at line 1)
list4.remove('hi')
             
list4.remove('hi')
             
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    list4.remove('hi')
ValueError: list.remove(x): x not in list
list4.append(200)
             

list4.append(200)
             
list4
             
[1000, 'hello', 40, True, 45, 200, 200]
list4.count(200)
             
2

list4.insert(3,50)
             
list4
             
[1000, 'hello', 40, 50, True, 45, 200, 200]
id(list4)
             
2569834327872
list4.pop()
             
200
list4
             
[1000, 'hello', 40, 50, True, 45, 200]
list4.pop(4)
             
True
list4
             
[1000, 'hello', 40, 50, 45, 200]
list2.clear()
             
list2
             
[]
del(list2)
             
list2
             
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    list2
NameError: name 'list2' is not defined. Did you mean: 'list1'?
list1=list2
             
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    list1=list2
NameError: name 'list2' is not defined. Did you mean: 'list1'?
list2=list1
             
list2
             
[10, 20, 30, 40]
tuple1=(11,22,33,44,55)
             
tuple1
             
(11, 22, 33, 44, 55)
tuple1[3]
             
44
tuple1[6]
             
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    tuple1[6]
IndexError: tuple index out of range
tuple1[3]=333
             
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    tuple1[3]=333
TypeError: 'tuple' object does not support item assignment
tuple1[0:4]
             
(11, 22, 33, 44)
tuple1[:2}
             
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
tuple1[::-2]
             
(55, 33, 11)
tuple1.index(44)
             
3
tuple1.count(22)
             
1
tuple2=tuple1
             
tuple2
             
(11, 22, 33, 44, 55)
id(tuple1)
             
2569836122304
id(tuple2)
             
2569836122304
tuple3=tuple(list2)
             
tuple3
             
(10, 20, 30, 40)
list2
             
[10, 20, 30, 40]
list1.append(tuple1)
             
list1
             
[10, 20, 30, 40, (11, 22, 33, 44, 55)]
list1[-1]
             
(11, 22, 33, 44, 55)
list5=list(tuple1)
             
list5
             
[11, 22, 33, 44, 55]
list1[3:1]
             
[]
list1[3][2]
             
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    list1[3][2]
TypeError: 'int' object is not subscriptable
list1[3][2]
             
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    list1[3][2]
TypeError: 'int' object is not subscriptable
set1={10,20,30}
             
set1
             
{10, 20, 30}
set2={10,20,30,40,50}
             
set2
             
{50, 20, 40, 10, 30}
set2.add(25)
             
set2
             
{50, 20, 40, 25, 10, 30}
set2.add('25')
             
set2
             
{50, '25', 20, 40, 25, 10, 30}
set3=set(set2)
             
set3
             
{50, '25', 20, 40, 25, 10, 30}
set3.remove('25')
             
set3
             
{50, 20, 40, 25, 10, 30}
set2
             
{50, '25', 20, 40, 25, 10, 30}
set2.union(set3)
             
{40, 10, 50, '25', 20, 25, 30}
set2.intersection(set3)
             
{40, 10, 50, 20, 25, 30}
set2.add(list2)
             
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    set2.add(list2)
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
set1.add(tuple2)
             
set1
             
{10, (11, 22, 33, 44, 55), 20, 30}

dict1={1:10,2:20,3:30}
             
dict1[2]
             
20
dict2={'a':10,'b':20,'c':30}
             
dict2['c'}
             
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
dict2['c']
             
30
stud={'rno':101,'name':'AAA','city':'BBB')
             
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
stud={'rno':101,'name':'AAA','city':'BBB'}
             
stud['name']
             
'AAA'
stud['name']='xxx'
             
stud
...              
{'rno': 101, 'name': 'xxx', 'city': 'BBB'}
>>> stud['fname']='yyy'
...              
>>> stud
...              
{'rno': 101, 'name': 'xxx', 'city': 'BBB', 'fname': 'yyy'}
>>> stud.get('name')
...              
'xxx'
>>> stud.keys()
...              
dict_keys(['rno', 'name', 'city', 'fname'])
>>> stud.values()
...              
dict_values([101, 'xxx', 'BBB', 'yyy'])
>>> stud.pop
...              
<built-in method pop of dict object at 0x0000025658B090C0>
>>> 
9
>>> stud.pop('fname')
...              
'yyy'
>>> stud
...              
{'rno': 101, 'name': 'xxx', 'city': 'BBB'}
