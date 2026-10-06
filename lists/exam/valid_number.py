s = input()
flag = 'NO'

s1 = s.split("-")
s2 = "".join(s1)

if s2.isdigit():
    if len(s1) == 4 and len(s1[0]) == 1 and len(s1[1]) == 3 and len(s1[2]) == 3 and len(s1[3]) == 4:
        if s[0] == '7': 
            flag = 'YES' 
            
    elif len(s1) == 3 and len(s1[0]) == 3 and len(s1[1]) == 3 and len(s1[2]) == 4:
        flag = 'YES'

print(flag)