import turtle
import math


def draw_square(t, side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)


def draw_pythagoras_tree(t, side_length, level):
    if level == 0:
        draw_square(t, side_length)
        return

    draw_square(t, side_length)

    t.forward(side_length)
    t.left(45)

    new_length = side_length / math.sqrt(2)

    draw_pythagoras_tree(t, new_length, level - 1)

    t.right(90)
    t.forward(new_length)
    t.left(90)

    draw_pythagoras_tree(t, new_length, level - 1)

    t.right(135)
    t.forward(side_length * math.sqrt(2))
    t.left(135)


def main():
    turtle_speed = 1
    recursion_level = int(input("Введіть рівень рекурсії: "))
    side_length = 100

    t = turtle.Turtle()
    t.speed(turtle_speed)
    turtle.tracer(0, 0)

    t.up()
    t.goto(-side_length / 2, side_length / 2)
    t.down()
    t.setheading(90)

    draw_pythagoras_tree(t, side_length, recursion_level)
    turtle.update()
    turtle.done()


if __name__ == "__main__":
    main()
