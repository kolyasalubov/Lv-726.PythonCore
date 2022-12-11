import square


def shape_choose():
    """This function asks user to choose one
    of the proposed shapes and returns it's square."""
    shape = int(input("Choose shape (1 - rectangle / 2 - triangle / 3 - circle): "))

    if shape == 1:
        print(square.rectangle_square())

    elif shape == 2:
        print(square.triangle_square())

    elif shape == 3:
        print(square.circle_square())

    else:
        print("You should choose one of the mentioned shapes.")
