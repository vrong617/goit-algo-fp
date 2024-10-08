import turtle


def draw_pythagoras_tree(branch_len, angle, depth):
    if depth == 0:
        return

    turtle.forward(branch_len)

    turtle.left(angle)
    draw_pythagoras_tree(branch_len * 0.7, angle, depth - 1)

    turtle.right(2 * angle)
    draw_pythagoras_tree(branch_len * 0.7, angle, depth - 1)

    turtle.left(angle)
    turtle.backward(branch_len)


def setup_turtle():
    turtle.speed("fastest")
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()


def main():
    try:
        depth = int(input("Введіть рівень рекурсії (рекомендовано 5-10): "))
        setup_turtle()
        draw_pythagoras_tree(100, 30, depth)
        turtle.done()
    except KeyboardInterrupt:
        print("\nПрограма зупинена користувачем.")
        turtle.bye()


if __name__ == "__main__":
    main()
