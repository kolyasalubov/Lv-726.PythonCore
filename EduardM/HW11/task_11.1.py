def main():
    user_age = int(input("Enter your age: "))
    if user_age < 0:
        raise ValueError("Age cannot be < 0")

    print("even" if user_age % 2 == 0 else "odd")


if __name__ == "__main__":
    main()
