class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #print("create: " + name)
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        x = 0
        y = 0
        s = ""
        while y < self.height:
            x = 0
            while x < self.width:
                if y == 0 or y == (self.height - 1) or x == 0 or x == (self.width - 1):
                    s += "*"
                else:
                    s += "*" #would had thought you'd leave this blank but its not in the example
                x += 1
            s += "\n"
            y += 1
        return s
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    def get_amount_inside(self, other):
        x = 0
        y = 0
        num = 0
        while y < self.height:
            x = 0
            while x < self.width:
                if (y + other.height) <= self.height and (x + other.width) <= self.width:
                    num += 1
                    #y += other.height
                x += other.width
                #x += 1
            y += other.height
            #y += 1
        return num


class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.height = width
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.width = height
        self.height = height
    def set_side(self, width):
        self.width = width
        self.height = width
    def __str__(self):
        return "Square(side=" + str(self.width) + ")"
