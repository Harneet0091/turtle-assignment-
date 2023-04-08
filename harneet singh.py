import turtle

class Shape:
    def __init__(self, sides, length, color):
        self.sides = sides
        self.length = length
        self.color = color
        self.t = turtle.Turtle()

    def draw(self):
        self.t.pencolor(self.color)
        for _ in range(self.sides):
            self.t.forward(self.length)
            self.t.right(360 / self.sides)

class Square(Shape):
    def __init__(self, length, color):
        super().__init__(4, length, color)

class Triangle(Shape):
    def __init__(self, length, color):
        super().__init__(3, length, color)

class Pentagon(Shape):
    def __init__(self, length, color):
        super().__init__(5, length, color)

class Hexagalon(Shape):
    def __init__(self, length, color):
        super().__init__(6, length, color)

class Heptagon(Shape):
    def __init__(self, length, color):
        super().__init__(7, length, color)      

class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.t = turtle.Turtle()

    def draw(self):
        self.t.pencolor(self.color)
        self.t.forward(self.width)
        self.t.right(90)
        self.t.forward(self.height)
        self.t.right(90)
        self.t.forward(self.width)
        self.t.right(90)
        self.t.forward(self.height)


def main():
    turtle.speed(0)
    turtle.bgcolor("black")

    square = Square(100, "red")
    square.draw()

    triangle = Triangle(100, "blue")
    triangle.t.penup()
    triangle.t.goto(-150, 0)
    triangle.t.pendown()
    triangle.draw()

    pentagon = Pentagon(100, "green")
    pentagon.t.penup()
    pentagon.t.goto(150, 0)
    pentagon.t.pendown()
    pentagon.draw()


    hexagalon = Hexagalon(120, "purple")
    hexagalon.t.penup()
    hexagalon.t.goto(180, 300)
    hexagalon.t.pendown()
    hexagalon.draw()

    rectangle = Rectangle(160,100, "white")
    rectangle.t.penup()
    rectangle.t.goto(160, -200)
    rectangle.t.pendown()
    rectangle.draw()


    heptagon = Heptagon(90, "yellow")
    heptagon.t.penup()
    heptagon.t.goto(10, 400)
    heptagon.t.pendown()
    heptagon.draw()
    
    
    turtle.done()

if __name__ == "__main__":
    main()
