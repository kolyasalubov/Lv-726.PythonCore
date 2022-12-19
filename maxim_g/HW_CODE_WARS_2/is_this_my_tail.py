def correct_tail(body, tail):
    sub = body[len(body)-1]
    if sub == tail:
        return True
    return False


result = correct_tail("Fox", "x")
print(result)