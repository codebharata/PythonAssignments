
import easygui
import turtle
import math


def get_dimension(shape):
    while True:
        value = easygui.enterbox(
            f"Enter the dimension for your {shape} (50–250):",
            "Shape Dimension"
        )

        if value is None:
            return None

        try:
            dimension = float(value)

            if 50 <= dimension <= 250:
                return dimension

            easygui.msgbox(
                "Please enter a value between 50 and 250.",
                "Invalid Dimension"
            )

        except ValueError:
            easygui.msgbox(
                "Please enter a valid number.",
                "Invalid Input"
            )


def get_color():
    colors = [
        "blue", "red", "green", "yellow",
        "orange", "purple", "pink", "cyan",
        "teal", "black"
    ]

    color = easygui.choicebox(
        "Choose a fill color:",
        "Color Selection",
        colors
    )

    return color


def draw_square(pen, size, color):
    pen.fillcolor(color)
    pen.penup()
    pen.goto(-size / 2, -size / 2)
    pen.setheading(0)
    pen.pendown()

    pen.begin_fill()

    for _ in range(4):
        pen.forward(size)
        pen.left(90)

    pen.end_fill()


def draw_triangle(pen, size, color):
    height = size * math.sqrt(3) / 2

    pen.fillcolor(color)
    pen.penup()
    pen.goto(-size / 2, -height / 3)
    pen.setheading(0)
    pen.pendown()

    pen.begin_fill()

    for _ in range(3):
        pen.forward(size)
        pen.left(120)

    pen.end_fill()


def draw_concentric_circles(pen, radius, color):
    pen.fillcolor(color)
    pen.setheading(0)

    for r in range(int(radius), 0, -20):
        pen.penup()
        pen.goto(0, -r)
        pen.pendown()
        pen.begin_fill()
        pen.circle(r)
        pen.end_fill()


def draw_star(pen, size, color):
    pen.fillcolor(color)
    pen.penup()
    pen.goto(0, size / 2)
    pen.setheading(0)
    pen.left(90)
    pen.pendown()

    pen.begin_fill()

    for _ in range(5):
        pen.forward(size)
        pen.right(144)

    pen.end_fill()


def main():
    shapes = [
        "Square",
        "Equilateral Triangle",
        "Concentric Circles",
        "Custom Star"
    ]

    shape = easygui.choicebox(
        "Choose a geometric pattern to draw:",
        "Geometric Pattern Studio",
        shapes
    )

    if shape is None:
        return

    dimension = get_dimension(shape)

    if dimension is None:
        return

    color = get_color()

    if color is None:
        return

    screen = turtle.Screen()
    screen.title("Geometric Pattern Studio")
    screen.bgcolor("white")
    screen.setup(width=700, height=600)

    pen = turtle.Turtle()
    pen.speed(5)
    pen.pensize(3)
    pen.color("black", color)

    if shape == "Square":
        draw_square(pen, dimension, color)

    elif shape == "Equilateral Triangle":
        draw_triangle(pen, dimension, color)

    elif shape == "Concentric Circles":
        draw_concentric_circles(pen, dimension, color)

    elif shape == "Custom Star":
        draw_star(pen, dimension, color)

    pen.hideturtle()

    easygui.msgbox(
        f"Your {shape.lower()} has been drawn successfully!",
        "Drawing Complete"
    )

    screen.bye()


if __name__ == "__main__":
    main()