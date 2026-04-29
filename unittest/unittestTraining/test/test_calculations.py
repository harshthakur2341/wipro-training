import sys
import unittest



from src.calculations import add,sub,mul,div,ne

class TestCalculations(unittest.TestCase):
    def test_add(self):
        res = add(10,5)
        self.assertEqual(15, res ,msg='Adition Err')


    def test_sub(self):
        res = sub(10,5)
        self.assertEqual(5, res ,msg='Subtr Err')

    def test_mul(self):
        res = mul(10,5)
        self.assertEqual(50, res ,msg='Multi Err')

    def test_div(self):
        res = div(10,5)
        self.assertEqual(2.0, res ,msg='Division Err')
    @unittest.skipIf(sys.version_info < (3,13),reason='Not Implemented')
    def test_ne(self):
        res = ne(10,100)
        self.assertTrue(res,msg='Not equal ')

    def test_diverr(self):
        #res = div(10,0)
        with self.assertRaises(ZeroDivisionError,msg='No Exception'):
            div(10,0)
