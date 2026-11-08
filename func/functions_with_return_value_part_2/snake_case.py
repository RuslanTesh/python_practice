def convert_to_python_case(text):
    text = ' '.join(text).split()
    for i in range(len(text)):
        if text[i].isupper():
            temp = text[i].lower()
            text[i] = f'_{temp}'
    new_text = ''.join(text)
    return new_text[1:]

txt = input()

print(convert_to_python_case(txt))




