class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):                 # setting new width of rectangle
        self.width = new_width

    def set_height(self, new_height):               # setting new height of rectangle
        self.height = new_height

    def get_area(self):                            # getting the area of the rectangle
        return self.width * self.height

    def get_perimeter(self):                        # getting the perimrter
        return 2 * (self.width + self.height)

    def get_diagonal(self):                        # getting the diagonal
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):                        # getting the picture of the rectangle
        if self.width >50 or self.height > 50:
            return "Too big for picture."
        row = ""
        for i in range(self.height):
            row += self.width * "*" + "\n"
        return row

    def get_amount_inside(self, shape):     # getting amount of how many shapes can be fit inside
        count = 0
        if self.width > shape.width and self.height > shape.height:
            count += self.get_area() // shape.get_area()
        else:
            return 0

        return count


    def __repr__(self):                        # getting the string representation
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    
    def __init__(self,side,):
        super().__init__(side, side)
    
    def set_side(self, side):                   # setting new side of the square
        super().set_width(side)
        super().set_height(side)

    def __repr__(self):                        # getting the string representation
        return f"Square(side={self.width})"


rect = Rectangle(5, 5)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))