from employeedetails import EmployeeDetails

#driver
eno = int(input('Emp no '))
name = input('Enter the name ')
bp = float(input('basic pay '))

employee = EmployeeDetails(empno = eno,ename = name, basic_pay= bp)


print('Emp no :',employee.get_empno())
print('emp name :', employee.ename)
print(' basic pay :', employee.basic_pay)
print('salary :', employee.calculate_netsal())



