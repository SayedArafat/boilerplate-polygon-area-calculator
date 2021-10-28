class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        picture_string = ''
        if self.width <= 50 and self.height <= 50:
            for row in range(self.height):
                for col in range(self.width):
                    picture_string += '*'
                picture_string += '\n'
        else:
            picture_string += "Too big for picture."

        return picture_string

    def get_amount_inside(self, instance):
        amount = self.get_area() // instance.get_area()
        return amount

    def __str__(self):
        return_string = f'Rectangle(width={self.width}, height={self.height})'
        return return_string


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)
        self.side = side

    def set_width(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_height(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        return_string = f'Square(side={self.side})'
        return return_string


rect = Rectangle(7, 8)
sq = Square(2)
sq.set_side(4)
sq.set_side(2)

print(rect)
print(sq)
