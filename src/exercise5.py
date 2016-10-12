import Stack


def par_matcher(str):
    s = Stack.Stack()
    if len(str) == 0:
        return False
    index = 0
    balanced = True
    while index < len(str) and balanced:

        if allowed_open(str[index]) > -1:
            s.push(str[index])

        elif allowed_close(str[index]) > -1:
            s.pop()

        else:
            balanced = False

        index += 1

    if s.size() == 0 and balanced:
        return True

    else:
        return False


def allowed_open(c):
    return "([{".find(c)


def allowed_close(c):
    return ")]}".find(c)


print par_matcher("{({[[()]]}[]([]))}")
