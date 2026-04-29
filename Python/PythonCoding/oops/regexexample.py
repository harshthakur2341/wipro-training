
import re
#beg and end match
'''txt = input('Enter a text ') # India is my country
bpat = input('Enter Beginning pattern ')#India
epat = input('Enter End pattern ') # country
bpat = '^'+bpat
epat = epat + '$'

if re.search(pattern = bpat,string= txt):
    print('Beginning pat Available ')
else:
    print('Beginning pat Not Available')

if re.search(pattern = epat,string= txt):
    print('Ending pat Available ')
else:
    print('Ending pat Not Available')'''

#digit

'''mbno = input('Enter a text ')
pat = '[0-9]'
#pat = r"\\d"

if re.fullmatch(pattern = pat , string = mbno):
    print('only digit')
else:
    print('Others char avbl')'''

#Username
'''
un= input('Enter Un ')
pat= r"^[a-z_]{8,}$"


if re.match(pattern=pat, string=un):
    print('valid un ')
else:
    print('Invalid')
'''

#Email

#emailadd = input('Email ')
#pat = r"^[a-z A-Z 0-9 _]+@[a-z]+\.[a-z]+$"

'''if re.match(pattern=pat, string=emailadd):
    print('Valid')
else:
    print('Invalid')'''

#password
'''
pwd = input('password : ')
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[-_@]).{8,}$"

if re.match(pattern=pat, string=pwd):
    print('Valid')
else:
    print('Invalid')
'''

txt=input('Text: ')
pat = r"\s+"

#print(re.sub(pattern = pat,string= txt,repl='*'))

print(re.split(pattern = pat,string= txt))

