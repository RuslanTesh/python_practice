s = input()

vowel_letters = 'ауоыиэяюеёАУОЫИЭЯЮЕЁ'
consonant_letters = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
vowels = 0
consonants = 0

for i in range(len(s)):
    if s[i] in vowel_letters:
        vowels += 1
    elif s[i] in consonant_letters:
        consonants += 1
    else:
        continue

print('Количество гласных букв равно', vowels)
print('Количество согласных букв равно', consonants)
