class MyVector:
    def __init__(self, values):
        self.values = values

    def get_vector(self):
        return self.values
    
    def __mul__(self, other):
        return sum(x1 * x2 for x1, x2 in zip(self.values, other.values))
    
    def is_perpendicular_to(self, other):
        return self * other == 0
    
    def cross_product(self, other):
        x1, y1, z1 = self.values
        x2, y2, z2 = other.values
        return MyVector([y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2])
    
    def __add__(self, other):
        return MyVector([x1+x2 for x1, x2 in zip(self.values, other.values)])
    
    def norm(self):
        return sum(i*i for i in self.values)**0.5
    
x = MyVector([1, 2, 3, 5])
y = MyVector([4, 5, 6, 0])
print(x.get_vector())
z = x + y
print(z.get_vector())
a = MyVector([0, 0])
print(a.norm())