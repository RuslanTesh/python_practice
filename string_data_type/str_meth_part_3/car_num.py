s = input()
l = 'АВЕКМНОРСТУХ'

if len(s) == 9 or len(s) == 10:
    digits = s[1:4]
    code = s[7:]
    
    if (s[6] == '_' 
        and (len(code) == 2 or len(code) == 3)
        and code.isdigit() 
        and s[0] in l
        and digits.isdigit()
        and s[4] in l
        and s[5] in l): 
        print('YES')
    else:
        print('NO')
else:
    print('NO')
