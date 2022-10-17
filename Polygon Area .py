class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        a = self.width*self.height
        return a

    def get_perimeter(self):
        a = 2*self.width + 2*self.height
        return a

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        if self.width <=50 and self.height <=50:
            a = ""
            for i in range(self.height):
                a += f"{self.width*'*'}\n"
            return a
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape: object):
        a = (self.height//shape.height)*(self.width//shape.width)
        return a
    def __str__(self):
        a = f"{type(self).__name__}(width={self.width}"
        a+= f", height={self.height})"
        return a


class Square(Rectangle):
    def __init__(self, length):
        self.height = self.width = length  

    def set_side(self, length):
        self.height = self.width = length

    def set_height(self, h):
        self.height = self.width = h
    
    def set_width(self, w):
        self.height = self.width = w

    def __str__(self):
        a = f"{type(self).__name__}(side={self.width})"
        return a

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))


