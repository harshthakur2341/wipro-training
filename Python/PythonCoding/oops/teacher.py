from oops.college import College


class Teacher(College):
    def _init__(self, ccode,cname,ccity,eid,tn,dp,bp):
        super()._init__(ccode,cname,ccity)
        self.empid = eid
        self.tname = tn
        self.dept = dp
        self.basicpay = bp

    def calculate_salary(self):
        return self.basicpay + (self.basicpay * 0.2)-(self.basicpay * 0.08)
