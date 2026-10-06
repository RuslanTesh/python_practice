s = input()
flag = 'NO'

if s[1] == '-' and s[5] == '-' and s[9] == '-' or s[3] == '-' and s[7] == '-':
    s1 = s.split("-")
    s2 = "".join(s1)

    if len(s1[0]) == 1 and len(s1[1]) == 3 and len(s1[2]) == 3 and len(s1[3]) == 4:
        if s2.isdigit():
            flag = 'YES'


print(flag)