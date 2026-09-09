s = input()
name = s[1:]

if s.startswith('@') and (5 <= len(s) <= 15) and name.isalnum():
    if name.islower() or name.isdigit():
        print('Correct')
    else:
        print('Incorrect')
else:
    print('Incorrect')
