def is_pangram(text):
    alph = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for el in alph:
        if el not in text:
            return False

    return True

text = input().lower()

print(is_pangram(text))
