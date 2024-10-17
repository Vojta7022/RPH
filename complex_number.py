class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    
    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)
    
    def print(self):
        if self.imaginary >= 0:
            print(f"{self.real} + {self.imaginary}i")
        else:
            print(f"{self.real} - {abs(self.imaginary)}i")

c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)
c3 = c1 + c2
c3.print()
c4 = c1 - c2
c4.print()
c5 = c1 * c2
c5.print()