import turtle


def draw_tree(branch_len, t, level):
    if level > 0:
        t.forward(branch_len)
        t.right(25)
        draw_tree(branch_len * 0.75, t, level - 1)
        t.left(50)
        draw_tree(branch_len * 0.75, t, level - 1)
        t.right(25)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    recursion_level = int(input("Please enter the recursion level: "))
    draw_tree(100, t, recursion_level)
    my_win.exitonclick()


if __name__ == "__main__":
    main()
