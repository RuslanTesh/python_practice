s = input()
space_count = 1

for i in range(len(s)):
    if s[i] == ' ':
        space_count += 1

print(space_count)