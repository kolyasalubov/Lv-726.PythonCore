from random import randint


def game() -> str:
    num = randint(1, 100)
    while True:
        user_num = int(input("Enter your number:"))
        if user_num < num:
            print("Number is greater then yours")
        elif user_num > num:
            print("Number is less then yours")
        else:
            print("Congratulations, you win!")
            break


def main() -> None:
    game()


if __name__ == "__main__":
    main()
