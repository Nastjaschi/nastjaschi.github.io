import math

class Triangle():
    def __init__(self,a,b,c): 
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (a + b + c)/2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def perimeter(self):
        return a + b + c 

    def scale(self, scale_factor):
        return Triangle(scale_factor * self.a, scale_factor * self.b, scale_factor * self.c)

    def is_valid(self):
        if self.c >= self.a+self.b or self.b >= self.c + self.a or self.a >= self.b + self.c:
            return False
        else:
            return True

    def is_right(self):
        if self.a**2 == self.b**2 + self.c**2 or self.b**2 == self.a**2 + self.c**2 or self.c**2 == self.b**2 + self.a**2:
            return True
        else:
            return False

t = Triangle(15,4,1)
print(t.is_valid())

t = Triangle(4,3,5)
print(t.is_right())