Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
s1.capitalize()
'Hello'
s1.upper()
'HELLO'
s1
'hello'
s1.lower()
'hello'
s1='hEllO'
s1.casefold()
'hello'
s1='HeLLo'
s1.casefold()
'hello'
s1.count(l)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s1.count(l)
NameError: name 'l' is not defined
s1.count('o')
1
s1.endswith()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s1.endswith()
TypeError: endswith expected at least 1 argument, got 0
s1.endswith('o')
True
s1.find('l')
-1
s1.find('o')
4
s1.index('o')
4
s1.index('l')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s1.index('l')
ValueError: substring not found
s1.isalpha()
True
s1.join('there')
'tHeLLohHeLLoeHeLLorHeLLoe'
s1.replace('L','l')
'Hello'
s1
'HeLLo'
s1='hello there - how are you'
s1.split('-')
['hello there ', ' how are you']
s1='hello there  how are you'
s1.split(' ')
['hello', 'there', '', 'how', 'are', 'you']
s1.split('')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s1.split('')
ValueError: empty separator
s1.swapcase()
'HELLO THERE  HOW ARE YOU'
s1='hello there !!!'
len(s1)
15
s1[1]
'e'
s1[1:12]
'ello there '
s1[14]
'!'
s1[-6]
'r'
s1[-4]
' '
s1[-16]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s1[-16]
IndexError: string index out of range
s1[0:5]
'hello'
s1[0:10]
'hello ther'
'hello ther'
'hello ther'
s1[:]
'hello there !!!'
s1[2:12:3]
'l e '
s1[::2]
'hlotee!!'
s1[-15:-10]
'hello'
s1[-15:10]
'hello ther'

=========================== RESTART: C:/wipro training/Python/s1_fuction.py ===========================
*
*
*
*
*
*
*
*
*
*
*

=========================== RESTART: C:/wipro training/Python/s1_fuction.py ===========================
*-*-*-*-*-*-*-*-*-*-*-

=========================== RESTART: C:/wipro training/Python/s1_fuction.py ===========================
h
e
l
l
o
 
t
h
e
r
e

=========================== RESTART: C:/wipro training/Python/s1_fuction.py ===========================
h
e
l
l
o
 
t
h
e
r
e
 
!
!
!
>>> 
===================== RESTART: C:/wipro training/Python/s1_fuction.py =====================
h
e
l
l
o
>>> 
===================== RESTART: C:/wipro training/Python/s1_fuction.py =====================
h
e
l
l
o
 
t
h
e
r
e
 
!
!
!
