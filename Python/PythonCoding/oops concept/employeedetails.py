class EmployeeDetails:
    def __init__(self, empno , ename ,basic_pay):
        self.__empno = empno
        self.__ename = ename
        self.__basic_pay = basic_pay
        self.__da = 20.0
        self.__hra = 10.0
        self.__pf = 5.5

    #def get_empno(self):
#return self.__empno

#def set_empno(self, eno):
#self.__empno = eno

    @property
    def empno(self):
        return self.__empno

    @empno.setter
    def empno(self, eno):
        self.__empno = eno

    @property
    def ename(self):
        return self.__ename
    @ename.setter
    def ename(self,en):
        self.__ename = en

    @property
    def basic_pay(self):
        return self.__basic_pay
    @basic_pay.setter
    def basic_pay(self,basic):
        self.__basic_pay = basic


    def __calculate_allowance(self):
        allowance = (self.__basic_pay * self.__da / 100) + (self.__basic_pay * self.__hra / 100)
        return allowance

    def __calculate_deduction(self):
        deduction = (self.__basic_pay * self.__pf / 100)
        return deduction

    def calculate_netsal(self):
        netsal = (self.__basic_pay + self.__calculate_allowance() - self.__calculate_deduction())
        return  netsal
