direction = input("Выберите направление (ш - шифрование, д - дешифрование): ").lower()
language = input("Выберите язык (рус - русский, англ - английский): ").lower()
step = int(input("Введите шаг сдвига (целое число): "))
text = input("Введите текст для обработки: ")

if direction == 'д':
    step = -step

if language == 'англ':
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mod = 26
else:
    alphabet_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphabet_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    mod = 32

res = ''

for i in range(len(text)):
    char = text[i]
    
    if char in alphabet_lower:
        current_index = alphabet_lower.find(char)
        new_index = (current_index + step) % mod
        res += alphabet_lower[new_index]
        
    elif char in alphabet_upper:
        current_index = alphabet_upper.find(char)
        new_index = (current_index + step) % mod
        res += alphabet_upper[new_index]
        
    else:
        res += char

print("Результат:")
print(res)
