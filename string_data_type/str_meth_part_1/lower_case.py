s = input()
counter = 0

for i in range(len(s)):
    if s[i] in 'abcdefghijklmnopqrstuvxwyz':
        counter += 1

print(counter)