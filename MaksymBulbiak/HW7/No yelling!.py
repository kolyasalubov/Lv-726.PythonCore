import unittest

def filter_words(st):
    """
    (str) -> str

    Write a function taking in a string like WOW this is REALLY          
    amazing and returning Wow this is really amazing. String should be
    capitalized and properly spaced. Using re and string is not allowed.
    """
    return " ".join(st.split()).lower().capitalize()


if __name__ == '__main__':
    unittest.main()

    assertEqual('HELLO world!','Hello world!')    