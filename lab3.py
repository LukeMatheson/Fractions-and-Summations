from Fraction import Fraction


def H(n):
    counter = 1
    finalFraction = Fraction(0, 1)
    for x in range(n):
        newFraction = Fraction(1, counter)
        finalFraction = finalFraction + newFraction
        counter += 1
    return finalFraction


def T(n):
    finalFraction = Fraction(0, 1)
    for x in range(n + 1):
        newFraction = Fraction(1, 2)
        finalFraction = finalFraction + (newFraction ** x)
    return finalFraction


def Z(n):
    fraction1 = Fraction(0, 1)
    for x in range(n + 1):
        newFraction = Fraction(1, 2)
        fraction1 = fraction1 + (newFraction ** x)
    fraction2 = Fraction(2, 1)
    finalFraction = fraction2 - fraction1
    return finalFraction


def R(n, b):
    counter = 1
    finalFraction = Fraction(0, 1)
    for x in range(n):
        newFraction = Fraction(1, counter)
        newFraction2 = newFraction ** b
        finalFraction = finalFraction + newFraction2
        counter += 1
    return finalFraction


test = 0
print('Welcome to Fun with Fractions!')
userInput = int(input('Enter Number of iterations (integer > 0):\n'))
while test == 0:
    if userInput <= 0:
        print('Bad Input')
        userInput = int(input('Enter Number of iterations (integer > 0):\n'))
    else:
        test += 1
fractionH = H(userInput)
print('H(' + str(userInput) + ')=' + str(fractionH))
decimalH = fractionH.num / fractionH.den
print('H(' + str(userInput) + ')~=' + str(decimalH))
fractionT = T(userInput)
print('T(' + str(userInput) + ')=' + str(fractionT))
decimalT = fractionT.num / fractionT.den
print('T(' + str(userInput) + ')~=' + str(decimalT))
fractionZ = Z(userInput)
print('Z(' + str(userInput) + ')=' + str(fractionZ))
decimalZ = fractionZ.num / fractionZ.den
print('Z(' + str(userInput) + ')~=' + str(decimalZ))
counter = 2
for z in range(7):
    fractionR = R(userInput, counter)
    print('R(' + str(userInput) + ',' + str(counter) + ')=' + str(fractionR))
    decimalR = fractionR.num / fractionR.den
    print('R(' + str(userInput) + ',' + str(counter) + ')~=' + str(decimalR))
    counter += 1
