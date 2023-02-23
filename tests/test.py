from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def testMulPositive(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def testDivPositive(self):
        assert self.calc.division(self, 10, 5) == 2

    def testSubPositive(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def testAddPositive(self):
        assert self.calc.adding(self, 10, 5) == 15
