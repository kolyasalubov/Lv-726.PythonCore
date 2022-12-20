import re


def pass_check(password):
    """This function checks whether entered password is valid."""

    # Output messages.
    valid = "Your password is valid."
    unvalid = "Try another password that will satisfy requirements."

    def pass_len(password):
        """This function checks whether password
        has correct lenght (6-16 characters)."""
        if len(password) < 6 or len(password) > 16:
            return 0

    def pass_sm_lett(password):
        """This function checks whether password has one of the letters [a-z]."""
        sm_lett = re.findall("[a-z]", password)
        if len(sm_lett) == 0:
            return 0

    def pass_cap_lett(password):
        """This function checks whether the password
        has one of capital letters [A-Z]."""
        cap_lett = re.findall("[A-Z]", password)
        if len(cap_lett) == 0:
            return 0

    def pass_digits(password):
        """This function checks whether password
        has one og digits [0-9]."""
        digits = re.findall("[0-9]", password)
        if len(digits) == 0:
            return 0

    def pass_symbols(password):
        """This function checks whether password has
        one of symbols [@ or # or $]."""
        symbols = re.findall("#|\$|@", password)
        if len(symbols) == 0:
            return 0

    # Checking results.
    if pass_len(password) == 0:
        return unvalid
    elif pass_sm_lett(password) == 0:
        return unvalid
    elif pass_cap_lett(password) == 0:
        return unvalid
    elif pass_digits(password) == 0:
        return unvalid
    elif pass_symbols(password) == 0:
        return unvalid
    else:
        return valid

password = input("Enter your password: ")

print(pass_check(password))
