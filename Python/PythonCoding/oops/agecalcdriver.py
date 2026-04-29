from oops.agecalc import AgeCalc
from oops.myexception import AgeException

age = int(input('Age: '))

aobj= AgeCalc()


try:
    aobj.voting_age_check(age)
    aobj.pension_age_check(age)

except AgeException as ae:
    print(ae)

else:
    print('Eligible , Do next Step...')
