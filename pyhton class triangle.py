class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def peri(self):
        return self.a + self.b + self.c

tri=Triangle(1,2,3)
print(tri.peri())