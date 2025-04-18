justin = Turtle()
justin_screen = Screen()


def forward():
    justin.forward(10)


def backward():
    justin.back(10)


def left():
    justin.left(10)


def right():
    justin.right(10)


def reset():
    justin.home()
    justin.clear()


justin_screen.listen()
justin_screen.onkey(fun=forward, key="w")
justin_screen.onkey(fun=backward, key="s")
justin_screen.onkey(fun=left, key="a")
justin_screen.onkey(fun=right, key="d")
justin_screen.onkey(fun=reset, key="c")


justin_screen.exitonclick()