import math
  
class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    # Function in the Class---->Methods
    def add(self, fraction_2):
        result_num = self.num * fraction_2.den + fraction_2.num * self.den
        result_den = self.den * fraction_2.den
        result_fraction = Fraction(result_num, result_den)
        result_fraction.simplify()  
        return result_fraction

    def subtract(self, fraction_2):
        result_num = self.num * fraction_2.den - fraction_2.num * self.den
        result_den = self.den * fraction_2.den
        result_fraction = Fraction(result_num, result_den)
        result_fraction.simplify()  
        return result_fraction

    # def multiply2(self,fraction_1,fraction_2):
    #     result_num = fraction_1.num * fraction_2.num
    #     result_den = fraction_2.den * fraction_2.den
    #     result_fraction = Fraction(result_num, result_den)
    #     result_fraction.simplify()  
    #     return result_fraction  

    def multiply(self, fraction_2):
        result_num = self.num * fraction_2.num
        result_den = self.den * fraction_2.den
        result_fraction = Fraction(result_num, result_den)
        result_fraction.simplify()  
        return result_fraction  

    def divide(self, fraction_2):
        result_num = self.num * fraction_2.den
        result_den = self.den * fraction_2.num
        result_fraction = Fraction(result_num, result_den)
        result_fraction.simplify()  
        return result_fraction
        
    def simplify(self):
        common_divisor = math.gcd(self.num, self.den)
        self.num //= common_divisor
        self.den //= common_divisor
    
    def to_decimal(self):
        return self.num / self.den
    
    # def show(self):
    #     print(self.num , "/",self.den)
try:

    numerator1 = int(input("enter the numerator of the first fraction: "))
    denominator1 = int(input("enter the denominator of the first fraction: "))

    numerator2 = int(input("enter the numerator of the second fraction: "))
    denominator2 = int(input("enter the denominator of the second fraction: "))

    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)

    result_sum = fraction1.add(fraction2)
    result_subtract = fraction1.subtract(fraction2)
    result_multiply = fraction1.multiply(fraction2)
    # result_multiply = fraction2.multiply2(fraction1)
    result_divide = fraction1.divide(fraction2)
    result_decimal1=fraction1.to_decimal()
    result_decimal2=fraction2.to_decimal()

    print(f"SUM: {result_sum.num}/{result_sum.den}")
    print(f"SUB: {result_subtract.num}/{result_subtract.den}")
    print(f"MULT: {result_multiply.num}/{result_multiply.den}")
    print(f"DIV: {result_divide.num}/{result_divide.den}")
    print(f"Decimal: {result_decimal1:.2f}")
    print(f"Decimal: {result_decimal2:.2f}")

except ValueError:
    print("you must enter an integer number!")
