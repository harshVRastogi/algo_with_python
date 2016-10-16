import Stack


def par_matcher(str_val):
    s = Stack.Stack()
    balanced = True
    index = 0
    while index < len(str_val) and balanced:
        if valid(str_val[index], 0):
            s.push(str_val[index])
        elif valid(str_val[index], 1) and is_equal(s.peek(), str_val[index]):
            s.pop()
        else:
            balanced = False
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def is_equal(o, c):
    l_open = ['{', '[', '(']
    l_close = ['}', ']', ')']
    return l_open.index(o) == l_close.index(c)


def valid(v, t):
    if t == 0:
        return False if "{[(".find(v) == -1 else True
    else:
        return False if "}])".find(v) == -1 else True


print par_matcher("[({})]")
