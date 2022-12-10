import re


user_password = input("Password:\n")


def check_password(password: str) -> None:
    """
    Function for check the validity of a password (input from users).
    """
    if re.findall("[a-z]", password) == []:
        print("At least 1 letter between [a-z]")
    if re.findall("[A-Z]", password) == []:
        print("And 1 letter between [A-Z]")
    if re.findall("[$#@]", password) == []:
        print("At least 1 character from [$#@]")
    if re.findall("[0-9]", password) == []:
        print("At least 1 number between [0-9]")
    if 6 >= len(password) <= 16:
        print("Minimum length 6 characters.\nMaximum length 16 characters.")


def main() -> None:
    check_password(user_password)


if __name__ == "__main__":
    main()
