def greet(name):
    """
    (str) -> str

    Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
    Can you help her?

    Example (Input --> Output)

    'Johny' --> 'Hello, my love!'
    'James' --> 'Hello, James!'
    """

    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

print(greet("Johnny"))
print(greet("James"))