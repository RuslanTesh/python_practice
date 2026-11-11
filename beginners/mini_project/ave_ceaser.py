s = input().split()
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res_words = []

for word in s:
    word_len = 0
    for char in word:
        if char.isalpha():
            word_len += 1
            
    encrypted_word = ''
    for char in word:
        if char in alphabet_lower:
            current_index = alphabet_lower.find(char)
            new_index = (current_index + word_len) % 26
            encrypted_word += alphabet_lower[new_index]
        elif char in alphabet_upper:
            current_index = alphabet_upper.find(char)
            new_index = (current_index + word_len) % 26
            encrypted_word += alphabet_upper[new_index]
        else:
            encrypted_word += char
            
    res_words.append(encrypted_word)

print(*(res_words))
