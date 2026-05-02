import pytest

from src.calculations import Calculation

class TestCalculation:
    calc = Calculation()

    @pytest.mark.parametrize("n1,n2,eval",
                             [(5,5,10),(-5,-5,-10),(0,5,5)
                             ])
    def test_add(self,n1,n2,eval):
        res = self.calc.add(n1,n2)
        assert res == eval,'Addition Error'

    @pytest.mark.parametrize("n1,n2,eval",
                             [(5, 5, 0), (-5, -5, -0),(0, 5, -5)
                             ])


    def test_sub(self,n1,n2,eval):
        res = self.calc.sub(n1,n2)
        assert res == eval,'Subtr Error'



    def test_mul(self):
        res = self.calc.mul(10,5)
        assert res == 50,'Multi Error'

    def test_div(self):
        res = self.calc.div(10,5)
        assert res == 2.0,'Division Error'


    @pytest.mark.skip(reason='NIV')
    def test_ne(self):
        res = self.calc.ne(10,10)
        assert res == True,'Not eql Error'


    @pytest.mark.xfail(reason='excep not handled')
    def test_diverror(self):
        #with pytest.raises(ZeroDivisionError):
        res = self.calc.div(10,0)
        assert res == 0









