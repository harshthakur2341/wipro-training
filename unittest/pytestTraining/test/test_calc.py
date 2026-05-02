from src.calculations import Calculation


class TestCalc:
    calc = Calculation()

    def test_area_of_suare(self):
        res=self.calc.area_of_square(10)
        assert res == 100,'Area Is wrong'

    def test_area_of_rect(self):
        res=self.calc.area_of_rect(10,5)
        assert res == 50,'Area rect Is wrong'
