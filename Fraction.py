class Fraction:
    def __init__(self, a, b):
        self.num = a
        self.den = b
        self.simplify()

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num)+"/"+str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def approximate(self):
        return self.num/self.den

    def simplify(self):
        x = self.gcd(self.num, self.den)
        self.num = self.num // x
        self.den = self.den // x

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def __add__(self, other):
        newNumerator = (self.num * other.den) + (other.num * self.den)
        newDenominator = self.den * other.den
        newFraction = Fraction(newNumerator, newDenominator)
        return newFraction

    def __sub__(self, other):
        fraction1 = Fraction(self.num, self.den)
        fraction2 = Fraction(-other.num, other.den)
        fraction3 = fraction1 + fraction2
        return fraction3

    def __mul__(self, other):
        newNumerator = self.num * other.num
        newDenominator = self.den * other.den
        newFraction = Fraction(newNumerator, newDenominator)
        return newFraction

    def __truediv__(self, other):
        newNumerator = self.num * other.den
        newDenominator = self.den * other.num
        newFraction = Fraction(newNumerator, newDenominator)
        return newFraction

    def __pow__(self, exp):
        if exp == 0:
            newFraction = Fraction(1, 1)
            return newFraction
        elif exp < 0:
            newNumerator = self.den ** -exp
            newDenominator = self.num ** -exp
            newFraction = Fraction(newNumerator, newDenominator)
            return newFraction
        else:
            newNumerator = self.num ** exp
            newDenominator = self.den ** exp
            newFraction = Fraction(newNumerator, newDenominator)
            return newFraction