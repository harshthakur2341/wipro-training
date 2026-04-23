"""
q2-22/02/26
"""
#enumerate

str = input('enter a word; ')
count = 0
for i,ch in enumerate(str):
    if ch == 'a':
        count = count + 1
print(count)