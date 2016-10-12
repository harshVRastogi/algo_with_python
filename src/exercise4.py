import Stack


def par_checker(sym_string):
    balanced = True
    index = 0
    s = Stack.Stack()
    while index < len(sym_string) and balanced:
        symbol = sym_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False


print par_checker("((()))()")
print par_checker("(()()))")
