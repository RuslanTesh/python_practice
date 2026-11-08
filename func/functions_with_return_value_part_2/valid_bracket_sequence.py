def is_correct_bracket(text):
    open = 0
    close = 0

    for el in text:
        if el == '(':
            open += 1
        elif el == ')':
            close += 1

        if close > open:
            return False

    if open == close:
        return True
    else:
        return False

txt = input()

print(is_correct_bracket(txt))




