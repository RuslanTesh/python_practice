def string_cleaning(text):
    punctuation = ['.', ',', '!', '?', '-', ' ']
    text = text.lower()
    for el in punctuation:
        if el in text:
            text = text.replace(el, '')

    return text


def is_palindrome(text):
    clean_text = string_cleaning(text)

    if clean_text == clean_text[::-1]:
        return True
    else:
        return False

txt = input()

print(is_palindrome(txt))


