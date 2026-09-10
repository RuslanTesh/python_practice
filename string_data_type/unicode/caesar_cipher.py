n = int(input())
s = input()
res = ''

for i in range(len(s)):
    current_code = ord(s[i])
    new_code = 97 + (current_code - 97 - n) % 26
    res += chr(new_code)
print(res)