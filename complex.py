class ComplexNumber:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def add(self, other):
        real_part = self.real + other.real
        image_part = self.image + other.image
        result = ComplexNumber(real_part, image_part)
        return result

    def multiply(self, other):
        real_part = self.real * other.real - self.image * other.image
        image_part = self.real * other.image + self.image * other.real
        result = ComplexNumber(real_part, image_part)
        return result

    def subtract(self, other):
        real_part = self.real - other.real
        image_part = self.image - other.image
        result = ComplexNumber(real_part, image_part)
        return result

# The __str__ method in a Python class defines a concise string representation of the object,returned when using str() or print()
# https://www.w3schools.com/python/python_classes.asp
    
    def __str__(self):
        return f"{self.real} + i {self.image}"


real1 = int(input("enter the real part of the first complex number: "))
imag1 = int(input("enter the imaginary part of the first complex number: "))
real2 = int(input("enter the real part of the second complex number: "))
imag2 = int(input("enter the imaginary part of the second complex number: "))

num1 = ComplexNumber(real1, imag1)
num2 = ComplexNumber(real2, imag2)



sum_result = num1.add(num2)
print(f"({num1}) + ({num2}) = {sum_result}")

multiply_result = num1.multiply(num2)
print(f" ({num1}) * ({num2}) = {multiply_result}")

subtract_result = num1.subtract(num2)
print(f"({num1}) - ({num2}) = {subtract_result}")
